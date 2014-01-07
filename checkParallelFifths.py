# Function checks for parallel fifths.  Returns an error message to 
# be printed, if any.
from music21 import *

def checkParallelFifths(chorale):
    # output is a list of strings which give error messages
    output = [];

    # parallelFifths is a list of VoiceLeadingQuartet objects, each 
    # which gives a pair of intervals in illegal relationship to 
    # eachother.
    parallelFifths = theoryAnalysis.theoryAnalyzer.getParallelFifths(chorale);
    
    # iterate through list, produce error message for each VoiceLeadingQuartet
    # object.
    if not parallelFifths:
        return output;

    for fifth in parallelFifths:
        output.append('Parallel fifth found!' +
                      '\n Measure Number: ' + str(fifth.v1n1.measureNumber) +
                      '\n First Voice: ' + 
                      '\n     First Note:  ' + str(fifth.v1n1.fullName) +
                      '\n     Second Note: ' + str(fifth.v1n2.fullName) +
                      '\n Second Voice: ' +
                      '\n     First Note:  ' + str(fifth.v2n1.fullName) +
                      '\n     Second Note: ' + str(fifth.v2n2.fullName) +
                      '\n')                 
    return output;
