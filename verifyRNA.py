# Verifies correctness of a roman numeral analysis

from music21 import *


def compareRomanToChord(rom, ch):
    if (ch.root().name != rom.root().name):
        return "Incorrect chord root";
    elif (ch.inversion() != rom.inversion()):
        return "Incorrect inversion";
    elif (ch.quality != rom.quality and ch.quality != 'other'):
        return "Incorrect chord quality";
    elif (ch.isDominantSeventh() != rom.isDominantSeventh()):
        return "Incorrect dominant seventh identification, or some part of dominant seventh chord not present";
    else:
        return "No error";

def verifyRNA(choraleAndNum):
    # output is a list of strings which give error messages
    output = [];

    # decompose input
    chorale = choraleAndNum[0];
    num = choraleAndNum[1];

    # obtain chord breakdown
    chordification = chorale.chordify();

    # obtain the type of a RomanNumeral object, for type checking
    SampleRomanNumeral = roman.RomanNumeral('I');
    TypeRomanNumeral = type(SampleRomanNumeral);

    # obtain the type of a chord object, for type checking
    TypeChord = chord.Chord;

    # create numeral list as follows:
    #    0: measure.beat as number
    #    1: RomanNumeral object
    numList = [];
    for omeasure in range(len(num)):
        for romanNumeral in range(len(num[omeasure])):
            if type(num[omeasure][romanNumeral]) == TypeRomanNumeral:
                entry = [];
                time = num[omeasure][romanNumeral].measureNumber + (0.1)*num[omeasure][romanNumeral].beat;
                time = round(time, 4);
                entry.append(time);
                entry.append(num[omeasure][romanNumeral]);
                numList.append(entry);

    # create chord list as follows
    #     0: measure.beat as number
    #     1: Chord object
    chordList = [];
    for omeasure in range(len(chordification))[1:]:
        for ochord in range(len(chordification[omeasure])):
            if type(chordification[omeasure][ochord]) == TypeChord:
                entry = [];
                time = chordification[omeasure][ochord].measureNumber + (0.1)*chordification[omeasure][ochord].beat;
                # round to cutoff extra decimal values
                time = round(time, 4);
                # add to chordList
                entry.append(time);
                entry.append(chordification[omeasure][ochord]);
                chordList.append(entry);

    # I define a correct roman numeral analysis as one in which each
    # numeral lines up with an appropriate chord.  Verify by going 
    # by going through numList.  Use a boolean to make sure there
    # is a chord for each roman numeral
    for i in range(len(numList)):
        numeralPair = numList[i]
        foundChord = False;
        for j in range(len(chordList)):
            chordPair = chordList[j];
            if (chordPair[0] == numeralPair[0]):
                foundChord = True;
                # One chord case:
                if (j == len(chordList) - 1 or i == len(numList) - 1 or numList[i+1][0] <= chordList[j+1][0]):
                    err = compareRomanToChord(numeralPair[1], chordPair[1]);
                    if (err != "No error"):
                        spl = str(chordPair[0]).split('.');
                        if len(spl[1]) > 1:
                            spl[1] = spl[1][0] + "." + spl[1][1];
                            output.append(err + " in measure " + spl[0] + " beat " + spl[1]);
                
                # Two chord case:
                else:
                    err = compareRomanToChord(numeralPair[1], chordPair[1]);
                    err2 = compareRomanToChord(numeralPair[1], chordList[j+1][1]);
                    if (err != "No error" and err2 != "No error"):
                        spl = str(chordPair[0]).split('.');
                        if len(spl[1]) > 1:
                            spl[1] = spl[1][0] + "." + spl[1][1];
                            output.append(err + " in measure " + spl[0] + " beat " + spl[1]);

        if (foundChord == False):
            spl = str(numeralPair[0]).split('.');
            if len(spl[1]) > 1:
                spl[1] = spl[1][0] + "." + spl[1][1];
            output.append("No chord found for roman numeral in measure " + spl[0] + " beat " + spl[1]);
   
    return output;
