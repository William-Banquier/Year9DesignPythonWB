from termcolor import cprint
import tkinter as tk #Import
import random as r

cprint("Start Program","green") #Start

root = tk.Tk() #Root


def butn2Time():
    btn3 = tk.Button(root)
    btn3.config(width = 20+r.randrange(0,10), height = 10+r.randrange(0,10), text = "Me Too",command = butn2Time)
    btn3.pack()

def facts():
    btn2 = tk.Button(root)
    btn2.config(width = 20+r.randrange(0,10), height = 10+r.randrange(0,10), text = "I am also a button",command = butn2Time)
    btn2.pack()


#Widget is a element in a GUI



btn1 = tk.Button(root)
#Configure
btn1.config(width = 20, height = 10, text = "I am a button",command = facts)
#Place widget - pack(), grid()


#    output = tk.Text(root, width = 100, height = 20,bg="grey")
 #   output.config()
  #  output.pack()
btn1.pack()



root.mainloop() #Loop

cprint("End Program","red") #End


