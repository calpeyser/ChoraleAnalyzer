# Gather all progressions in a chorale

from music21 import *
import utilities

# returns a list of romannumeral objects
def getChordList(rntext):
	numerals = [];
	for i in range(len(rntext[1])):
		for j in range(len(rntext[1][i])):
			if type(rntext[1][i][j]) == roman.RomanNumeral:
				numerals.append(rntext[1][i][j]);
	return numerals;

def gatherProgs(rntext):
	rna = getChordList(rntext); # a list of all the chords in the chorale
	trackers = dochorale(rna, 1, 5);
	return trackers;


# method mostly adapted from work done by Dr. Dmitri Tymozcko
def dochorale(rna, n, size):															# record progressions UP TO size n
	global counts, locations, output, pTreb, pBass, chorale, analyzed_file, anal
	global quarterChords, eighthEighthChords
	global startOffset, endOffset, ourKey, lastMeasure
	#anal = analyzed_file.flat.getElementsByClass(['RomanNumeral', 'RomanTextUnprocessedToken']) #CAL: An array full of roman numerals
	anal = rna;
	#anal.show('text')
	trackers = [];
	lastMeasure = 0
	startOffset = 0
	endOffset = 0
	for i in range(len(anal) - size + 1):
		RN = []
		stopRecording = False
		ourKey = []
		progStr = ''
		lastSym = ''
		
		"""Main loop: breaks the recording process if we have a phrase marker ||, an unknown key sign ?: or a key change"""
		
		for j in range(0, size):
			if 'RomanTextUnprocessedToken' in anal[i+j].classes: 
				stopRecording = True
				break
			elif anal[i+j].figure == '?:':
				stopRecording = True
				break
			else:
				if not ourKey:
					theFigure = anal[i+j]
					if (anal[i+j].pivotChord):					# if the progression starts with a pivot chord, use the later tonality
						theFigure = anal[i+j].pivotChord
					ourKey = theFigure.key.pitchAndMode
					progStr = theFigure.figure
					lastSym = theFigure.figure
					startOffset = anal[i+j].offset
					endOffset = anal[i+j].offset

					sMeasure = str(anal[i].measureNumber);
					eMeasure = str(anal[i+j].measureNumber);
					sBeat = str(anal[i].beat);
					eBeat = str(anal[i+j].beat);

					tracker = utilities.progressionTracker(progStr, sMeasure, sBeat, eMeasure, eBeat);   # create a progression tracker for this progression
				else:
					if anal[i+j].key.pitchAndMode == ourKey and anal[i+j].figure != lastSym:
						progStr = progStr + ' -> ' + anal[i+j].figure
						lastSym = anal[i+j].figure
						endOffset = anal[i+j].offset
						sMeasure = str(anal[i].measureNumber);
						eMeasure = str(anal[i+j].measureNumber);
						sBeat = str(anal[i].beat);
						eBeat = str(anal[i+j].beat);

						tracker = utilities.progressionTracker(progStr, sMeasure, sBeat, eMeasure, eBeat);   # create a progression tracker for this progression
					else:
						stopRecording = True
						break
			trackers.append(tracker);
		if stopRecording: continue
		
		"""
		"Compute stats on duration of RNs.  Doesn't work for some deClerq/Temperley Files; not currently used"
		try:
			if anal[i].beat - int(anal[i].beat) < .01 and anal[i].duration.quarterLength == 1: 
				quarterChords += 1
				#print anal[i].figure, "quarterchord"
			if anal[i].beat - int(anal[i].beat) < .01 and anal[i].duration.quarterLength == .5 and anal[i+1].duration.quarterLength == .5:
				eighthEighthChords += 1 
				#print anal[i].figure, anal[i+1].figure, "eighth eighth"
		except:
			pass"""
		
	return trackers;
