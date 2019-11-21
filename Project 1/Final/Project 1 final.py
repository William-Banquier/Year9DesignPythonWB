from tkinter import *
from tkinter import filedialog
import os
inputText = ""
inputSize = 0







def callback(string):
    #Input Stuff

    inputSize = (len(e.get().split()))
    
    print(inputSize)

    inputTextSize.config(state = "normal")
    inputTextSize.delete(0, END)
    inputTextSize.insert(0, "Word Count:"+str(inputSize))
    inputTextSize.config(state = "disabled")

    #Output Stuff
    #textSummarizer(inputText) this line is an example for  what will happen when the two scripts are combined

    outputEntry.config(state = "normal")
    outputEntry.delete(0, END)
    outputEntry.insert(0, string)
    #outputEntry.config(state = "disabled")
    print(len(string.split()))

    outputTextSize.config(state = "normal")
    outputTextSize.delete(0, END)
    outputTextSize.insert(0, "Word Count:"+str(len(string.split())))
    outputTextSize.config(state = "disabled")




##############################################################################



#WORKING YAAAAAAAAYYYYYY




#file = open("historicalText.txt","r+")

#Sample Text



def hisSum():
	
    his = (e.get())

    #file = open("shortText.txt","r+")
    shortText = ("national:nat government:gov institution:inst international:internat official:off corporation:corp corporate:corp federal:fed department:depart canada:CAN").split()

    longWord = [""]
    shortWord = [""]
    for i in range(0,len(shortText)):
        longWord.append(shortText[i].split(":")[0])
        shortWord.append(shortText[i].split(":")[1])
    #.split("\n")[0])


    #print(shortWord,longWord)

    
    output = []
    # for i in range(len(his)):
    # 	for y in range(0,len(longWord)):
    # 		his[i] = ((his[i].lower().replace(longWord[y],shortWord[y])))


    final = his
    #final += his
    #print(final.split("\n")[0],"\n\n",final.split("\n")[-2])

    dictionary = his.split(".")[0]
    ndictionary = ""
    for i in range(0,len(dictionary.split())):
        #print(len(dictionary.split()[i]))
        if (len(dictionary.split()[i])) > 10:
            #print(i)
            ndictionary+=dictionary.split()[i]+" "
    #print(dictionary.split())
    #print(ndictionary)
    #print("\n")

    trueFinal = ""
    quickEnd = False


    finalSentanceCount = len(final.split("."))
    #print(finalSentanceCount)
    finalSentance = (final.split("."))

    for i in range(finalSentanceCount):
        #print(finalSentance[i])#,y)
        quickEnd = False
        for y in range(len(ndictionary.split())):
            if  ndictionary.split()[y] in finalSentance[i] and quickEnd == False:
                trueFinal += finalSentance[i]+". "
                quickEnd == True
                break

    os.system("clear")
    print(trueFinal)
    callback(trueFinal)


    #hisSum("The politics of Canada function within a framework of parliamentary democracy and a federal system of parliamentary government with strong democratic traditions.[1] Canada is a constitutional monarchy, in which the monarch is head of state. In practice, the executive powers are directed by the Cabinet, a committee of ministers of the Crown responsible to the elected House of Commons of Canada and chosen and headed by the Prime Minister of Canada.[2] Canada is described as a full democracy,[3] with a tradition of liberalism,[4] and an egalitarian,[5] moderate political ideology.[6][7][8] Far-right and far-left politics have never been a prominent force in Canadian society.[9][10] Peace, order, and good government, alongside an implied bill of rights are founding principles of the Canadian government.[11][12] An emphasis on social justice has been a distinguishing element of Canada's political culture.[13] Canada has placed emphasis on equality and inclusiveness for all its people.[14] The country has a multi-party system in which many of its legislative practices derive from the unwritten conventions of and precedents set by the Westminster parliament of the United Kingdom. The two dominant political parties in Canada have historically been the Liberal Party of Canada and the Conservative Party of Canada (or its predecessors) however, the social democratic New Democratic Party (NDP) has risen to prominence and even threatened to upset the two other established parties during the 2011 federal election. Smaller parties like the Quebec nationalist Bloc Québécois and the Green Party of Canada have also been able to exert their own influence over the political process. Canada has evolved variations: party discipline in Canada is stronger than in the United Kingdom, and more parliamentary votes are considered motions of confidence, which tends to diminish the role of non-Cabinet members of parliament (MPs). Such members, in the government caucus, and junior or lower-profile members of opposition caucuses, are known as backbenchers. Backbenchers can, however, exert their influence by sitting in parliamentary committees, like the Public Accounts Committee or the National Defence Committee.")

    #dictionary= longWord
    #fakeDictionary= []

    #trueFinish = ""
    # for i in range(0,len(final[0].split("."))):
    # 	fakeDictionary += final[0].split()[i].split()
    # 	if (len(fakeDictionary[i])) >3:
    # 		dictionary+=final[0].split()[i].split()

    # #print(dictionary)


    # for i in range(len(final)):
    # 	for y in range(len(final[i].split("."))):
    # 		for z in range(len(dictionary)):
    # 			if dictionary[z] in final[i].split()[y].lower() :
    # 				trueFinish+=final[i].split(".")[y]+" "
    #print(final)
    #print(trueFinish)
    ###########################################################################################






def quickCopy():
    master.clipboard_append(outputEntry.get())




#TKinter Name Is Master
master = Tk()



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
        hisSum()
        print("File Upload End")



#Title
master.title("Text Summerizer V 1.0")
#Button
b = Button(master, text="Submit", width=10, command=hisSum)
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

outputTextSize = Entry(master, text="", width=30, state = DISABLED)
outputTextSize.grid(row = 2, column = 0)



readFile = Button(master, text="Upload .Txt File", command=chooseFile)
readFile.grid(row=5,column = 0)

copyFile = Button(master, text="Copy To Clipboard", command=quickCopy)
copyFile.grid(row=5,column = 2)


mainloop()
