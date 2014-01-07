# Function checks for incomplete chords.  Returns an error message to be
# be printed, if any.
from music21 import *

def checkIncompleteChords(chorale):
    # output is a list of strings which give error messages
    output = [];

    # chords will be a list of all the chords in the chorale
    chords = chorale.chordify();
    
    # iterate through list, produce error message for each chord which is 
    # incomplete
    for chord in chords:
        if(not(chord.Chord.isTriad()|chord.Chord.isSeventh())):
                output.append('Illegal chord found!' +
                              '\n Measure Number: ' + str(chord.measureNumber) + 
                              '\n    Chord: ' + str(chord.fullName) +
                              '\n')
    return output;
            
