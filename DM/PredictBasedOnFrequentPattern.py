
import csv
root="/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/Frequent"
k=1
document = open(root+"/cluster_"+str(k)+".csv", 'r+');
frequentDoc = open(root+"/cluster_"+str(k)+"_association.csv","r+");
finalResult = open(root+"/doc_"+str(k)+"_cluster.txt", 'w+');

documentReader = csv.reader(document);
freq = csv.reader(frequentDoc);
 
mapping = {}
for outerRow in documentReader:
    docId = outerRow[0];
    words = outerRow[1:]
    print docId,words
    for row in freq :
        item = row[0].strip("\{\}");
        flag = item in words;
        print flag
        if not(flag) :
            if docId in mapping.keys():
                existing = mapping.get(docId);
                if (len(existing) == 5) :
                    break;
                if item not in existing :
                    existing.append(item)
            else:
                mapping[docId] = [item];
        
    frequentDoc.seek(0);      
print len(mapping), "\n", (mapping)
for key in (mapping):
    missingValues = mapping.get(key);
    finalResult.write("%s" % key);
    for item in missingValues:
        finalResult.write(",%s" % item);
    finalResult.write("\n");
document.close();
frequentDoc.close();
finalResult.close();
