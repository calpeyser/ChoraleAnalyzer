# module contains utilities 

import string

# assign list of errors
def assignList():
    global errorList;
    errorList = [];
    
# get list of errors
def retrieveList():
    return errorList;


# removes duplicates from a list
def removeDuplicates(errors):
    seen = [];
    for error in errors:
        if error not in seen:
            seen.append(error);
    return seen;

# function takes as an argument a function which returns error messages.
# the messages are then printed
def printErrors(errorGenerator, arg, initialMes, clearMes):
    out = [];
    out.append("    " + initialMes);
    messages = errorGenerator(arg);
    if not messages:
        out.append("    " + clearMes);
    else:
        for error in messages:
            out.append(error);
            errorList.append(error);
    out.append("-----------------------------------------------------");
    return out;

# An errorTracker is a data structure meant to store the types and number
# of errors occuring over several chorale checks, or over one chorale check
class errorTracker:
    
    def __init__(self, progTrackers = None):
        # Parallel Intervals
        self.P1 = 0;
        self.P5 = 0;
        self.P8 = 0;
        # Ranges
        self.bassRange = 0;
        self.tenorRange = 0;
        self.altoRange = 0;
        self.sopRange = 0;
        # Closeness
        self.altSopInt = 0;
        self.tenAltInt = 0;
        # Voice Crossing
        self.BTVC = 0;
        self.TAVC = 0;
        self.ASVC = 0;
        # Tritones
        self.tritone = 0;
        # Repeated Bass
        self.repBass = 0;
        # Chord progressions
        self.inversion = 0;
        self.majorMinor = 0;
        self.invalidProg = 0;

        # progTrackers
        self.progTrackers = progTrackers;

        # For each of the 17 error types, average violations per measure
        # in the chorales
        self.bachViolations = [0.000994036, 0.21868787, 0.001988072, 0.081510934, 0.005964215, 0.000994036, 0.000994036, 0.021868787, 0.07554672, 0.040755467, 0.093439364, 0.028827038, 0.047713718, 0.034791252, 0.03777336, 0.078528827, 0.093439364]
        # The average violations per measure in this chorale
        self.inputViolations = [];


    def printState(self):
        print('P1: ' + str(self.P1));
        print('P5: ' + str(self.P5));
        print('P8: ' + str(self.P8));
        print('bassRange: ' + str(self.bassRange));
        print('tenorRange: ' + str(self.tenorRange));
        print('altoRange: ' + str(self.altoRange));
        print('sopRange: ' + str(self.sopRange));
        print('altSopInt: ' + str(self.altSopInt));
        print('tenAltInt: ' + str(self.tenAltInt));
        print('BTVC: ' + str(self.BTVC));
        print('TAVC: ' + str(self.TAVC));
        print('ASVC: ' + str(self.ASVC));
        print('tritone: ' + str(self.tritone));
        print('repBass: ' + str(self.repBass));
        print('inversion: ' + str(self.inversion));
        print('majorMinor: ' + str(self.majorMinor));
        print('invalidProg: ' + str(self.invalidProg));

    # takes an error and updates local variables.  Works by basic
    # string manipulation
    def processError(self, err):
        sp = err.split();
        if len(sp) < 3:
            return
        firstWord = sp[0];
        secondWord = sp[1];
        thirdWord = sp[2];
        lastWord = sp[-1];

        # get beat and measure
        if "measure" in sp and "beat" in sp:
            measure = sp[sp.index("measure") + 1];
            beat = sp[sp.index("beat") + 1];
        else:
            measure = None;
            beat = None;

        # identify subset of progTrackers that are relevant
        incidentProgs = [];
        if measure != None and self.progTrackers:
            for i in range(len(self.progTrackers)):
                if self.progTrackers[i].contains(measure, beat):
                    incidentProgs.append(i);
                    
        # Parallel Unison
        if secondWord == 'unison':
            self.P1 = self.P1 + 1;
        # Parallel Fifth
        elif secondWord == 'fifth':
            self.P5 = self.P5 + 1;
        # Parallel Octave
        elif secondWord == 'octave':
            self.P8 = self.P8 + 1;
        # Bass Range
        elif firstWord == 'Bass' and secondWord == 'out':
            self.bassRange = self.bassRange + 1;
            for i in incidentProgs:
                self.progTrackers[i].bassRange += 1;
        # Tenor Range
        elif firstWord == 'Tenor' and secondWord == 'out':
            self.tenorRange = self.tenorRange + 1;
            for i in incidentProgs:
                self.progTrackers[i].tenorRange += 1;
        # Alto Range
        elif firstWord == 'Alto' and secondWord == 'out':
            self.altoRange = self.altoRange + 1;
            for i in incidentProgs:
                self.progTrackers[i].altoRange += 1;
        # Soprano Range
        elif firstWord == 'Soprano' and secondWord == 'out':
            self.sopRange = self.sopRange + 1;
            for i in incidentProgs:
                self.progTrackers[i].sopRange += 1;
        # Alto Soprano Closeness
        elif firstWord == 'Interval' and thirdWord == 'alto':
            self.altSopInt = self.altSopInt + 1;
            for i in incidentProgs:
                self.progTrackers[i].altSopInt += 1;
        # Tenor Alto Closeness
        elif firstWord == 'Interval' and thirdWord == 'tenor':
            self.tenAltInt = self.tenAltInt + 1;
            for i in incidentProgs:
                self.progTrackers[i].tenAltInt += 1;
        # Bass Tenor Voice Crossing
        elif firstWord == 'Bass/Tenor':
            self.BTVC = self.BTVC + 1;
            for i in incidentProgs:
                self.progTrackers[i].BTVC += 1;
        # Tenor Alto Voice Crossing
        elif firstWord == 'Tenor/Alto':
            self.TAVC = self.TAVC + 1;
            for i in incidentProgs:
                self.progTrackers[i].TAVC += 1;
        # Alto Soprano Voice Crossing
        elif firstWord == 'Alto/Soprano':
            self.ASVC = self.ASVC + 1;
            for i in incidentProgs:
                self.progTrackers[i].ASVC += 1;
        # Tritone
        elif thirdWord == 'tritone':
            self.tritone = self.tritone + 1;
            for i in incidentProgs:
                self.progTrackers[i].tritone += 1;
        # Repeated Bass
        elif firstWord == 'Repeated':
            self.repBass = self.repBass + 1;
            for i in incidentProgs:
                self.progTrackers[i].repBass += 1;
        # Inversion
        elif lastWord == 'inversion':
            self.inversion = self.inversion + 1;
        elif lastWord == 'I6':
            self.inversion = self.inversion + 1;
        # Major/Minor
        elif lastWord == 'major' or lastWord == 'minor':
            self.majorMinor = self.majorMinor + 1;
        # Invalid progression
        elif thirdWord == 'Invalid':
            self.invalidProg = self.invalidProg + 1;

    def printProgProfiles(self):
        for prog in self.progTrackers:
            prog.printProgressionTracker();

    def computeBachness(self, numberOfMeasures):
        self.inputViolations = [self.P1, self.P5, self.P8, self.bassRange, self.tenorRange, self.altoRange, self.sopRange, self.altSopInt, self.tenAltInt, self.BTVC, self.TAVC, self.ASVC, self.tritone, self.repBass, self.inversion, self.majorMinor, self.invalidProg];
        for i in range(len(self.inputViolations)):
            self.inputViolations[i] = float(self.inputViolations[i])/numberOfMeasures;
        ratios = [];
        for i in range(len(self.bachViolations)):
            ratios.append(self.inputViolations[i]/self.bachViolations[i]);

        bachness = 0;
        for i in ratios:
            bachness += i;

        return bachness/17;

# A progressionTracker represents a single chord progression occuring in a single chorale
# it can store incident rule violations
class progressionTracker:

    def __init__(self, stringProg, startM, startB, endM, endB):
        self.prog = stringProg;
        self.chords = string.split(stringProg, " -> ");
        self.size = len(self.chords);
        self.startM = startM;
        self.endM = endM;
        self.startB = startB;
        self.endB = endB;

        # incident violations
        self.P1 = 0;
        self.P5 = 0;
        self.P8 = 0;
        # Ranges
        self.bassRange = 0;
        self.tenorRange = 0;
        self.altoRange = 0;
        self.sopRange = 0;
        # Closeness
        self.altSopInt = 0;
        self.tenAltInt = 0;
        # Voice Crossing
        self.BTVC = 0;
        self.TAVC = 0;
        self.ASVC = 0;
        # Tritones
        self.tritone = 0;
        # Repeated Bass
        self.repBass = 0;
        # Chord progressions
        self.inversion = 0;
        self.majorMinor = 0;
        self.invalidProg = 0;

    def contains(self, measure, beat):
        errorMB = int(measure) + 0.1*int(beat.split(".")[0]);
        startMB = int(self.startM) + 0.1*int(self.startB.split(".")[0]);
        endMB = int(self.endM) + 0.1*int(self.endB.split(".")[0]);     

        if (errorMB >= startMB) and (errorMB <= endMB):
            return True;
        else: return False;


    # add self to prog2, return the sum
    def addProg(self, prog2):
            self.P1 += prog2.P1;
            self.P5 += prog2.P5;
            self.P8 += prog2.P8;
            self.bassRange += prog2.bassRange 
            self.tenorRange += prog2.tenorRange;
            self.altoRange += prog2.altoRange;
            self.sopRange += prog2.sopRange;
            self.altSopInt += prog2.altSopInt;
            self.tenAltInt += prog2.tenAltInt;
            self.BTVC += prog2.BTVC;
            self.TAVC += prog2.TAVC;
            self.ASVC += prog2.ASVC;
            self.tritone += prog2.tritone;
            self.repBass += prog2.repBass;
            return self;

    # is this the same progression as prog2?
    def equals(self, prog2):
        if self.prog == prog2.prog: 
            return True;
        else: return False;

    # produces a string representation of the progression and the errors
    def printProgressionTracker(self):
        print "Size: " + str(self.size);
        print "Prog: " + str(self.prog);
        print "Goes from: " + str(self.startM) + "/" + str(self.startB) +  " to " + str(self.endM) + "/" + str(self.endB);
        print('P1: ' + str(self.P1));
        print('P5: ' + str(self.P5));
        print('P8: ' + str(self.P8));
        print('bassRange: ' + str(self.bassRange));
        print('tenorRange: ' + str(self.tenorRange));
        print('altoRange: ' + str(self.altoRange));
        print('sopRange: ' + str(self.sopRange));
        print('altSopInt: ' + str(self.altSopInt));
        print('tenAltInt: ' + str(self.tenAltInt));
        print('BTVC: ' + str(self.BTVC));
        print('TAVC: ' + str(self.TAVC));
        print('ASVC: ' + str(self.ASVC));
        print('tritone: ' + str(self.tritone));
        print('repBass: ' + str(self.repBass));
        print('inversion: ' + str(self.inversion));
        print('majorMinor: ' + str(self.majorMinor));
        print('invalidProg: ' + str(self.invalidProg));

    # produces a string representation of the progression, not the errors
    def printProgString(self):
        print "Prog: " + str(self.prog);



