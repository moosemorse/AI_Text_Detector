from tkinter import *

percent = 0 
#create root window 
root = Tk()
#dimensions of window and title
root.geometry("960x540")
root.title("AI Text Detector")


heading = Label(text = "AI TEXT DETECTOR", font = ("Monospace", 30))
submitBtn = Button(text = "Submit", bg = "#04AA6D" )
textArea = Text(height = 10, width = 50, font = ("arial", 10)) 
percentage = Label(text = percent, font = ("Monospace", 30))

#place widgets on top of eachother 
heading.pack()
textArea.pack() 
submitBtn.pack()
percentage.pack() 
#code keeps displaying - keeps window open 
mainloop() 