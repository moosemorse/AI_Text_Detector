from tkinter import *

#create root window 
root = Tk()
#dimensions of window and title
root.geometry("960x540")
root.title("AI Text Detector")


heading = Label(text = "AI TEXT DETECTOR", font = ("Monospace", 30))

#place widgets on top of eachother 
heading.pack(side = TOP)

#code keeps displaying - keeps window open 
mainloop() 