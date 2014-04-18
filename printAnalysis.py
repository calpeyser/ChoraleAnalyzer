#import choraleAnalyzer
import sys
import pickle

#for line in choraleAnalyzer.ChoraleAnalyzer(sys.argv[1], sys.argv[2], True):
#	print line;

print "----ANALYSIS PLACEHOLDER-----";


class dummyErrorTracker:
	def __init__(self):
		self.x = range(100);
	def save_to_pkl(self, file_name):
		f = open(file_name, "w");
		pickle.dump(self, f);
		f.close();


dummy = dummyErrorTracker();
dummy.save_to_pkl("error_tracker.pkl");
