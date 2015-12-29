'''
Created on Nov 27, 2015

@author: apple
'''
import csv
root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/submit"
k=4
frequentDoc = open(root + "/cluster_"+str(k)+"_association.csv", "r+");
sortedFrequentDoc = open(root + "/sorted_cluster_"+str(k)+"_association.csv", 'w+');

freq = csv.reader(frequentDoc);
sortedFreq = csv.writer(sortedFrequentDoc);
rows = list(freq);
length = len(rows);
startIndex = 0;
endIndex = 1;
print length;
while  endIndex < length:
    print endIndex
    line_1 = rows[startIndex];
    supp_1 = line_1[1];
    rule_1 = line_1[0];
    line_2 = rows[endIndex];
    supp_2 = line_2[1];
    rule_2 = line_2[0];
    if supp_1 == supp_2:
        endIndex = endIndex + 1;
    if supp_1 > supp_2 or endIndex == length :
        a =[];
        for row in range(startIndex, endIndex):
            rule = str(rows[row][0])
            a.append(rule)
        b = sorted(a, lambda x, y: -1 if len(x) > len(y) else 1 if len(x) < len(y) else 0)
        for i in range(len(b)):
            sortedFreq.writerow([b[i]])
        
        startIndex = endIndex
        endIndex = startIndex + 1
print "end"            
frequentDoc.close();
sortedFrequentDoc.close()
