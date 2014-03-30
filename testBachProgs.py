import sys
import os
import pickle # for packing up the dict
from utilities import *
import subprocess, glob
from choraleAnalyzer import *

# take a list of progTrackers with possible duplicates, and return a list of 
# distinct progTrackers where errors are summed.  In these new progTrackers,
# only the progString and error counts are relevant
def combineProgs(progs):
    outProgs = [];  # This list contains all distinct progTrackers, with summed errors
    for newProg in progs:  
        alreadyHaveIt = False; # is this prog already in outProgs?
        for i in range(len(outProgs)):  # if we already have this prog, add them;
            if outProgs[i].equals(newProg):
                outProgs[i] = outProgs[i].addProg(newProg);
                alreadyHaveIt = True;
                break;
        if not alreadyHaveIt:
            outProgs.append(newProg);
    return outProgs;


# extract unique progressionTrakckers from any number of chorales
def getProgs(numberOfChorales):

    if len(sys.argv) < 2:
        print "Usage: python testBachProgs.py [number of chorales]";
        exit();
    pFlag = True;
    if len(sys.argv) == 3:
        pFlag = False;

    numberOfChorales = int(numberOfChorales);
    output = [];

    errorTrackers = [];
    for i in range(numberOfChorales):
        num = i + 1;
        if num < 10:
            txt = "00" + str(num);
        elif num < 100:
            txt = "0" + str(num);
        elif num >= 100:
            txt = str(num);
        c = "Tymo/XMLChorales/riemenschneider" + txt + ".xml";
        b = "Tymo/BachChorales/riemenschneider" + txt + ".txt";
        
        print "Analyzing riemenschneider" + txt;

        errorTrackers.append(ChoraleAnalyzer(c,b,True,True));

    allProgs = [];
    for errTracker in errorTrackers:
        allProgs += errTracker.progTrackers;
    return combineProgs(allProgs);

# take a set of unique progressionTrackers (the output of getProgs(), for example),
# and create a Python dictionary, mapping progression string to list of error values.
def createProgDict(uniqueProgs):
    typesOfErrors = 17;
    out = {};
    for prog in uniqueProgs:
        for errorIndex in range(typesOfErrors):
            errorList = [prog.P1, prog.P5, prog.P8, prog.bassRange, prog.tenorRange, prog.altoRange, prog.sopRange, prog.altSopInt, prog.tenAltInt, prog.BTVC, prog.TAVC, prog.ASVC, prog.tritone, prog.repBass];
            out[prog.prog] = errorList;
    return out;

def analyzeToPickle(numberOfChorales):
    progList = getProgs(numberOfChorales);
    progDict = createProgDict(progList);
    f = open("errorsByProg.pkl", "w");
    pickle.dump(progDict, f)

analyzeToPickle(int(sys.argv[1]));



