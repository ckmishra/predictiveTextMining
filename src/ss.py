'''
Created on Nov 20, 2015

@author: apple
'''
import sys,getopt
def main(argv) :
    vocabulary = ''
    documentWords = ''
    outputfile = ''
    try:
     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'txtToCsvConverter.py -d <documentWords.txt> -v <Vocabulary.txt> -o <documentWords.csv>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'txtToCsvConverter.py -d <documentWords.txt> -v <Vocabulary.txt> -o <documentWords.csv>'
            sys.exit()
        elif opt in ("-d", "--ifile"):
            documentWords = arg
        elif opt in ("-v", "--ifile"):
            vocabulary = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', documentWords
    print 'Output file is "', outputfile
    document= open(documentWords,'r+');
    vocabulary = open(vocabulary, "r+")
    header = vocabulary.read().splitlines();
    header.insert(0,"ID");
    print "Length of List ", len(header)
    
    import csv
    csvfile= open(outputfile, 'w+');
    writer = csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader();
    
    trueValues = {}
    dummy = {}
    initilizeFalse = [False]*(len(header)-1) 
    
    for line in document:
        lines = line.splitlines();
        
    for i in range(len(lines)) :    
        dummy = dict(zip(header[1:],initilizeFalse))
        words = lines[i];
        print len(words)
        print words
        wordList = words.split(",")
        unique  = wordList[1];
        print unique
        docid = wordList[0];
        wordList =wordList[2:int(unique)+2]
        wordList.insert(0,"ID");
        values = [True]*len(wordList) 
        values.insert(0,docid);
        trueValues = dict(zip(wordList,values))
        dummy.update(trueValues);
        writer.writerow(dummy);
        print dummy


if __name__ == "__main__":
    main(sys.argv[1:])