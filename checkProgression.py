# Funciton checks for illegal progressions
from music21 import *
from progressionChecker import *
 
def checkProgressionPairs(rom, dim = 2):
    # output is a list of strings which give error messages
    output = [];

    # rom1D is a one dimensional list of roman numerals
    if (dim == 1):
        rom1D = rom;

    if (dim == 2):
        rom1D = [];
        for x in range(len(rom)):
            for y in range(len(rom[x])):
                if type(rom[x][y]) == roman.RomanNumeral:
                    rom1D.append(rom[x][y]);
    

    # create a progressionChecker object with the right starting mode
    checker = progressionChecker(rom1D[0].key.mode);


    # Pairs of chords:  iterate until second to last chord. 
    for i in range(len(rom1D) - 1):
        # if modulation, recursively call checkProgression
        if (rom1D[i].key != rom1D[i+1].key):
            return output + checkProgressionPairs(rom1D[i+1:], 1);
        else:
            checker.setChords(rom1D[i], rom1D[i+1]);
            err = checker.isValid()
            if (len(err) != 0):
                for errorString in err:
                    output.append(errorString);

    return output;
         

 
def checkProgressionSingles(rom, dim = 2):
    # output is a list of strings which give error messages
    output = [];

    # rom1D is a one dimensional list of roman numerals
    if (dim == 1):
        rom1D = rom;

    if (dim == 2):
        rom1D = [];
        for x in range(len(rom)):
            for y in range(len(rom[x])):
                if type(rom[x][y]) == roman.RomanNumeral:
                    rom1D.append(rom[x][y]);
    

    # create a progressionChecker object with the right starting mode
    checker = progressionChecker(rom1D[0].key.mode);


    # Pairs of chords:  iterate until second to last chord. 
    for i in range(len(rom1D)):
        # if modulation, recursively call checkProgression
        if (i < len(rom1D) - 1):
            if (rom1D[i].key != rom1D[i+1].key):
                return output + checkProgressionSingles(rom1D[i+1:], 1);

        checker.setChord(rom1D[i]);
        err = checker.isValid()
        if (len(err) != 0):
            for errorString in err:
                output.append(errorString);

    return output;


# return errors in roman numeral analysis. Covers only those errors which
# can be determined from the roman numeral analysis itself.
def checkProgression(rom):
    return checkProgressionSingles(rom) + checkProgressionPairs(rom);



