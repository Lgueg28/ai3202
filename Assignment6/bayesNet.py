import getopt, sys

def initDictionary():
    #initialze pollution dictionary
    nodesDictionary = {}
    nodesDictionary['pollution'] = {}
    nodesDictionary['pollution']['low'] = 0.9
    nodesDictionary['pollution']['high'] = 0.1
    nodesDictionary['smoker'] = {}
    nodesDictionary['smoker']['true'] = 0.3
    nodesDictionary['smoker']['false'] = 0.7
    nodesDictionary['cancer'] = {}
    nodesDictionary['cancer']['HT'] = 0.05
    nodesDictionary['cancer']['HF'] = 0.02
    nodesDictionary['cancer']['LT'] = 0.03
    nodesDictionary['cancer']['LF'] = 0.001
    nodesDictionary['dyspnoea'] = {}
    nodesDictionary['dyspnoea']['true'] = 0.65
    nodesDictionary['dyspnoea']['false'] = 0.30
    nodesDictionary['xray'] = {}
    nodesDictionary['xray']['true'] = 0.90
    nodesDictionary['xray']['false'] = 0.20
    return nodesDictionary

#function calculates the probability of cancer based on values of pollution and smoker
def calcProbCancer(dictionary):
	probCancer = (dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['cancer']['HF'] * dictionary['pollution']['high'] * dictionary['smoker']['false']) + (dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false'])
	return probCancer

#calculates marginal probability for specified node
def calcMarginal(name, dictionary):
	probCancer = calcProbCancer(dictionary)
	print "Marginal Probability for: " + name
	if ( name == 'cancer' ):
		print "The Probability of cancer is: " + str(probCancer)
		print "The Probability of NO cancer is: " + str(1 - probCancer)
	elif ( name == 'dyspnoea' ):
		margDyspnoea = (probCancer * dictionary[name]['true']) + ( (1-probCancer) * dictionary[name]['false'])
		print "The Probability of Dyspnoea is: " + str(margDyspnoea)
		print "The Probability of NO Dyspnoea is: " + str(1-margDyspnoea)
	elif ( name == 'xray' ):
		margXRay = (probCancer * dictionary[name]['true']) + ( (1-probCancer) * dictionary[name]['false'])
		print "The probability of a Positive xRay is: " + str(margXRay)
		print "The probability of a negative xRay is: " + str(1-margXRay)
	elif ( name == 'smoker'):
		print "The Probabilty of being a smoker is: " + str(dictionary[name]['true'])
		print "The Probability of not being a smoker is: " + str(dictionary[name]['false'])
	elif ( name == 'pollution'):
		print "The probability of low pollution is: " + str(dictionary[name]['low'])
		print "The probability of high pollution is: " + str(dictionary[name]['high'])

def calcJoint(flags, dictionary):
	dyspnoea = None
	xray = None
	cancer = None 
	smoker = None
	pollution = None
	if "D" in flags:
		dyspnoea = "All"
	if "~d" in flags:
		dyspnoea = False
	elif "d" in flags:
		dyspnoea = True
	if "X" in flags:
		xray = "All"
        if "~x" in flags:
		xray = False
        elif "x" in flags: 
		xray = True
 	if "C" in flags:
		cancer = "All"
        if "~c" in flags:
		cancer = False
        elif "c" in flags: 
		cancer = True
	if "P" in flags:
		pollution = "All"	
        if "~p" in flags:
		pollution = False
        elif "p" in flags: 
		pollution = True
	if "S" in flags:
		smoker = "All"	
        if "~s" in flags:
		smoker = False
        elif "s" in flags:
		smoker = True
	
	if (cancer == 'All' and smoker == 'All' and pollution == 'All' and (dyspnoea == 'All' or xray == 'All')):
        	probCancerLT = (dictionary['pollution']['low'] * dictionary['smoker']['true'] * dictionary['cancer']['LT'])
          	probCancerLF = dictionary['pollution']['low'] * dictionary['smoker']['false'] * dictionary['cancer']['LF']
          	probCancerHT = dictionary['pollution']['high'] * dictionary['smoker']['true'] * dictionary['cancer']['HT']
          	probCancerHF = dictionary['pollution']['high'] * dictionary['smoker']['false'] * dictionary['cancer']['HF']

          	probNotCancerLT = dictionary['pollution']['low'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['LT'])
           	probNotCancerLF = dictionary['pollution']['low'] * dictionary['smoker']['false'] * (1-dictionary['cancer']['LF'])
             	probNotCancerHT = dictionary['pollution']['high'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['HT'])
            	probNotCancerHF = dictionary['pollution']['high'] * dictionary['smoker']['false'] * (1-dictionary['cancer']['HF'])
		
		if(dyspnoea == 'All'):
			print "dcsp: " + str(probCancerLT * dictionary['dyspnoea']['true'])
			print "dc~sp: " + str(probCancerLF * dictionary['dyspnoea']['true'])  
			print "dcs~p: " + str(probCancerHT * dictionary['dyspnoea']['true'])  
			print "dc~s~p: " + str(probCancerHF * dictionary['dyspnoea']['true'])
			print "d~csp: " + str(probNotCancerLT * dictionary['dyspnoea']['false'])             
                	print "d~c~sp: " + str(probNotCancerLF * dictionary['dyspnoea']['false'])
                	print "d~cs~p: " + str(probNotCancerHT * dictionary['dyspnoea']['false'])
                	print "d~c~s~p: " + str(probNotCancerHF * dictionary['dyspnoea']['false'])
			print "~dcsp: " + str(probCancerLT * (1-dictionary['dyspnoea']['true']))
                	print "~dc~sp: " + str(probCancerLF * (1-dictionary['dyspnoea']['true']))
                	print "~dcs~p: " + str(probCancerHT * (1-dictionary['dyspnoea']['true']))
                	print "~dc~s~p: " + str(probCancerHF * (1-dictionary['dyspnoea']['true']))
               		print "~d~csp: " + str(probNotCancerLT * (1-dictionary['dyspnoea']['false']))
                	print "~d~c~sp: " + str(probNotCancerLF * (1-dictionary['dyspnoea']['false']))
                	print "~d~cs~p: " + str(probNotCancerHT * (1-dictionary['dyspnoea']['false']))
               		print "~d~c~s~p: " + str(probNotCancerHF * (1-dictionary['dyspnoea']['false']))
  	 		return

		if(xray == 'All'):
			print "xcsp: " + str(probCancerLT * dictionary['xray']['true'])
                        print "xc~sp: " + str(probCancerLF * dictionary['xray']['true'])
                        print "xcs~p: " + str(probCancerHT * dictionary['xray']['true'])
                        print "xc~s~p: " + str(probCancerHF * dictionary['xray']['true'])
                        print "x~csp: " + str(probNotCancerLT * dictionary['xray']['false'])     
                        print "x~c~sp: " + str(probNotCancerLF * dictionary['xray']['false'])
                        print "x~cs~p: " + str(probNotCancerHT * dictionary['xray']['false'])
                        print "x~c~s~p: " + str(probNotCancerHF * dictionary['xray']['false'])
                        print "~xcsp: " + str(probCancerLT * (1-dictionary['xray']['true']))
                        print "~xc~sp: " + str(probCancerLF * (1-dictionary['xray']['true']))
                        print "~xcs~p: " + str(probCancerHT * (1-dictionary['xray']['true']))
                        print "~xc~s~p: " + str(probCancerHF * (1-dictionary['xray']['true']))
                        print "~x~csp: " + str(probNotCancerLT * (1-dictionary['xray']['false']))
                        print "~x~c~sp: " + str(probNotCancerLF * (1-dictionary['xray']['false']))
                        print "~x~cs~p: " + str(probNotCancerHT * (1-dictionary['xray']['false']))
                        print "~x~c~s~p: " + str(probNotCancerHF * (1-dictionary['xray']['false']))	
			return

	if (cancer == "All" and smoker == "All" and pollution == "All"):
		calcConditional("c", "sp", dictionary)
		calcConditional("c", "~sp", dictionary)
		calcConditional("c", "s~p", dictionary)
		calcConditional("c", "~s~p", dictionary)
		calcConditional("~c", "sp", dictionary)
                calcConditional("~c", "~sp", dictionary)
                calcConditional("~c", "s~p", dictionary)
                calcConditional("~c", "~s~p", dictionary)
		return

        if (xray == 'All' and dyspnoea == 'All' and cancer == 'All'):
                probCancer = (dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['cancer']['HF'] * dictionary['pollution']['high'] * dictionary['smoker']['false']) + (dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false'])
                probNotCancer = (1- probCancer)
		print "cdx: " + str(probCancer * dictionary['dyspnoea']['true']*dictionary['xray']['true'])
		print "c~dx: " + str(probCancer * (1-dictionary['dyspnoea']['true'])*dictionary['xray']['true'])
		print "cd~x: " + str(probCancer * dictionary['dyspnoea']['true']*(1-dictionary['xray']['true']))
		print "c~d~x: " + str(probCancer * (1-dictionary['dyspnoea']['true'])*(1-dictionary['xray']['true']))
		print "~cdx: " + str(probNotCancer * dictionary['dyspnoea']['false']*dictionary['xray']['false'])
                print "~c~dx: " + str(probNotCancer * (1-dictionary['dyspnoea']['false'])*dictionary['xray']['false'])
                print "~cd~x: " + str(probNotCancer * dictionary['dyspnoea']['false']*(1-dictionary['xray']['false']))
                print "~c~d~x: " + str(probNotCancer * (1-dictionary['dyspnoea']['false'])*(1-dictionary['xray']['false']))
		return

	if (dyspnoea == 'All' and cancer == 'All'):
		calcConditional("d", "c", dictionary)
		calcConditional("d", "~c", dictionary)
		calcConditional("~d", "c", dictionary)
		calcConditional("~d", "~c", dictionary)
		return

	if (xray == 'All' and cancer == 'All'):
                calcConditional("x", "c", dictionary)
                calcConditional("x", "~c", dictionary)
                calcConditional("~x", "c", dictionary)
                calcConditional("~x", "~c", dictionary)
		return
	
	if (cancer == True and smoker == True and pollution == True):
		calcConditional("c", "sp", dictionary)
		return

	if (cancer == True and smoker == False and pollution == True):
                calcConditional("c", "~sp", dictionary)
		return

	if (cancer == True and smoker == True and pollution == False):
                calcConditional("c", "s~p", dictionary)
		return

	if (cancer == True and smoker == False and pollution == False):
                calcConditional("c", "~s~p", dictionary)
		return

	if (cancer == False and smoker == True and pollution == True):
                calcConditional("~c", "sp", dictionary)
		return

        if (cancer == False and smoker == False and pollution == True):
                calcConditional("~c", "~sp", dictionary)
		return

        if (cancer == False and smoker == True and pollution == False):
                calcConditional("~c", "s~p", dictionary)
		return

        if (cancer == False and smoker == False and pollution == False):
                calcConditional("~c", "~s~p", dictionary)
		return

	if (cancer == "All" and smoker == True and pollution == True):
                calcConditional("c", "sp", dictionary)
		calcConditional("~c", "sp", dictionary)
		return

        if (cancer == "All"  and smoker == False and pollution == True):
                calcConditional("c", "~sp", dictionary)
		calcConditional("~c", "sp", dictionary)
		return

        if (cancer == "All" and smoker == True and pollution == False):
                calcConditional("c", "s~p", dictionary)
		calcConditional("~c", "s~p", dictionary)
		return

        if (cancer == "All"  and smoker == False and pollution == False):
                calcConditional("c", "~s~p", dictionary)
		calcConditional("~c", "~s~p", dictionary)
		return

	if (smoker == 'All' and pollution == 'All'):
		print "ps: " + str(dictionary['smoker']['true'] * dictionary['pollution']['low'])
		print "~ps: " + str(dictionary['smoker']['true'] * dictionary['pollution']['high'])
		print "p~s: " + str(dictionary['smoker']['false'] * dictionary['pollution']['low'])
		print "~p~s: " + str(dictionary['smoker']['false'] * dictionary['pollution']['high'])
		return
	
	if (smoker == True and pollution == True):
		print "ps: " + str(dictionary['smoker']['true'] * dictionary['pollution']['low'])
		return

	if (smoker == True and pollution == False):
		print "~ps: " + str(dictionary['smoker']['true'] * dictionary['pollution']['high'])
		return

	if (smoker == False and pollution == True):
		print "p~s: " + str(dictionary['smoker']['false'] * dictionary['pollution']['low'])
		return

	if (smoker == False and pollution == False):
		print "~p~s: " + str(dictionary['smoker']['false'] * dictionary['pollution']['high'])
		return		

def calcConditional(calcVars, given, dictionary):
	dyspnoea = None
        xray = None
        cancer = None
        smoker = None
        pollution = None
	if "D" in calcVars:
                dyspnoea = "All"
        if "~d" in calcVars:
                dyspnoea = False
        elif "d" in calcVars:
                dyspnoea = True
        if "X" in calcVars:
                xray = "All"
        if "~x" in calcVars:
                xray = False
        elif "x" in calcVars:
                xray = True
        if "C" in calcVars:
                cancer = "All"
        if "~c" in calcVars:
                cancer = False
        elif "c" in calcVars:
                cancer = True
        if "P" in calcVars:
                pollution = "All"
        if "~p" in calcVars:
                pollution = False
        elif "p" in calcVars:
                pollution = True
        if "S" in calcVars:
                smoker = "All"
        if "~s" in calcVars:
                smoker = False
        elif "s" in calcVars:
                smoker = True

	givenDyspnoea = None
        givenXray = None
        givenCancer = None
        givenSmoker = None
        givenPollution = None
        if "D" in given:
                givenDyspnoea = "All"
        if "~d" in given:
                givenDyspnoea = False
        elif "d" in given:
                givenDyspnoea = True
        if "X" in given:
                givenXray = "All"
        if "~x" in given:
                givenXray  = False
        elif "x" in given:
                givenXray = True
        if "C" in given:
                givenCancer = "All"
        if "~c" in given:
                givenCancer = False
        elif "c" in given:
                givenCancer = True
        if "P" in given:
                givenPollution = "All"
        if "~p" in given:
                givenPollution = False
        elif "p" in given:
                givenPollution = True
        if "S" in given:
                givenSmoker = "All"
        if "~s" in given:
                givenSmoker = False
        elif "s" in given:
                givenSmoker = True
	
	#probability of pollution given cancer and smoking
	if ( (pollution == True or pollution == False) and ( (givenSmoker == True) and (givenCancer == True or givenCancer == False) ) ):
		if (givenCancer):
               		probPollutionLow = dictionary['pollution']['low'] * dictionary['smoker']['true'] * dictionary['cancer']['LT']
                	probCancer = probPollutionLow + (dictionary['pollution']['high'] * dictionary['smoker']['true'] * dictionary['cancer']['HT'])
                	if (pollution):
                        	print "The Probability of -gp|cs is: " + str(probPollutionLow/probCancer)
                	else:
                        	print "The Probability of -g~p|cs is: " + str(1-(probPollutionLow/probCancer))
			return
		else:
			probPollutionLow = dictionary['pollution']['low'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['LT'])
                        probCancer = probPollutionLow + (dictionary['pollution']['high'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['HT']))
                        if (pollution):
                                print "The Probability of -gp|~cs is: " + str(probPollutionLow/probCancer)
                        else:
                                print "The Probability of -g~p|~cs is: " + str(1-(probPollutionLow/probCancer))
                        return
		
	#the eight probailities of cancer
	if ((cancer or cancer == False) and ((givenPollution == True or givenPollution == False) and (givenSmoker == True or givenSmoker == False))):
		if (cancer):
			if (givenPollution and givenSmoker):
				probCancer = (dictionary['pollution']['low'] * dictionary['smoker']['true'] * dictionary['cancer']['LT'])
				print "The Probability of -gc|ps is: " + str(probCancer)
			elif (givenPollution and givenSmoker == False):
				probCancer = dictionary['pollution']['low'] * dictionary['smoker']['false'] * dictionary['cancer']['LF']
				print "The Probability of -gc|p~s is: " + str(probCancer)
			elif (givenPollution == False and givenSmoker):
				probCancer = dictionary['pollution']['high'] * dictionary['smoker']['true'] * dictionary['cancer']['HT']
				print "The Probability of -gc|~ps is: " + str(probCancer)
			else:
				probCancer = dictionary['pollution']['high'] * dictionary['smoker']['false'] * dictionary['cancer']['HF'] 
				print "The Probability of -gc|~p~s is: " + str(probCancer)
		else:
			if (givenPollution and givenSmoker):
                                probCancer = dictionary['pollution']['low'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['LT'])
                                print "The Probability of -g~c|ps is: " + str(probCancer)
                        elif (givenPollution and givenSmoker == False):
                                probCancer = dictionary['pollution']['low'] * dictionary['smoker']['false'] * (1-dictionary['cancer']['LF'])
                                print "The Probability of -g~c|p~s is: " + str(probCancer)
                        elif (givenPollution == False and givenSmoker):
                                probCancer = dictionary['pollution']['high'] * dictionary['smoker']['true'] * (1-dictionary['cancer']['HT']) 
                                print "The Probability of -g~c|~ps is: " + str(probCancer)
                        else:  
                                probCancer = dictionary['pollution']['high'] * dictionary['smoker']['false'] * (1-dictionary['cancer']['HF'])
                                print "The Probability of -g~c|~p~s is: " + str(probCancer)
		return
	
	#smoker given dyspnoea
	if ( ((smoker == True or smoker == False) or (pollution == True or pollution == False)) and (givenDyspnoea == True or givenDyspnoea == False) ):
		probSmokerTrue = (dictionary['dyspnoea']['true'] * dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['dyspnoea']['true'] * dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['dyspnoea']['false'] * (1-dictionary['cancer']['HT']) * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['dyspnoea']['false'] * (1-dictionary['cancer']['LT']) * dictionary['pollution']['low'] * dictionary['smoker']['true'])
		probSmokerAll = (dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + ( dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + ((1-dictionary['cancer']['HT']) * dictionary['pollution']['high'] * dictionary['smoker']['true']) + ((1-dictionary['cancer']['LT']) * dictionary['pollution']['low'] * dictionary['smoker']['true'])
		probCancer = (dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['cancer']['HF'] * dictionary['pollution']['high'] * dictionary['smoker']['false']) + (dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false'])
		smokerGivenDyspnoea = ((probSmokerTrue/probSmokerAll) * dictionary['smoker']['true'])/((dictionary['dyspnoea']['true']*probCancer) + (dictionary['dyspnoea']['false']*(1-probCancer))) 
		probPollutionTrue = (dictionary['dyspnoea']['true'] * dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['dyspnoea']['true'] * dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false']) + (dictionary['dyspnoea']['false'] * (1-dictionary['cancer']['LT']) * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['dyspnoea']['false'] * (1-dictionary['cancer']['LF']) * dictionary['pollution']['low'] * dictionary['smoker']['false'])
                probPollutionAll = (dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + ( dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false']) + ((1-dictionary['cancer']['LT']) * dictionary['pollution']['low'] * dictionary['smoker']['true']) + ((1-dictionary['cancer']['LF']) * dictionary['pollution']['low'] * dictionary['smoker']['false'])
                pollutionGivenDyspnoea = ((probPollutionTrue/probPollutionAll) * dictionary['pollution']['low'])/((dictionary['dyspnoea']['true']*probCancer) + (dictionary['dyspnoea']['false']*(1-probCancer)))
		if(smoker or smoker == False):
			if (smoker):
				print "The probability of -gs|d is: " + str(smokerGivenDyspnoea)
			else:
				print "The Probability of -g~s|d is: " + str(1-(smokerGivenDyspnoea))
			return
		elif(pollution or pollution == False):
			if (pollution):
        	                print "The probability of -gp|d is: " + str(pollutionGivenDyspnoea)
	                else:
                	        print "The Probability of -g~p|d is: " + str(1-(pollutionGivenDyspnoea))
			return
		elif(cancer or cancer == False):
			if(cancer):
				print "The Probability of -gc|d is: " + str(cancerGivenDyspnoea)
			else:
				print "The Probability of -g~c|d is: " + str(1-cancerGivenDyspnoea)

	#probabilities given smoking and dyspnoea
        if ( ((cancer == True or cancer == False) or (xray == True or xray == False)) and (givenSmoker == True and givenDyspnoea == True ) ):
		calcCancerGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT'])
                calcAllGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'])
                calcProbCancer = calcCancerGivenSmoker/calcAllGivenSmoker
		calcProbCancerGivenD = (dictionary['dyspnoea']['true']*calcProbCancer)/((dictionary['dyspnoea']['true']*calcProbCancer)+(dictionary['dyspnoea']['false']*(1-calcProbCancer)))
		calcProbXrayGivenD = (dictionary['xray']['true'] * calcProbCancerGivenD) + (dictionary['xray']['false'] * (1-calcProbCancerGivenD))
		if (cancer == True or cancer == False):
			if (cancer):
				print "the probability of -gc/sd is: " + str(calcProbCancerGivenD)
			else: 
				print "the probability of -g~c/sd is: " + str(1-calcProbCancerGivenD)		
			return

		if (xray == True or xray == False):
			if (xray):
				print "The probability of -gx/sd is: " + str(calcProbXrayGivenD)
			else:
				print "The probability of -g~x/sd is: " + str(1-calcProbXrayGivenD)
			return
		
	#probability of cancer given dyspnoea
	if (((cancer == True or cancer == False) or (xray == True or xray == False)) and (givenDyspnoea == True or givenDyspnoea == False)):
		probCancer = (dictionary['cancer']['HT'] * dictionary['pollution']['high'] * dictionary['smoker']['true']) + (dictionary['cancer']['HF'] * dictionary['pollution']['high'] * dictionary['smoker']['false']) + (dictionary['cancer']['LT'] * dictionary['pollution']['low'] * dictionary['smoker']['true']) + (dictionary['cancer']['LF'] * dictionary['pollution']['low'] * dictionary['smoker']['false'])
		margDyspnoea = (probCancer * dictionary['dyspnoea']['true']) + ( (1-probCancer) * dictionary['dyspnoea']['false'])
		probCancerGivenDyspnoea = (dictionary['dyspnoea']['true'] * probCancer)/margDyspnoea
		margXRay = (probCancerGivenDyspnoea * dictionary['xray']['true']) + ((1-probCancerGivenDyspnoea) * dictionary['xray']['false'])
		if (cancer == True or cancer == False):
			if (cancer):
				print "the probability of -gc|d is: " + str(probCancerGivenDyspnoea)
			else:
				print "The probability of -g~c|d id: " + str(1-probCancerGivenDyspnoea)
			return
		else:
			if(xray):
				print "The probability of -gx|d is: " + str(margXRay)
			else:
				print "The probability of -g~x|d is: " + str(1-margXRay)
		
		 	

	# -gc|s and -g~c|s 
	if ( (cancer or cancer == False) and givenSmoker == True):
		calcCancerGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT'])
		calcAllGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['true'] * dictionary['pollution']['low']) 
		calcProbCancer = calcCancerGivenSmoker/calcAllGivenSmoker
		if(cancer):
			print "Probability of c|s is: " + str(calcProbCancer)
  		else: 
			print "Probability of ~c|s is: " + str(1-calcProbCancer)
		return

	# -gc|p and -g~c|p 
	if ( (cancer or cancer == False) and givenPollution == True):
		calcCancerGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                calcAllGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                calcProbCancer = calcCancerGivenPollution/calcAllGivenPollution
                if(cancer):
                        print "Probability of c|s is: " + str(calcProbCancer)
                else:
                        print "Probability of ~c|s is: " + str(1-calcProbCancer)
		return

	# -gc|~s and -g~c|~s
	if ( (cancer or cancer == False) and givenSmoker == False ):
		calcCancerGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                calcAllGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                calcProbCancer = calcCancerGivenNotSmoker/calcAllGivenNotSmoker
                if(cancer):
                        print "Probability of c|~s is: " + str(calcProbCancer)
                else:
                        print "Probability of ~c|~s is: " + str(1-calcProbCancer)
                return

	# -gc|~p and -g~c|~p
        if ( (cancer or cancer == False) and givenPollution == False ):
                calcCancerGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF'])
                calcAllGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'])
                calcProbCancer = calcCancerGivenNotPollution/calcAllGivenNotPollution
                if(cancer):
                        print "Probability of c|~s is: " + str(calcProbCancer)
                else:
                        print "Probability of ~c|~s is: " + str(1-calcProbCancer)
                return
	
	#dyspnoea Given cancer
	if ( (dyspnoea or dyspnoea == False) and (givenCancer == True or givenCancer == False) ):
		if (givenCancer):
			if (dyspnoea):
				print "The Probability of -gd|c: " + str(dictionary['dyspnoea']['true'])
			else:
				print "The Probability of -g~d|c: " + str(1-dictionary['dyspnoea']['true'])
			return
		else:
			if (dyspnoea):
                                print "The Probability of -gd|~c: " + str(dictionary['dyspnoea']['false'])
                        else:
                                print "The Probability of -g~d|~c: " + str(1-dictionary['dyspnoea']['false'])
			return

	#dyspnoea Given smoker
        if ( (dyspnoea or dyspnoea == False) and (givenSmoker == True or givenSmoker == False) ):
                if (givenSmoker):
			calcCancerGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT'])
	                calcAllGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'])
        	        calcProbCancer = calcCancerGivenSmoker/calcAllGivenSmoker
                        if (dyspnoea):				
                                print "The Probability of -gd|s: " + str((dictionary['dyspnoea']['true'] * calcProbCancer) + (dictionary['dyspnoea']['false'] * (1 - calcProbCancer)) )
                        else:
                                print "The Probability of -g~d|s: " + str(((1-dictionary['dyspnoea']['true']) * calcProbCancer) + ((1-dictionary['dyspnoea']['false']) * (1 - calcProbCancer)))
                else:
			calcCancerGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                	calcAllGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                	calcProbCancer = calcCancerGivenNotSmoker/calcAllGivenNotSmoker
                        if (dyspnoea):
                                print "The Probability of -gd|~s: " + str((dictionary['dyspnoea']['true'] * calcProbCancer) + (dictionary['dyspnoea']['false'] * (1 - calcProbCancer)))
                        else:
                                print "The Probability of -g~d|~s: " + str(((1-dictionary['dyspnoea']['true']) * calcProbCancer) + ((1-dictionary['dyspnoea']['false']) * (1 - calcProbCancer)))
		return

	#dyspnoea Given Pollution
        if ( (dyspnoea or dyspnoea == False) and (givenPollution == True or givenPollution == False) ):
                if (givenPollution):
			calcCancerGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                	calcAllGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                	calcProbCancer = calcCancerGivenPollution/calcAllGivenPollution
                        if (dyspnoea):
                                print "The Probability of -gd|p: " + str((dictionary['dyspnoea']['true'] * calcProbCancer) + (dictionary['dyspnoea']['false'] * (1 - calcProbCancer)) )
                        else:
                                print "The Probability of -g~d|p: " + str(((1-dictionary['dyspnoea']['true']) * calcProbCancer) + ((1-dictionary['dyspnoea']['false']) * (1 - calcProbCancer)))
                else:
			calcCancerGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF'])
 	               	calcAllGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'])
        	       	calcProbCancer = calcCancerGivenNotPollution/calcAllGivenNotPollution
                        if (dyspnoea):
                                print "The Probability of -gd|~p: " + str((dictionary['dyspnoea']['true'] * calcProbCancer) + (dictionary['dyspnoea']['false'] * (1 - calcProbCancer)))
                        else:
                                print "The Probability of -g~d|~p: " + str(((1-dictionary['dyspnoea']['true']) * calcProbCancer) + ((1-dictionary['dyspnoea']['false']) * (1 - calcProbCancer)))
		return


	#xray Given cancer
	if ( (xray or xray == False) and (givenCancer == True or givenCancer == False) ):
                if (givenCancer):
                        if (xray):
                                print "The Probability of -gx|c: " + str(dictionary['xray']['true'])
                        else:
                                print "The Probability of -g~x|c: " + str(1-dictionary['xray']['true'])
                        return
                else:
                        if (xray):
                                print "The Probability of -gx|~c: " + str(dictionary['xray']['false'])
                        else:
                                print "The Probability of -g~x|~c: " + str(1-dictionary['xray']['false'])
                        return
	
	#xray Given smoker
        if ( (xray or xray == False) and (givenSmoker == True or givenSmoker == False) ):
                if (givenSmoker):
                        calcCancerGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT'])
                        calcAllGivenSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'])
                        calcProbCancer = calcCancerGivenSmoker/calcAllGivenSmoker
                        if (xray):
                                print "The Probability of -gx|s: " + str((dictionary['xray']['true'] * calcProbCancer) + (dictionary['xray']['false'] * (1 - calcProbCancer)) )
                        else:
                                print "The Probability of -g~x|s: " + str(((1-dictionary['xray']['true']) * calcProbCancer) + ((1-dictionary['xray']['false']) * (1 - calcProbCancer)))
                else:
                        calcCancerGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                        calcAllGivenNotSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                        calcProbCancer = calcCancerGivenNotSmoker/calcAllGivenNotSmoker
                        if (xray):
                                print "The Probability of -gx|~s: " + str((dictionary['xray']['true'] * calcProbCancer) + (dictionary['xray']['false'] * (1 - calcProbCancer)))
                        else:
                                print "The Probability of -g~x|~s: " + str(((1-dictionary['xray']['true']) * calcProbCancer) + ((1-dictionary['xray']['false']) * (1 - calcProbCancer)))
                return

        #xray Given Pollution
        if ( (xray or xray == False) and (givenPollution == True or givenPollution == False) ):
                if (givenPollution):
                        calcCancerGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                        calcAllGivenPollution = (dictionary['smoker']['true'] * dictionary['pollution']['low']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'])
                        calcProbCancer = calcCancerGivenPollution/calcAllGivenPollution
                        if (xray):
                                print "The Probability of -gx|p: " + str((dictionary['xray']['true'] * calcProbCancer) + (dictionary['xray']['false'] * (1 - calcProbCancer)) )
                        else:
                                print "The Probability of -g~x|p: " + str(((1-dictionary['xray']['true']) * calcProbCancer) + ((1-dictionary['xray']['false']) * (1 - calcProbCancer)))
                else:
                        calcCancerGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF'])
                        calcAllGivenNotPollution = (dictionary['smoker']['true'] * dictionary['pollution']['high']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'])
                        calcProbCancer = calcCancerGivenNotPollution/calcAllGivenNotPollution
			if (xray):
                                print "The Probability of -gx|~p: " + str((dictionary['xray']['true'] * calcProbCancer) + (dictionary['xray']['false'] * (1 - calcProbCancer)))
                        else:
                                print "The Probability of -g~x|~p: " + str(((1-dictionary['xray']['true']) * calcProbCancer) + ((1-dictionary['xray']['false']) * (1 - calcProbCancer)))
                return

	
	#smoking or not smoking given cancer or not cancer
	if ( (smoker == True or smoker == False) and (givenCancer == True or givenCancer == False) ):
		if (givenCancer):
			oddsOfCancerSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT'])
		   	oddsOfCancerNonSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
			totalOddsOfCancer = oddsOfCancerSmoker + oddsOfCancerNonSmoker
			if (smoker):
				print "The Probability of -gs|c: " + str(oddsOfCancerSmoker/totalOddsOfCancer)
			else: 
				print "The Probability of -g~s|c: " + str(oddsOfCancerNonSmoker/totalOddsOfCancer)
			return
		else:
			oddsOfNotCancerSmoker = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * (1-dictionary['cancer']['HT'])) + (dictionary['smoker']['true'] * dictionary['pollution']['low'] * (1-dictionary['cancer']['LT']))
                        oddsOfNotCancerNonSmoker = (dictionary['smoker']['false'] * dictionary['pollution']['high'] * (1-dictionary['cancer']['HF'])) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * (1-dictionary['cancer']['LF']))
                        totalOddsOfNotCancer = oddsOfNotCancerSmoker + oddsOfNotCancerNonSmoker
			if (smoker):
				print "The Probability of -gs|~c: " + str(oddsOfNotCancerSmoker/totalOddsOfNotCancer)
			else:
				print "The Probability of -g~s|~c: " + str(oddsOfNotCancerNonSmoker/totalOddsOfNotCancer)
			return
	
	
	#pollution or not pollution given cancer or not cancer
        if ( (pollution == True or pollution == False) and (givenCancer == True or givenCancer == False) ):
                if (givenCancer):
                        oddsOfCancerPollutionHigh = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * dictionary['cancer']['HT']) + (dictionary['smoker']['false'] * dictionary['pollution']['high'] * dictionary['cancer']['HF'])
                        oddsOfCancerPollutionLow = (dictionary['smoker']['true'] * dictionary['pollution']['low'] * dictionary['cancer']['LT']) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * dictionary['cancer']['LF'])
                        totalOddsOfCancer = oddsOfCancerPollutionHigh + oddsOfCancerPollutionLow
                        if (pollution):
                                print "The Probability of -gp|c: " + str(oddsOfCancerPollutionLow/totalOddsOfCancer)
                        else:
                                print "The Probability of -g~p|c: " + str(oddsOfCancerPollutionHigh/totalOddsOfCancer)
                        return
                else:
			oddsOfNotCancerPollutionHigh = (dictionary['smoker']['true'] * dictionary['pollution']['high'] * (1-dictionary['cancer']['HT'])) + (dictionary['smoker']['false'] * dictionary['pollution']['high'] * (1-dictionary['cancer']['HF']))
                        oddsOfNotCancerPollutionLow = (dictionary['smoker']['true'] * dictionary['pollution']['low'] * (1-dictionary['cancer']['LT'])) + (dictionary['smoker']['false'] * dictionary['pollution']['low'] * (1-dictionary['cancer']['LF']))
                        totalOddsOfNotCancer = oddsOfNotCancerPollutionHigh + oddsOfNotCancerPollutionLow
                        if (pollution):
                                print "The Probability of -gp|~c: " + str(oddsOfNotCancerPollutionLow/totalOddsOfNotCancer)
                        else:
                                print "The Probability of -g~p|~c: " + str(oddsOfNotCancerPollutionHigh/totalOddsOfNotCancer)
			return

	
        #cases for smoker given pollution
	if ( (smoker or smoker == False) and (givenPollution or givenPollution == False) ):
		if (smoker):
			print "The probability of s|p or s|~p: " + str(dictionary['smoker']['true'])
		else:
			print "The probability of ~s|p or ~s|~p: " + str(dictionary['smoker']['false'])
		return
	
	#cases for pollution given smoker
	if( (pollution or  pollution == False) and (givenSmoker or givenSmoker == False) ):
		if (pollution):
			print "The probability of p|s or p|~s: " + str(dictionary['pollution']['low'])
		else:
			print "The Probability of ~p|s or ~p|~s: " + str(dictionary['pollution']['high'])
		return

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

    #initialze pollution dictionary
    bayesDictionary = initDictionary()      

    #check input flags, return what is needed
    for o, a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			#print a[0]
			#print a[1:]
			newVal = float(a[2:])
			if (a[1] != '='):
				print 'Invalid syntax --> Ex. -pP=0.80 will set probability of low pollution to 0.80'
			if (a[0] == 'S'):
				bayesDictionary['smoker']['true'] = newVal
				bayesDictionary['smoker']['false'] = 1 - newVal
			elif (a[0] == 'P'):
				bayesDictionary['pollution']['low'] = newVal
				bayesDictionary['pollution']['high'] = 1 - newVal
			else:
				print 'Invalid syntax --> Ex. -pP=0.80 will set probability of low pollution to 0.80'

		#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			#print "flag", o
			#print "args", a
			#print type(a)
			if (a == 'D'):
				name = 'dyspnoea'
			elif (a == 'P'):
				name = 'pollution'
			elif (a == 'S'):
				name = 'smoker'
			elif (a == 'C'):
				name = 'cancer'
			elif (a == 'X'):
				name = 'xray'				
			calcMarginal(name, bayesDictionary)

		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			p = a.find("/")
			print a[:p]
			print a[p+1:]
			calcConditional(a[:p], a[p+1:], bayesDictionary)
			
		elif o in ("-j"):
			print "flag", o
			print "args", a
			calcJoint(a, bayesDictionary)
		else:
			assert False, "unhandled option"
		
    # ...

if __name__ == "__main__":
    main()
   
