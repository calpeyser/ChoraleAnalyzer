# A progression checker contains the data for harmonic rules, and provides
# methods for validating chord sequences.

from music21 import *

class progressionChecker:
    
    MIdest   = [True , True , True , True , True , True , True ];
    Miidest  = [False, True , False, False, True , False, True ];
    Miiidest = [True , False, True , True , True , True , False];
    MIVdest  = [True , True , False, True , True , False, True ];
    MVdest   = [True , False, False, True , True , True , False];
    Mvidest  = [True , True , False, True , True , True , True ];
    Mviidest = [True , False, False, False, True , False, True ];

    midest   = [True , True , True , True , True , True , True ];
    miidest  = [False, True , False, False, True , False, True ];
    mIIIdest = [True , False, True , True , True , True , False];
    mivdest  = [True , True , False, True , True , False, True ];
    mVdest   = [True , False, False, True , True , True , False];
    mVIdest  = [True , True , False, True , True , True , True ];
    mviidest = [True , False, False, False, True , False, True ];

    # gives the appropriate modality for each scale degree
    Mmodalities = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished'];
    mmodalities = ['minor', 'diminished', 'major', 'either', 'major', 'major', 'diminished']


    # we first define a couple of simple checks. These in particular
    # return strings, not booleans.  Some are mode specific.

    # One chord checks
    def modalityErr_Major(self):
        if self.num.quality != self.Mmodalities[self.num.scaleDegree - 1] and self.Mmodalities[self.num.scaleDegree - 1] != 'either':
            return ('Measure ' + str(self.num.measureNumber) + ': In a major key, a chord on scale degree ' + str(self.num.scaleDegree) + ' must be ' + str(self.Mmodalities[self.num.scaleDegree - 1]));

    def modalityErr_Minor(self):
        if self.num.quality != self.mmodalities[self.num.scaleDegree - 1] and self.mmodalities[self.num.scaleDegree - 1] != 'either':
            return ('Measure ' + str(self.num.measureNumber) + ': In a minor key, a chord on scale degree ' + str(self.num.scaleDegree) + ' must be ' + str(self.mmodalities[self.num.scaleDegree - 1]));

    def twoInversion_Minor(self):
        if self.num.scaleDegree == 2:
            if self.num.inversion() != 1:
                return('Measure ' + str(self.num.measureNumber) + ': In a minor key,the second degree chord must appear in first inversion');

    def sixInversion_MajorMinor(self):
        if self.num.scaleDegree == 6:
            if self.num.inversion() == 1:
                return('Measure ' + str(self.num.measureNumber) + ': The sixth degree chord cannot appear in first inversion. ');
    
    def sevenInversion_MajorMinor(self):
        if self.num.scaleDegree == 7:
            if self.num.inversion() != 1:
                return('Measure ' + str(self.num.measureNumber) + ': The seventh degree chord must appear in first inversion. ');

    

    # Two chord checks
    def sixToOne_MajorMinor(self):
        if self.num1.scaleDegree == 6 and self.num2.scaleDegree == 1 and not self.of1 and not self.of2:
            if self.num2.inversion() != 1:
                return ('Measure ' + str(self.num2.measureNumber) + ': When vi resolves to the tonic, it must be I6');

    def fiveTo_Minor(self):
        if self.num1.scaleDegree == 5 and not self.of1:
            if self.num2.scaleDegree == 4 and not self.of2:
                if self.num2.quality == 'minor' or self.num2.inversion != 1:
                    return ('Measure ' + str(self.num2.measureNumber) + ': In minor, V goes to IV6, not iv6 or IV'); 
            if self.num2.scaleDegree == 6 and not self.of2:
                if self.num2.inversion() != 1:
                    return ('Measure ' + str(self.num2.measureNumber) + ': In minor, V goes to vi6, not vi');

    def pairValid_MajorMinor(self):
        out = True;
    # Check each of four cases
        # Case 1: Diatonic chord to diatonic chord
        if not self.of1 and not self.of2:
            out = self.dest[self.base1.scaleDegree - 1][self.base2.scaleDegree - 1];

        # Case 2: Diatonic chord to borrowed chord
        elif not self.of1 and self.of2 != None:
            if self.of2.quality == 'major' or self.of2.quality == 'minor':
                out = True;
            else:
                out = False;
        # Case 3: Borrowed chord to diatonic chord
        elif self.of1 != None and not self.of2:
            if self.of1.scaleDegree == self.base2.scaleDegree:
                if self.base1.scaleDegree == 5 or self.base1.scaleDegree == 7:
                    out = True;
            # deceptive progression
            elif (self.base1.scaleDegree + self.of1.scaleDegree == self.base2.scaleDegree + 7):
                out = True;
            else:
                out = False;
        # Case 4: Borrowed chord to borrowed chord
        elif self.of1 != None and self.of2 != None:
            # Subcase 1: both chords are borrowed from the same key
            if self.of1.scaleDegree == self.of2.scaleDegree:
                # same chord
                if self.base1.scaleDegree == self.base2.scaleDegree:
                    out = True;
                # preceeded by own subdominant
                elif (self.base1.scaleDegree == 4 or self.base2.scaleDegree == 2) and (self.base2.scaleDegree == 5 or self.base2.scaleDegree == 7):
                    out = True;
                # deceptive progression
                elif self.base1.scaleDegree + self.of1.scaleDegree + 1 == self.base2.scaleDegree + self.of2.scaleDegree:
                    out = True;
                else:
                    out = False;
            # Subcase 2: the chords are borrowed from different keys
            else:
                out = False;
    
        if out == False:
            return ('Measure ' + str(self.num1.measureNumber) + ': Invalid progression from ' + str(self.num1.figure) + ' to ' + str(self.num2.figure) + '.');


  
    # there are two types of progressionCheckers - major and minor.  They 
    # have an array of allowed simple progressions, and a list of mode 
    # specific checks to be run.

    def __init__(self, mode):
        assert(mode == "major" or mode == "minor")
        self.mode = mode;
        if mode == "major":
            self.dest = [self.MIdest, self.Miidest, self.Miiidest, self.MIVdest, self.MVdest, self.Mvidest, self.Mviidest];
            self.singleChecks = [self.modalityErr_Major, self.sixInversion_MajorMinor, self.sevenInversion_MajorMinor];
            self.doubleChecks = [self.sixToOne_MajorMinor, self.pairValid_MajorMinor];

        if mode == "minor":
            self.dest = [self.midest, self.miidest, self.mIIIdest, self.mivdest, self.mVdest, self.mVIdest, self.mviidest];
            self.singleChecks = [self.modalityErr_Minor, self.twoInversion_Minor, self.sixInversion_MajorMinor, self.sevenInversion_MajorMinor];
            self.doubleChecks = [self.sixToOne_MajorMinor, self.fiveTo_Minor, self.pairValid_MajorMinor];


    # setChords is meant to set up the progressionChecker for use on a pair 
    # of chords, in order to verify the progression.  If isValid is called
    # after a setChords call, the validity of the pair will be determined
    def setChords(self, numA, numB):

        # tell the object that it is of type TwoChord
        self.checkerType = "TwoChord";

        # first we must store the roman numerals
        self.num1 = numA;
        self.num2 = numB;

        # now must parse into base and of
        if not self.num1.secondaryRomanNumeral:
            self.base1 = self.num1;
            self.of1 = None;
        else:
            breakdown = self.num1.figure.split("/" + self.num1.secondaryRomanNumeral.figure);
            self.base1 = roman.RomanNumeral(breakdown[0]);
            self.of1 = roman.RomanNumeral(self.num1.secondaryRomanNumeral.figure);
        if not self.num2.secondaryRomanNumeral:
            self.base2 = self.num2;
            self.of2 = None;
        else:
            breakdown = self.num2.figure.split("/" + self.num2.secondaryRomanNumeral.figure);
            self.base2 = roman.RomanNumeral(breakdown[0]);
            self.of2 = roman.RomanNumeral(self.num2.secondaryRomanNumeral.figure); 
                
    def setChord(self, num):

        # tell the object that it is of type OneChord
        self.checkerType = "OneChord";

        # first we must store the roman numeral
        self.num = num;

        # now must parse into base and of
        if not self.num.secondaryRomanNumeral:
            self.base = self.num;
            self.of = None;
        else:
            breakdown = self.num.figure.split("/" + self.num.secondaryRomanNumeral.figure);
            self.base = roman.RomanNumeral(breakdown[0]);
            self.of = roman.RomanNumeral(self.num.secondaryRomanNumeral.figure);
        
    # tells if whatever was put into the progressionChecker is valid.
    # If a single chord was put in, validates it.  If two chords were put
    # in, validates the transition.
    def isValid(self):
        output = [];
        if self.checkerType == "OneChord":
            for function in self.singleChecks:
                err = function();
                if err != None:
                    output.append(err);
        elif self.checkerType == "TwoChord":
            for function in self.doubleChecks:
                err = function();
                if err != None:
                    output.append(err);

        return output;
