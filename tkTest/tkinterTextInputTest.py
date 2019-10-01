# importing tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter.messagebox import askyesno 


def printSave():
    print("hi")
    print(input_text)

# creating root 
root = Tk() 
  
# specifying geometry 
root.geometry('200x100') 
  
# This is used to take input from user 
# and show it in Entry Widget. 
# Whatever data that we get from keyboard 
# will be treated as string. 
input_text = StringVar() 
  
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
  
# focus_force is used to take focus 
# as soon as application starts 
entry1.focus_force() 
entry1.pack(side = TOP, ipadx = 30, ipady = 6) 
  
save = ttk.Button(root, text = 'Save', command = "printSave")
save.pack(side = TOP, pady = 10) 

  
root.mainloop() 