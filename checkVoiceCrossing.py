# Verifies that there are no voice crossings
from music21 import *

def failedBassTenorCross(chord):
    if chord[3].pitch > chord[2].pitch:
        return True;
    else:
        return False;

def failedTenorAltoCross(chord):
    if chord[2].pitch > chord[1].pitch:
        return True;
    else:
        return False;

def failedAltoSopranoCross(chord):
    if chord[1].pitch > chord[0].pitch:
        return True;
    else:
        return False;

def checkVoiceCrossing(slices):
    # output is a list of strings which give error messages
    output = [];

    # iterate through list and check for errors
    if not slices:
        return output;

    for slice in slices:
        chord = slice.getChord();
        if len(chord) == 4:
            if (failedBassTenorCross(chord)):
                output.append('Bass/Tenor voice crossing in measure ' 
                              + str(chord[3].measureNumber) + " beat " + str(chord[3].beat));
            if (failedTenorAltoCross(chord)):
                output.append('Tenor/Alto voice crossing in measure '
                              + str(chord[2].measureNumber) + " beat " + str(chord[2].beat));
            if (failedAltoSopranoCross(chord)):
                output.append('Alto/Soprano voice crossing in measure '
                              + str(chord[1].measureNumber) + " beat " + str(chord[1].beat));

    return output;
