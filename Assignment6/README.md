#Intro To Artificial Intelligence Baye's Net

###Supported Flags and options

#####-g
Conditional Probability Flag
supported(p, s, c, x, d) or not these ex. ~p
example usage: -gc/s (probability of cancer given smoking)

#####-m
Marginal Probability Flag
supported (P, S, C, X, D)
example usage: -mP (marginal probability of pollution)

#####-p
Change Probability flag
changes smoking or pollutions probability
-pP=0.5 sets pollution = low to 0.5

#####-j
Joint Probability Flag
supported(p, s, c, x, d) or not these ex. ~p or all these ex. P
-jCSP (all probabilities for all combinations of cancer, smoking and pollution

#####Example Usage
python bayesNet.py -pP=0.5 -gc/p
