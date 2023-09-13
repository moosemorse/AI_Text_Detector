from transformers import RobertaConfig, AutoModel, get_cosine_schedule_with_warmup
import torch.nn as nn
import math
from torchmetrics.functional.classification import auroc
import torch.nn.functional as F
import torch 
import pytorch_lightning as pl

class ChatGPT_Classifier(pl.LightningModule):
  #roberta is a pretrained model that can be used for many downstream task
  #in our context we are using it for classification so we'd want to append a classification head onto the end of the model
  #to improve our performance even more, we will add a 2 layer neural network to the end (so a hidden layer --> final layer)
  def __init__(self, config):
    super().__init__()
    self.config = config
    #AutoModel automatically assigns compatible model according to model_name set in dictionary
    self.pretrained_model = AutoModel.from_pretrained(config['model_name'], return_dict = True)
    #hidden layer
    self.hidden = nn.Linear(self.pretrained_model.config.hidden_size, self.pretrained_model.config.hidden_size)
    #classification layer
    self.classifier = nn.Linear(self.pretrained_model.config.hidden_size, self.config['n_labels'])
    #torch can automatically initialise these layers, but using xavier_uniform_
    #means we can initialise the weight of the NN layer ==> improving performance
    torch.nn.init.xavier_uniform_(self.hidden.weight)
    torch.nn.init.xavier_uniform_(self.classifier.weight)
    #loss function - Binary cross entropy with logits loss to pass in our output
    #labels to create a single loss which we can then backpropogate to our network
    #BCEwithlogitsloss is more numerically stable - it combines a sigmoid layer and BCE in a single class
    self.loss_func = nn.BCEWithLogitsLoss(reduction='mean')
    #dropout layer - randomly turns on/off several nodes in NN every iteration,
    #as a form of some regularization
    self.dropout = nn.Dropout()

  def forward(self, input_ids, attention_mask, labels=None):
    #roberta model
    output = self.pretrained_model(input_ids = input_ids, attention_mask = attention_mask)
    #use a mean output as its a better representation of the entire sentence
    #dimension we take the mean on is the first dimension
    #since this is the tokens we have
    pooled_output = torch.mean(output.last_hidden_state, 1)
    #nerual network classification layers
    #pass pooled_output through hidden layer
    pooled_output = self.hidden(pooled_output)
    #pass pooled_output into dropout layer which forces the model to try
    #classify a sentence with only a few tokens left
    pooled_output = self.dropout(pooled_output)
    #pass pooled_output through activation function (relu)
    pooled_output = F.relu(pooled_output)
    #final output (=logits)
    logits = self.classifier(pooled_output)
    #calculate loss
    loss = 0
    #if labels are present this means that we are using training data
    #hence a loss is calculated
    if labels is not None:
      labels = labels.to(logits.dtype)
      loss = self.loss_func(logits.view(-1, self.config['n_labels']), labels.view(-1, self.config['n_labels']) )
    return loss, logits

  #unpack batch and pass through model
  #return loss, predictions and labels for evaluation later
  def training_step(self, batch, batch_index):
    loss, logits = self(**batch)
    self.log("train loss", loss, prog_bar = True, logger = True)
    return {"loss": loss, "predictions": logits, "labels": batch['labels']}

  def testing_step(self, batch, batch_index):
    loss, logits = self(**batch)
    self.log("test loss", loss, prog_bar = True, logger = True)
    return {"test_loss": loss, "predictions": logits, "labels": batch['labels']}

  def predict_step(self, batch, batch_index):
    #unpack contents of dictionary (batch) and pass in as kwargs
    none, logits = self(**batch)
    return logits

  def configure_optimizers(self):
    optimiser = torch.optim.AdamW(self.parameters(), lr=self.config['lr'], weight_decay = self.config['w_decay'])
    #train_size/batch size
    total_steps = self.config['train_size'] / self.config['bs']
    #this is needed as we a have a warmup period for the
    warmup_steps = math.floor(total_steps *  self.config['warmup'])
    scheduler = get_cosine_schedule_with_warmup(optimiser, warmup_steps, total_steps)
    return [optimiser], [scheduler]