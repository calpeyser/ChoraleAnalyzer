# Function checks for parallel octaves.  Returns an error message to 
# be printed, if any.
from music21 import *

def checkParallelOctaves(chorale):
    # output is a list of strings which give error messages
    output = [];

    # parallelFifths is a list of VoiceLeadingQuartet objects, each 
    # which gives a pair of intervals in illegal relationship to 
    # eachother.
    parallelOctaves = theoryAnalysis.theoryAnalyzer.getParallelOctaves(chorale);
    # iterate through list, produce error message for each VoiceLeadingQuartet
    # object.

    if not parallelOctaves:
        return output;
        
    for octave in parallelOctaves:
        output.append('Parallel octave found!' +
                      '\n Measure Number: ' + str(octave.v1n1.measureNumber) +
                      '\n First Voice: ' + 
                      '\n     First Note:  ' + str(octave.v1n1.fullName) +
                      '\n     Second Note: ' + str(octave.v1n2.fullName) +
                      '\n Second Voice: ' +
                      '\n     First Note:  ' + str(octave.v2n1.fullName) +
                      '\n     Second Note: ' + str(octave.v2n2.fullName) +
                      '\n')
                      
                      
                 
    return output;
