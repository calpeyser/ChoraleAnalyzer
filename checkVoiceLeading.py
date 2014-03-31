# Function performs voice leading analysis.  Checks each chord for internal 
# violations of the style.
from checkTritones import *
from checkRepeatedBass import *
from utilities import printErrors

def checkVoiceLeading(chorale):
    out = [];
    chordification = chorale.chordify();
    slices = theoryAnalysis.theoryAnalyzer.getVerticalSlices(chorale);

    # check for tritones
    for line in printErrors(checkTritones, slices, "Checking for tritones", "No tritones found"):
        out.append(line);
    # check for repeated bass tones
    for line in printErrors(checkRepeatedBass, chordification, "Checking for repeated bass notes", "No repeated bass notes"):
        out.append(line);

    # could add check2leap, checkDimInt

    return out;
