# Verifies that distance between parts is not too large

from music21 import *

# Distance between bass and soprano cannot be greater than 
# a 12th
#def failedTenorSopranoDistance(chord):
#    if interval.Interval(chord[3], chord[1]).cents > interval.Interval('P12').cents:
#        return True;
#    else:
#        return False;

# Distance between alto and soprano cannot be greater than an octave
def failedAltoSopranoDistance(chord):
    if interval.Interval(chord[1], chord[0]).cents > interval.Interval('P8').cents:
        return True;
    else:
        return False;


def failedTenorAltoDistance(chord):
    if interval.Interval(chord[2], chord[1]).cents > interval.Interval('P8').cents:
        return True;
    else:
        return False;


def checkCloseness(slices):
    # output is a list of strings which give error messages
    output = [];

    # since VerticalSlice is not represented in a measure, use
    # chord notes to determine measure
    for slice in slices:
        chord = slice.getChord();
 #       if (failedTenorSopranoDistance(chord)):
 #           output.append('Interval between tenor and soprano greater than a 12th in measure ' + str(chord[3].measureNumber));
        if (failedAltoSopranoDistance(chord)):
            output.append('Interval betweeen alto and soprano greater than an octave in measure ' + str(chord[1].measureNumber));
        if (failedTenorAltoDistance(chord)):
            output.append('Interval between tenor and alto greater than an octave in measure ' + str(chord[2].measureNumber));
               
    return output;
