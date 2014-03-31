# identifyPatterns.py 

# This module reads data from ALL_melodydegreesBACH.pkl residing in local directory
# This file is a pickle-formatted dictionary produced by sd.py in Dr. Tymozcko's code

from music21 import *
import pickle

# get the dictionary
f = open("ALL_melodydegreesBACH.pkl", "r");
melodyData = pickle.load(f);
f = open("ALL_progressionsBACH.pkl", "r");
progData = pickle.load(f);

for key in progData[0]:
	print str(key) + " Value: " + str(progData[0][key]); 