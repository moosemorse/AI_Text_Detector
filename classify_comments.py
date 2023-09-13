import torch 
from transformers import RobertaTokenizer
import joblib 
from model_class import ChatGPT_Classifier

def classify_text(text):  

    #load the model from pickle (serialised file) 
    model = joblib.load('model/TATG_Model_Copy')

    tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

    model.eval() 

    with torch.no_grad(): 
        text = str(text) 
        token_text = tokenizer.encode_plus(text, 
                                        add_special_tokens = True, 
                                        return_tensors = 'pt', 
                                        return_attention_mask = True)
        logits = model(**token_text)
        final_result = torch.sigmoid(torch.Tensor(logits)) 
    
    #final result in form of tensor 
    #cast tensor into int 
    final_result = final_result[1].item() 
    final_result = 1 - final_result

    return final_result

