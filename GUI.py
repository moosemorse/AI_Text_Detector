from tkinter import *

percent = 0 
#create root window 
root = Tk()
#dimensions of window and title
root.geometry("960x540")
root.title("AI Text Detector")

textArea = Text(height = 15, width = 60, font = ("arial", 10))  

def submit(): 
    print(textArea.get("1.0", "end-1c")) #placeholder before we implement model 

def clearText(): 
    textArea.delete("1.0", "end") 

heading = Label(text = "AI TEXT DETECTOR", font = "Monospace 30 bold")
examples = Label()
submitBtn = Button(text = "Submit", bg = "#04AA6D", height = 2, width = 10, command=submit)
clearBtn = Button(text = "Clear", height = 2, width = 10, command =clearText)
percentage = Label(text = str(percent) + " %", font = ("Monospace", 30))



#place widgets on top of eachother 
heading.pack()
textArea.pack()
clearBtn.pack()
submitBtn.pack()
percentage.pack()
#code keeps displaying - keeps window open 
mainloop() 