from tkinter import *
from tkinter import filedialog

inputText = ""
inputSize = 0




#TKinter Name Is Master
master = Tk()

def callback():
    #Input Stuff
    
    inputText = (e.get())
    inputSize = (len(e.get().split()))

    print(inputText)
    inputTextSize.config(state = "normal")
    inputTextSize.delete(0, END)
    inputTextSize.insert(0, "Word Count:"+str(inputSize))
    inputTextSize.config(state = "disabled")

    #Output Stuff
    #textSummarizer(inputText) this line is an example for  what will happen when the two scripts are combined


    outputTextSize.config(state = "normal")
    outputTextSize.delete(0, END)
    outputTextSize.insert(0, "Word Count:"+str(inputSize))
    outputTextSize.config(state = "disabled")


#Gets user to put file in and also reads and puts file into other function called "callback"
def chooseFile():
    print("File Upload Start")
    file = filedialog.askopenfile(parent=master,mode='rb',title='Choose a file')
    if file != None:
        data = file.readlines()
        file.close()
        print(data)
        data = str(data)
        e.delete(0, END)
        e.insert(0,data)
        callback()
        print("File Upload End")


#Title
master.title("Text Summerizer V 1.0")
#Button
b = Button(master, text="Submit", width=10, command=callback)
b.grid(row = 0, column = 0)

#Text
title = Label(master, text="Text Summarizer", width=30)
title.grid(row = 0, column = 2)

#Input Text
e = Entry(master, text = "Put Text Here")
e.grid(row = 1, column = 2)
e.insert(0, "Input Text")

inputTextSize = Entry(master, text="N/A", width=30, state = DISABLED)
inputTextSize.grid(row = 1, column = 0)

#Output Text
outputEntry = Entry(master)
outputEntry.grid(row = 2, column = 2)
outputEntry.insert(0, "Output Text")
outputEntry.config(state = DISABLED)

outputTextSize = Entry(master, text="N/A", width=30, state = DISABLED)
outputTextSize.grid(row = 2, column = 0)



readFile = Button(master, text="Upload .Txt File", command=chooseFile)
readFile.grid(row=5)

mainloop()
