'''
Created on Nov 20, 2015

@author: chandan
'''
root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/submit";

document = open(root + "/DocumentWords.txt", 'r+');
vocabulary = open(root + "/Vocabulary.txt", "r+");
header = vocabulary.read().splitlines();
header.insert(0, "ID");
print "Length of Header ", len(header)

import csv
finalCsv = root + "/MatrixFormData.csv";
csvfile = open(finalCsv, 'w+');
writer = csv.DictWriter(csvfile, fieldnames=header)
writer.writeheader();

initializeFalse = [0] * (len(header) - 1) 
lines = document.readlines();
print len(lines)
i = 0
for line in lines :
    initialDictionary = dict(zip(header[1:], initializeFalse))
    wordList = line.rstrip('\r\n').split(",");
    docid = wordList[0];
    unique = wordList[1];
    wordList = wordList[2:int(unique) + 2]
    wordList.insert(0, "ID");
    values = [1] * len(wordList);
    values.insert(0, docid);
    trueValues = dict(zip(wordList, values))
    initialDictionary.update(trueValues);
    writer.writerow(initialDictionary);

