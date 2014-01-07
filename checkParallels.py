# Function checks for parallels by calling relevant functions.
# Prints

from checkParallelFifths import *
from checkParallelOctaves import *
from checkParallelUnisons import *
from utilities import printErrors

def checkParallels(chorale):

    # find parallel unisons   
    printErrors(checkParallelUnisons, chorale, "Scanning for parallel unisons", "No parallel unisons found");
   
    # find parallel octaves  
    printErrors(checkParallelOctaves, chorale, "Scanning for parallel octaves", "No parallel octaves found");

    # find parallel fifths          
    printErrors(checkParallelFifths, chorale, "Scanning for parallel fifths", "No parallel fifths found");

