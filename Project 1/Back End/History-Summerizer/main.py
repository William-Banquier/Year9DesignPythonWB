##############################################################################



#WORKING YAAAAAAAAYYYYYY




#file = open("historicalText.txt","r+")

#Sample Text



def hisSum(his):
	
	#file = open("shortText.txt","r+")
	shortText = "national:nat government:gov institution:inst international:internat official:off corporation:corp corporate:corp federal:fed department:depart canada:CAN".split()
	longWord = []
	shortWord = []
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
	print(finalSentanceCount)
	finalSentance = (final.split("."))

	for i in range(finalSentanceCount):
		#print(finalSentance[i])#,y)
		quickEnd = False
		for y in range(len(ndictionary.split())):
			if  ndictionary.split()[y] in finalSentance[i] and quickEnd == False:
				trueFinal += finalSentance[i]
				quickEnd == True
				break


	print(trueFinal)


hisSum("The politics of Canada function within a framework of parliamentary democracy and a federal system of parliamentary government with strong democratic traditions.[1] Canada is a constitutional monarchy, in which the monarch is head of state. In practice, the executive powers are directed by the Cabinet, a committee of ministers of the Crown responsible to the elected House of Commons of Canada and chosen and headed by the Prime Minister of Canada.[2] Canada is described as a full democracy,[3] with a tradition of liberalism,[4] and an egalitarian,[5] moderate political ideology.[6][7][8] Far-right and far-left politics have never been a prominent force in Canadian society.[9][10] Peace, order, and good government, alongside an implied bill of rights are founding principles of the Canadian government.[11][12] An emphasis on social justice has been a distinguishing element of Canada's political culture.[13] Canada has placed emphasis on equality and inclusiveness for all its people.[14] The country has a multi-party system in which many of its legislative practices derive from the unwritten conventions of and precedents set by the Westminster parliament of the United Kingdom. The two dominant political parties in Canada have historically been the Liberal Party of Canada and the Conservative Party of Canada (or its predecessors) however, the social democratic New Democratic Party (NDP) has risen to prominence and even threatened to upset the two other established parties during the 2011 federal election. Smaller parties like the Quebec nationalist Bloc Québécois and the Green Party of Canada have also been able to exert their own influence over the political process. Canada has evolved variations: party discipline in Canada is stronger than in the United Kingdom, and more parliamentary votes are considered motions of confidence, which tends to diminish the role of non-Cabinet members of parliament (MPs). Such members, in the government caucus, and junior or lower-profile members of opposition caucuses, are known as backbenchers. Backbenchers can, however, exert their influence by sitting in parliamentary committees, like the Public Accounts Committee or the National Defence Committee.")

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