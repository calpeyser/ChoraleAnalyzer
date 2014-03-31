# Anlaysis module for a dictionary of unique progs to error counts,
# as created by the testBachProgs module

import pickle
import copy, sys

# total errors in Bach (371 Chorales).  # NOTE - UPDATE TO ALL 371.  THIS IS ONLY 70
# Errors are: P1, P5, P8, bassRange, tenorRange, altoRange, sopRange, altSopInt, tenAltInt,
# BTVC, TAVC, ASVC, tritone, repBass
totalErrors = [7, 1536, 377, 142, 14, 1, 0, 26, 658, 63, 130, 34, 79, 330];
errorTypes = ["P1", "P5", "P8", "bassRange", "tenorRange", "altoRange", "sopRange", "altSopInt", "tenAltInt", "BTVC", "TAVC", "ASVC", "tritone", "repBass"];

# reads from file, depickles
def loadProgsDict():
	f = open("errorsByProg.pkl", "r");
	progsDict = pickle.load(f);
	return progsDict;

# print a string representation of the progressions dict
def printDict(realProgsDict):
	for key in realProgsDict:
		print key + " " + str(realProgsDict[key]);

# returns a dict that maps progressions to list of proportion of errors that occur in it, by type
def getProportionsDict(realProgsDict):
	progsDict = copy.deepcopy(realProgsDict);
	for key in progsDict:
		errorList = progsDict[key];
		for i in range(len(errorList)):
			if totalErrors[i] != 0:
				errorList[i] = float(errorList[i])/float(totalErrors[i]);
			else: errorList[i] = 0;
		progsDict[key] = errorList;
	return progsDict;

# returns a list of most common prog by error type, together with proportion
# optional argument: size of progs under consideration
def getWorstProgs(realProgsDict, size = None):
	propDict = getProportionsDict(realProgsDict);
	out = [];
	for i in range(len(totalErrors)):
		big = 0;
		prog = "";
		for key in propDict:
			if size:
				if len(key.split("->")) != size:
					continue;
			if propDict[key][i] > big:
				big = propDict[key][i];
				prog = key;
		out.append([prog, big]);
	return out;


# like getWorstProgs(), but prints results
def printWorstProgs(realProgsDict, size = None):
	progsDict = getProportionsDict(realProgsDict)
	worstProgs = getWorstProgs(progsDict, size);
	for i in range(len(worstProgs)):
		print errorTypes[i] + ": " + worstProgs[i][0] + " " + str(worstProgs[i][1]); 

progsDict = loadProgsDict();
#printDict(progsDict);
if len(sys.argv) == 1:
	printWorstProgs(progsDict);
else: printWorstProgs(progsDict, int(sys.argv[1]));



