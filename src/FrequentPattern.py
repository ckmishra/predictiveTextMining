'''
Created on Nov 20, 2015

@author: apple
'''
import csv
'''
Created on Nov 20, 2015

@author: chandan
'''
document = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/DocumentWords.txt", 'r+');
freq = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/freq_0.25.csv","rU");
freqset = set();
for row in csv.reader(freq) : 
    print row
    for i in range(len(row)):
     freqset.add(row[i])
    
freqset.remove("");
header = list(freqset);
header.insert(0, "ID");
print "Length of Header ", len(header)


finalCsv = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/final_freq.csv"
csvfile = open(finalCsv, 'w+');
writer = csv.DictWriter(csvfile, fieldnames=header)
writer.writeheader();


initializeFalse = [False] * (len(header) - 1) 
lines = document.readlines();

for line in lines :
    initialDictionary = dict(zip(header[1:], initializeFalse))
    wordList = line.rstrip('\r\n').split(",");
    docid = wordList[0];
    unique = wordList[1];
    wordList = set(header).intersection(wordList);
    wordList = list(wordList);
    wordList.insert(0, "ID");
    values = [True] * len(wordList);
    values.insert(0, docid);
    trueValues = dict(zip(wordList, values))
    initialDictionary.update(trueValues);
    writer.writerow(initialDictionary);
    print initialDictionary



