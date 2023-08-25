from tkinter import *

percent = 0 
#create root window 
root = Tk()
#dimensions of window and title
root.geometry("450x540")
root.title("AI Text Detector")
#Disable the resizable property 
root.resizable(False, False) 

textArea = Text(height = 15, width = 60)  

def submit(): 
    #paramters: 
	# 1.0 means input should be read from line one 
	# end: reads until end of text 
	# 1c: removes 1 char starting from end 
    print(textArea.get("1.0", "end-1c")) 

def clearText(): 
    textArea.delete("1.0", "end")

#loads AI text into text Area 
def aiText(): 
		clearText()
		try: 
			with open("AI_Text_Detector/examples/aitxt.TXT") as file: 
				text = file.read()
				textArea.insert(END, text) 
		except Exception as e: 
			print(e)  

#loads human text into textArea 
def humanText(): 
		clearText()
		try: 
			with open("AI_Text_Detector/examples/humantxt.TXT") as file: 
				text = file.read()
				textArea.insert(END, text) 
		except Exception as e: 
			print(e)    
			
#widget creation 
heading = Label(text = "AI TEXT DETECTOR", font = "Monospace 30 bold")
examples = Label(text = "Examples: ", font = "Monospace 20")
aiExample = Button(text = "AI", height = 2, width = 10, command = aiText)
humanExample = Button(text = "Human", height = 2, width = 10, command = humanText)
submitBtn = Button(text = "Submit", bg = "#04AA6D", height = 2, width = 10, command=submit)
clearBtn = Button(text = "Clear", height = 2, width = 10, command =clearText)
percentage = Label(text = str(percent) + " %", font = ("Monospace", 30))
scrollbar = Scrollbar() 


#geometry management 
heading.grid(row = 0, column = 0, pady = 2, padx = 10) 
examples.grid(row = 1, column = 0, padx = 10, sticky = W) 
aiExample.grid(row = 1, column = 0, padx = 120, sticky = E) 
humanExample.grid(row = 1, column = 0, padx = 20, sticky = E) 
textArea.grid(row = 2, column = 0, pady = 20, padx = 10)
clearBtn.grid(row = 3, column = 0, padx = 100, sticky = E)
submitBtn.grid(row = 3, column = 0, padx = 10, sticky = E)  
percentage.grid(row = 5, column = 0, pady = 30) 

#code keeps displaying - keeps window open 
mainloop() 