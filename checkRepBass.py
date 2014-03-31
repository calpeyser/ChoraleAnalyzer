# Funciton checks for repeated bass notes.  Returns an error message to
# be printed, if any.
from music21 import *

def failedRepBass(firstNote, secondNote):
    if (firstNote == secondNote):
        return True;
    else:
        return False;

def checkRepBass(bass):
    # output is a list of strings which give error messages
    output = [];

    # pitches is a list of pitches that occur in the bass part
    pitches = bass.pitches;

    # iterate until second to last chord.  Check chord with subsequent chord
    for count in range(0,len(pitches) - 2):
        firstNote = pitches[count];
        secondNote = pitches[count+1];
        if (failedRepBass(firstNote, secondNote)):
            output.append('Bass note repeated. Note number: ' + 
                          str(count+1));
    
    return output;
         
