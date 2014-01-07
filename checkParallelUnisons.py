# Funciton checks for parallel unisons.  Returns an error message to
# be printed, if any.
from music21 import *

def checkParallelUnisons(chorale):
    # output is a list of strings which give error messages
    output = [];

    # identifyParallelUnisons() is a music21 method which stores all
    # parallel unisons in VLQTheoryResult objects
    theoryAnalysis.theoryAnalyzer.identifyParallelUnisons(chorale);
    
    # get list, put in parallelUnisons
    parallelUnisons = chorale.analysisData['ResultDict']['parallelUnisons'];

    # iterate through list, produce error message for each 
    # VLQTheoryResult object.  Note: A VLQTheoryResult object
    # contains a VoiceLeadingQuartet object, which can be used like
    # in other methods.
    if not parallelUnisons:
        return output;

    for unison in parallelUnisons:
        output.append('Parallel unison found!' +
                      '\n Measure Number: ' + str(unison.vlq.v1n1.measureNumber) +
                      '\n First Voice: ' +
                      '\n     First Note:  ' + str(unison.vlq.v1n1.fullName) +
                      '\n     Second Note: ' + str(unison.vlq.v1n2.fullName) + 
                      '\n Second Voice: ' +
                      '\n     First Note:  ' + str(unison.vlq.v2n1.fullName) +
                      '\n     Second Note: ' + str(unison.vlq.v2n2.fullName) +
                      '\n')
    return output; 
