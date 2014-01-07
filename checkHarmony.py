# Function performs basic harmonic analysis.  Checks each chord for internal 
# violations of the style.
from music21 import *
from verifyRNA import verifyRNA
from checkProgression import *
from utilities import printErrors

def checkHarmony(chorale, rntext):

    # slices is a list of VerticalSlice objects, each of which 
    # contains one chord of the chorale.  Note that in each slice,
    # object, the parts are numbered as follows: 0-soprano, 1-alto,
    # 2-tenor, 3-bass
    slices = theoryAnalysis.theoryAnalyzer.getVerticalSlices(chorale);

    # roman is a stream object which contains the roman numeral analysis
    # inputed by the student
    rom = rntext[1];

    choraleAndRoman = [chorale, rom];

    printErrors(verifyRNA, choraleAndRoman, "Verifying that Roman Numeral Analysis in fact reflects the score", "Roman Numeral Analysis appears to be correct");
    
    printErrors(checkProgression, rom, "Validating chord progressions in Roman Numeral Analysis", "Chord Progression Valid");

   
