# Funciton checks for tritones.  Returns an error message to
# be printed, if any.
from music21 import *

intA = interval.Interval('A4');
intB = interval.Interval('D5');
intC = interval.Interval('A-4');
intD = interval.Interval('D-5');
intervalList = [intA, intB, intC, intD];

def failedSopranoTritone(firstChord, secondChord):
    if interval.Interval(firstChord[0], secondChord[0]) in intervalList:
        return True;
    else:
        return False;


def failedAltoTritone(firstChord, secondChord):
    if interval.Interval(firstChord[1], secondChord[1]) in intervalList:
        return True;
    else:
        return False;


def failedTenorTritone(firstChord, secondChord):
    if interval.Interval(firstChord[2], secondChord[2]) in intervalList:
        return True;
    else:
        return False;


def failedBassTritone(firstChord, secondChord):
    if interval.Interval(firstChord[3], secondChord[3]) in intervalList:
        return True;
    else:
        return False;

def checkTritones(slices):
    # output is a list of strings which give error messages
    output = [];

    # iterate until second to last chord.  Check chord with subsequent chord
    for count in range(0,len(slices) - 2):
        firstChord = slices[count].getChord();
        secondChord = slices[count + 1].getChord();
        if len(firstChord) == 4 and len(secondChord) == 4:
            if (failedSopranoTritone(firstChord, secondChord)):
                output.append('Soprano makes tritone in measure ' + str(firstChord[0].measureNumber) + " beat " + str(firstChord[0].beat));
            if (failedAltoTritone(firstChord, secondChord)):
                output.append('Alto makes tritone in measure ' + str(firstChord[1].measureNumber) + " beat " + str(firstChord[1].beat));
            if (failedTenorTritone(firstChord, secondChord)):
                output.append('Tenor makes tritone in measure ' + str(firstChord[2].measureNumber) + " beat " + str(firstChord[2].beat));
            if (failedBassTritone(firstChord, secondChord)):
                output.append('Bass makes tritone in measure ' + str(firstChord[3].measureNumber) + " beat " + str(firstChord[3].beat));

        
       
    return output; 
