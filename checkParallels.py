# Function checks for parallels by calling relevant functions.

from checkParallelFifths import *
from checkParallelOctaves import *
from checkParallelUnisons import *
from utilities import printErrors


# returns a list of measure.beat for each note
def getOffsetArray(part):
    offsetDict = {};
    offsets = [];
    measureNumber = -1;
    for elementA in range(len(part)):
        if isinstance(part[elementA], stream.Measure):
            measureNumber = measureNumber + 1;
            for elementB in range(len(part[elementA])):
                if isinstance(part[elementA][elementB], note.Note):
                    offsetDict[round(measureNumber+part[elementA][elementB].beat*(0.1),4)] = part[elementA][elementB];
                    offsets.append(round(measureNumber+part[elementA][elementB].beat*(0.1),4));
    return [offsets, offsetDict];
        

def checkParallels(chorale):
    out = [];

    offsetInfo = [getOffsetArray(chorale.parts[0]), getOffsetArray(chorale.parts[1]), getOffsetArray(chorale.parts[2]), getOffsetArray(chorale.parts[3])];
    input = [chorale, offsetInfo];

    # find parallel unisons   
    for line in printErrors(checkParallelUnisons, input, "Scanning for parallel unisons", "No parallel unisons found"):
        out.append(line);
   
    # find parallel octaves  
    for line in printErrors(checkParallelOctaves, input, "Scanning for parallel octaves", "No parallel octaves found"):
        out.append(line);

    # find parallel fifths          
    for line in printErrors(checkParallelFifths, input, "Scanning for parallel fifths", "No parallel fifths found"):
        out.append(line);

    return out;
