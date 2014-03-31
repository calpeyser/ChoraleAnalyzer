import sys
import os
from utilities import *
import subprocess, glob
from choraleAnalyzer import *
if len(sys.argv) < 2:
    print "Usage: python testBach.py [number of chorales]";
    exit();
pFlag = True;
if len(sys.argv) == 3:
    pFlag = False;

numberOfChorales = int(sys.argv[1]);
output = [];

for i in range(numberOfChorales):
    num = i + 1;
    if num < 10:
        txt = "00" + str(num);
    elif num < 100:
        txt = "0" + str(num);
    elif num < 100:
        txt = str(num);
    c = "Tymo/XMLChorales/riemenschneider" + txt + ".xml";
    b = "Tymo/BachChorales/riemenschneider" + txt + ".txt";
    input = "python choraleAnalyzer.py " + c + " " + b;
    print "Analyzing riemenschneider" + str(num);

    # Code taken from stack overflow post
    # http://stackoverflow.com/questions/15786637/python-subprocess-store-each-line-of-output-in-a-list
    globpattern = 'path/to/*.*'
    if pFlag:
        cmd = ['python', 'choraleAnalyzer.py', c, b];
    else:
        cmd = ['python', 'choraleAnalyzer.py', c, b, 'noParallels'];
    #cmd.extend(glob.glob(globpattern))
    #proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    #outputlines = filter(lambda x:len(x)>0,(line.strip() for line in proc.stdout))
    outputlines = ChoraleAnalyzer(c, b);
    output = output + outputlines;

errorTracker = errorTracker();
for line in output:
    errorTracker.processError(line);

errorTracker.printState();
