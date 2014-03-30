# Function performs zero-th order analysis.  Checks each chord for internal 
# violations of the style.
from checkRanges import *
from checkCloseness import *
from checkVoiceCrossing import *
from utilities import printErrors

def checkZeroOrder(chorale):
    out = [];

    # slices is a list of VerticalSlice objects, each of which 
    # contains one chord of the chorale.  Note that in each slice,
    # object, the parts are numbered as follows: 0-soprano, 1-alto,
    # 2-tenor, 3-bass
    slices = theoryAnalysis.theoryAnalyzer.getVerticalSlices(chorale);

    # check ranges
    for line in printErrors(checkRanges, slices, "Checking ranges", "All parts in range"):
        out.append(line);
    # check part distances
    for line in printErrors(checkCloseness, slices, "Checking distances between parts", "All parts sufficiently close together"):
        out.append(line);

    # check voice crossings
    for line in printErrors(checkVoiceCrossing, slices, "Checking for voice crossings", "No voice crossings found"):
        out.append(line);
   
    return out;
