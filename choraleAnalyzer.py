import os
import sys
from music21 import *
from checkParallels import *
from checkZeroOrder import *
from checkVoiceLeading import *
from checkHarmony import *
from utilities import *
from gatherProgs import * 
import subprocess, glob

def ChoraleAnalyzer(XMLfile, ROMANfile, parallelsFlag = True, errFlag = False):
    out = [];
    out.append(("--------------------Chorale Analyzer-----------------"));
        
    # list for error storage
    assignList();

    # parse and store MusicXML file
    chorale = converter.parse(XMLfile);

    # parse and store Roman Numeral Analysis
#NOTE MAY WANT TO INCLUDE OPTION TO EXCLUDE HARMONY
    harmonyFlag = False;
    rntext = converter.parse(ROMANfile);
    harmonyFlag = True; 

    if parallelsFlag:
        for line in checkParallels(chorale):
            out.append(line);

    for line in checkZeroOrder(chorale):
        out.append(line);
    for line in checkVoiceLeading(chorale):
        out.append(line);
    for line in checkHarmony(chorale, rntext):
        out.append(line);

    # progression trackers
    progTrackers = gatherProgs(rntext);

    # read output
    tracker = errorTracker(progTrackers);
    # utilities.py has already taken care of writing to 'errors'.  
    # now we read
    outputLines = retrieveList();
    for line in outputLines:
        tracker.processError(line);

    # Count measures
    chordification = chorale.chordify();
    measureCounter = 0;
    for i in range(len(chordification)):
        if str(type(chordification[i])) == "<class 'music21.stream.Measure'>":
            measureCounter += 1;
        
    # compute and print Bachness
    out.append("Bachness Score: " + str(tracker.computeBachness(measureCounter)));

    out.append("--------------------Analysis Complete----------------");

    if errFlag == False:
        return out;
    else: return tracker;

