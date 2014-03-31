import sys;

xmlName = sys.argv[1];
rnaName = sys.argv[2];

fa = open(xmlName, "r");
fb = open(rnaName, "r");

xmlString = fa.read();
rnaString = fb.read();

f1 = open("xmlfile.xml", "w");
f2 = open("rnafile.txt", "w");

f1.write(xmlString);
f2.write(rnaString);

