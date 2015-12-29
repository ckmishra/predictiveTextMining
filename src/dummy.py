'''
Created on Nov 20, 2015

@author: apple
'''
import sys,csv

def main(argv) :
    documentFileLocation = sys.argv[1];
    vocabularyFileLocation = sys.argv[2];
    document = open(documentFileLocation, 'r+');
    vocabulary = open(vocabularyFileLocation, "r+")
    header = vocabulary.read().splitlines();
    header.insert(0, "ID");
    print "Length of Header ", len(header)
    
    finalCsv = sys.argv[2]
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
        wordList = wordList[2:int(unique) + 2]
        wordList.insert(0, "ID");
        values = [True] * len(wordList);
        values.insert(0, docid);
        trueValues = dict(zip(wordList, values))
        initialDictionary.update(trueValues);
        writer.writerow(initialDictionary);
        print initialDictionary


if __name__ == '__main__':
    main(sys.argv[1:])