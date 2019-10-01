from tkinter import * 
window = Tk()
number1 = False
number2 = False


def number1Int():
    global number1
    if number1 == True:
        number1 = False
    else:
        number1 = True 
    print(number1)

def number2Int():
    global number2
    if number2 == True:
        number2 = False
    else:
        number2 = True 
    print(number2)

button1 = Button(window, command = number1Int,text="1")
button1.pack()
button2 = Button(window, command = number2Int,text="2")
button2.pack()

window.mainloop()