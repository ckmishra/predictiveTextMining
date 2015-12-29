
import csv
root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/submit";
k = 4;
#for i in range(1,k+1) :
num = 4;
document = open(root + "/cluster_" + str(num) + ".csv", 'r+');
frequentDoc = open(root + "/sorted_cluster_" + str(num) + "_association.csv", "r+");
finalResult = open(root + "/doc_" + str(num) + "_cluster.txt", 'w+');

documentReader = csv.reader(document);
freq = csv.reader(frequentDoc);

mapping = {}
for outerRow in documentReader:
    docId = outerRow[0];
    words = outerRow[1:]
    for row in freq :
        #print "outside";
        associationRule = row[0].split("=>");
        lhs = associationRule[0].strip("\{\} ").split(',');
        rhs = associationRule[1].strip(" \{\}").split(',');
        lhsFlag = set(lhs).issubset(words) or (len(lhs) == 0);
        rhsFlag = (set(rhs).issubset(words));
        if (not(rhsFlag) and lhsFlag) :
            #print "inside";
            if (docId not in mapping.keys()) :
                mapping[docId] = [rhs[0]]
            else :
                existing = mapping.get(docId)
                if len(existing) == 5:
                    break;
                elif rhs[0] not in existing :
                    existing.append(rhs[0])
    frequentDoc.seek(0)
print "number of docs", len(mapping), "\n", mapping

for key in sorted(mapping):
    missingValues = mapping.get(key);
    finalResult.write("%s" % key);
    for item in missingValues:
        finalResult.write(",%s" % item);
    finalResult.write("\n");
frequentDoc.close();            
document.close();
finalResult.close();