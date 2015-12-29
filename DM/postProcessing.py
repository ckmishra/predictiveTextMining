'''
Created on Nov 24, 2015

@author: apple
'''
root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final";
cluster_1_doc = open(root + "/doc_1_cluster.txt", 'r+');
cluster_2_doc = open(root + "/doc_2_cluster.txt", 'r+');
cluster_3_doc = open(root + "/doc_3_cluster.txt", 'r+');
cluster_4_doc = open(root + "/doc_4_cluster.txt", 'r+');

resultDoc = open(root + "/301280815.txt", 'w+');
for line in cluster_1_doc.readlines():
    resultDoc.write(line);
for line in cluster_2_doc.readlines():
    resultDoc.write(line);
for line in cluster_3_doc.readlines():
    resultDoc.write(line);
for line in cluster_4_doc.readlines():
    resultDoc.write(line);
resultDoc.close()
cluster_1_doc.close();
cluster_2_doc.close()
cluster_3_doc.close()
cluster_4_doc.close()