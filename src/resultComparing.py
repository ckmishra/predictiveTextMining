'''
Created on Nov 21, 2015

@author: apple
'''
import csv
from _sqlite3 import Row


collabration_doc = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/Collaboration_1.csv", "rU")
result_em = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/em_result.csv", "rU");

cluster0 = []
cluster1 = []
cluster2 = []
cluster3 = []
for row in csv.reader(result_em) : 
     if row[-1] == 'cluster0' :
        cluster0.append(row[1]);
     elif row[-1] == 'cluster1' :
        cluster1.append(row[1]);
     elif row[-1] == 'cluster2' :
        cluster2.append(row[1]);
     elif row[-1] == 'cluster3' :
        cluster3.append(row[1]);


#print cluster0;  
#print cluster1;   
#print cluster2;   
#print cluster3;    

collab = {}
for row in csv.reader(collabration_doc):
    if len(row) ==0 : 
        break
    if row[0] in collab.keys():
        collab.get(row[0]).append(row[-1]);
    else :
        collab[row[0]] = [row[-1]];
    if row[1] in collab.keys():
        collab.get(row[1]).append(row[-1]);
    else :
        collab[row[1]] = [row[-1]];

for i in collab:
    print i , collab.get(i) 
#print len(collab)
miscalsification = 0;
for key, value in collab.iteritems():
    #print value;
    t1 = set(value).intersection(set(cluster0))
    t2 = set(value).intersection(set(cluster1))
    t3 = set(value).intersection(set(cluster2))
    t4 = set(value).intersection(set(cluster3))
    result =[t1,t2,t3,t4]
    miscalsification = miscalsification + result.count(set([]));
    
#print miscalsification;
    
