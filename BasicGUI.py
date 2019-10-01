from termcolor import cprint
import tkinter as tk #Import

cprint("Start Program","green") #Start

root = tk.Tk() #Root

#Widget is a element in a GUI

#Step one construct the widget

btn1 = tk.Button(root)
#Configure
btn1.config(width = 10, height = 30, text = "I am a button")
#Place widget - pack(), grid()


output = tk.Text(root, width = 100, height = 20)
output.config()

btn1.pack()
output.pack()

root.mainloop() #Loop

cprint("End Program","red") #End


