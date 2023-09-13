from tkinter import *
from classify_comments import classify_text
from model_class import ChatGPT_Classifier

percent = 0 
#create root window 
root = Tk()
#dimensions of window and title
root.geometry("550x560")
root.title("AI Content Detector")
#Disable the resizable property 
root.resizable(False, False) 

textArea = Text(height = 15, width = 75, font = "Arial 10" )  

def submit(): 
	#paramters: 
	# 1.0 means input should be read from line one 
	# end: reads until end of text 
	# 1c: removes 1 char starting from end 
	global percent 
	percent = int(100 * classify_text(textArea.get("1.0", "end-1c"))); 
	global percentage 
	percentage.config(text=str(percent) + "% chance of AI-generated")


def clearText(): 
	textArea.delete("1.0", "end") 
	global percentage 
	percentage.config(text="0 %")
	
#loads AI text into text Area 
def aiText(): 
		clearText()
		try: 
			with open("examples/aitxt.TXT") as file: 
				text = file.read()
				textArea.insert(END, text) 
		except Exception as e: 
			print(e)  

#loads human text into textArea 
def humanText(): 
		clearText()
		try: 
			with open("examples/humantxt.TXT") as file: 
				text = file.read()
				textArea.insert(END, text) 
		except Exception as e: 
			print(e)    
			
#widget creation 
heading = Label(text = "AI CONTENT DETECTOR", font = "Monospace 30 bold")
examples = Label(text = "Examples: ", font = "Monospace 20")
aiExample = Button(text = "AI", height = 2, width = 10, command = aiText)
humanExample = Button(text = "Human", height = 2, width = 10, command = humanText)
percentage = Label(text = str(percent) + " %", font = ("Monospace", 30))
submitBtn = Button(text = "Submit", bg = "#04AA6D", height = 2, width = 10, command=submit)
clearBtn = Button(text = "Clear", height = 2, width = 10, command =clearText)
scrollbar = Scrollbar() 


#geometry management 
heading.grid(row = 0, column = 0, pady = 2, padx = 10) 
examples.grid(row = 1, column = 0, pady = 10,  padx = 10, sticky = W) 
aiExample.grid(row = 1, column = 0, pady = 10, padx = 100, sticky = E) 
humanExample.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = E) 
textArea.grid(row = 2, column = 0, pady = 20, padx = 10)
clearBtn.grid(row = 3, column = 0, padx = 100, sticky = E)
submitBtn.grid(row = 3, column = 0, padx = 10, sticky = E)  
percentage.grid(row = 5, column = 0, pady = 30) 

#code keeps displaying - keeps window open 
mainloop() 