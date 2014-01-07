# Verifies that each part is inside of expected range

from music21 import *
from utilities import removeDuplicates

def failedSopranoRange(chord):
    if chord[0].pitch > pitch.Pitch('g5'):
        return True;
    elif chord[0].pitch < pitch.Pitch('c4'):
        return True;
    else:
        return False;

def failedAltoRange(chord):
    if chord[1].pitch > pitch.Pitch('d5'):
        return True;
    elif chord[1].pitch < pitch.Pitch('g3'):
        return True;
    else:
        return False;

def failedTenorRange(chord):
    if chord[2].pitch > pitch.Pitch('g4'):
        return True;
    elif chord[2].pitch < pitch.Pitch('c3'):
        return True;
    else:
        return False;

def failedBassRange(chord):
    if chord[3].pitch > pitch.Pitch('c4'):
        return True;
    elif chord[3].pitch < pitch.Pitch('f2'):
        return True;
    else:
        return False;


def checkRanges(slices):
    # output is a list of strings which give error messages
    output = [];

    # since VerticalSlice is not represented in a measure, use
    # bass note to determine measure
    for slice in slices:
        chord = slice.getChord();
        if (failedSopranoRange(chord)):
            output.append('Soprano out of range in measure ' + 
                          str(chord[3].measureNumber));
        if (failedAltoRange(chord)):
            output.append('Alto out of range in measure ' + 
                          str(chord[3].measureNumber));
        if (failedTenorRange(chord)):
            output.append('Tenor out of range in measure ' +
                          str(chord[3].measureNumber));
        if (failedBassRange(chord)):
            output.append('Bass out of range in measure ' +
                          str(chord[3].measureNumber));
        
    return removeDuplicates(output);
