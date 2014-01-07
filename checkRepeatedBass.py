# Funciton checks for repeated bass notes.  Returns an error message to
# be printed, if any.
from music21 import *

def checkRepeatedBass(chordification):
    # output is a list of strings which give error messages
    output = [];

    # We create a list of measures. While were at it, find time
    # signature
    measures = [];   
    for i in range(len(chordification)):
        if str(type(chordification[i])) == "<class 'music21.stream.Measure'>":
            measures.append(chordification[i]);
    timeSignature = measures[1].bestTimeSignature().numerator;


    # We now create a list of notes, maintaining measureNum 
    # as a property.  Also maintain beat in bt property.
    bassNotes = [];
    for m in range(len(measures)):
        for n in range(len(measures[m])):
            if str(type(measures[m][n])) == "<class 'music21.chord.Chord'>":
                bassNote = measures[m][n][-1];
                bassNote.measureNum = m;
                bassNote.bt = measures[m][n].beat + timeSignature*m;
                bassNotes.append(bassNote);

    # Go note to note, and identify repeated bass notes
    for i in range(len(bassNotes) - 1):
        firstNote = bassNotes[i];
        secondNote = bassNotes[i+1];
        if firstNote.pitch == secondNote.pitch:
            if firstNote.bt + firstNote.duration.quarterLength < secondNote.bt:
                output.append("Repeated bass note (" + str(secondNote.pitch) + ") in measure " + str(secondNote.measureNum));


    
    return output;


         
