from tkinter import *

#create root window 
root = Tk()
#dimensions of window and title
root.geometry("960x540")
root.title("AI Text Detector")


heading = Label(text = "AI TEXT DETECTOR", font = ("Monospace", 30))
enterText = Entry() 
textArea = Text(height = 5, width = 25, font = ("arial", 10)) 

#place widgets on top of eachother 
heading.pack()
enterText.pack()
textArea.pack() 
#code keeps displaying - keeps window open 
mainloop() 