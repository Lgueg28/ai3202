import sys

def main():
	#Get File name as Input
	if (len(sys.argv) != 2):
		print "Bad Input Argument(s). Correct Usage: python hmmPart1.py fileName"
		return
	fileName = sys.argv[1]

	#I will be using this to construct the dictionaries
	alphabetArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "_"]
	emissionDictionary = {}
	transitionDictionary  = {}
	startStateDictionary = {}	

	#Construct dictionary structure for all calculations
	for letter in alphabetArray:
		emissionDictionary[letter] = {}
		transitionDictionary[letter]  = {}
	        startStateDictionary[letter] = 0
		for key in alphabetArray:
			emissionDictionary[letter][key] = 0
			transitionDictionary[letter][key]  = 0

	#Parse Input file using below rules, each word is an array in megaArray. Each state and output is modeled by an array of [state, output]
	with open(fileName) as f:
		megaArray = []
		tempWord = [] 
		for line in f:
			#if word is done, append to megaArray then empty tempWord
			if (line[0] == "_"):
				#also 
				tempWord.append( ["_", "_"] )
				megaArray.append(tempWord)
				tempWord = []
			#append (state, output) to tempWord
			else:
				tempWord.append( [line[0], line[2]] )
	
	#Call calculation functions
	calcEmission(megaArray, emissionDictionary)
	calcTransition(megaArray, transitionDictionary)
	calcStartState(megaArray, startStateDictionary)

#Calculates the emission probability
def calcEmission(megaArray, emissionDictionary):
	
	print "Emission Probabilities Format -- > P( output | state ): "
	print ""
	#Construct alphabet Dictionary using below counters
	for i in emissionDictionary:
		stateCount = 0
		for index in range(0, len(megaArray)):
			for pair in megaArray[index]:
				#If we have a state "a", look at the output and increment emission counter
				if (pair[0] == i):
					stateCount = stateCount + 1
					emissionDictionary[i][pair[1]] = emissionDictionary[i][pair[1]] + 1		
		
		#Laplace and then print the Emission dictionary data
		for j in emissionDictionary[i]:
			emissionDictionary[i][j] = (emissionDictionary[i][j] + 1) / (float(stateCount) + 27)
			print "P( " + j  + " | " +  i  + " ): " + str(round(emissionDictionary[i][j], 6))
	return

#calculates the emission probability
def calcTransition(megaArray, transitionDictionary):
	print "_________________________________________________________________"
	print ""
	print ""
	print "Transition Probabilities Format -- > P( state + 1 | state ): "
	print ""
	#Construct Transition Dictionary using below counters
        for i in transitionDictionary:
                stateCount = 0
                for index in range(0, len(megaArray)):
                        for pairIndex in range(0, len(megaArray[index])-1):
				#If we have a state of "a", look at the next state and increment transition counter 
                                if (megaArray[index][pairIndex][0] == i):
					transitionLetter = megaArray[index][pairIndex+1][0] 
                                        stateCount = stateCount + 1
                                        transitionDictionary[i][transitionLetter] = transitionDictionary[i][transitionLetter] + 1

		#Laplace and then print the Transition dictionary data
                for j in transitionDictionary[i]:
                        transitionDictionary[i][j] = (transitionDictionary[i][j] + 1) / (float(stateCount) + 27)
			print "P( " + j + " | " + i + " ): " + str(round(transitionDictionary[i][j], 6))
	
#calculates the start state	
def calcStartState(megaArray, startStateDictionary):
	print "_________________________________________________________________"
        print ""
        print ""
        print "Start State Probabilities Format -- > P( state ): "
	print ""
	#Construct Start State Dictionary using below counters
        for i in startStateDictionary:
		totalLetters = 0
                for index in range(0, len(megaArray)):
                        for pairIndex in range(0, len(megaArray[index])):
				#Calculates total letters in the state column
				totalLetters = totalLetters + 1
				#Implement state counter
                                if (megaArray[index][pairIndex][0] == i):
                                        startStateDictionary[i] =  startStateDictionary[i] + 1
		
		#Divide to get the probability
		startStateDictionary[i] = startStateDictionary[i]/float(totalLetters)
                print "P( " + i + " ): " + str(round(startStateDictionary[i], 6))

if __name__ == "__main__": main()
	
