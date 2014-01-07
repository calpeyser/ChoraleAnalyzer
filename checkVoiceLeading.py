# Function performs voice leading analysis.  Checks each chord for internal 
# violations of the style.
from checkTritones import *
from checkRepeatedBass import *
from utilities import printErrors

def checkVoiceLeading(chorale):

    chordification = chorale.chordify();
    slices = theoryAnalysis.theoryAnalyzer.getVerticalSlices(chorale);

    # check for tritones
    printErrors(checkTritones, slices, "Checking for tritones", "No tritones found");
    # check for repeated bass tones
    printErrors(checkRepeatedBass, chordification, "Checking for repeated bass notes", "No repeated bass notes");

    # could add check2leap, checkDimInt
