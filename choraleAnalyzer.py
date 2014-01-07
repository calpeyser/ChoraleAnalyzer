import os
import sys
from music21 import *
from checkParallels import *
from checkZeroOrder import *
from checkVoiceLeading import *
from checkHarmony import *
from utilities import *
import subprocess, glob

# there must be at least one command line argument
if len(sys.argv) < 2:
    print "Required input: musicXML file."
    exit();

print("--------------------Chorale Analyzer-----------------");

# list for error storage
assignList();

# parse and store MusicXML file
chorale = converter.parse(sys.argv[1]);

# parse and store Roman Numeral Analysis
harmonyFlag = False;
if len(sys.argv) > 2:
    rntext = converter.parse(sys.argv[2]);
    harmonyFlag = True; 

parallelsFlag = True;
if len(sys.argv) == 4:
    parallelsFlag = False;

if parallelsFlag:
    checkParallels(chorale)

checkZeroOrder(chorale);
checkVoiceLeading(chorale);
if (harmonyFlag == True): 
    checkHarmony(chorale, rntext);

# read output
errorTracker = errorTracker();
# utilities.py has already taken care of writing to 'errors'.  
# now we read
outputLines = retrieveList();
for line in outputLines:
    errorTracker.processError(line);

# Count measures
chordification = chorale.chordify();
measureCounter = 0;
for i in range(len(chordification)):
    if str(type(chordification[i])) == "<class 'music21.stream.Measure'>":
        measureCounter += 1;

# compute and print Bachness
print("Bachness Score: " + str(errorTracker.computeBachness(measureCounter)));

print("--------------------Analysis Complete----------------");


