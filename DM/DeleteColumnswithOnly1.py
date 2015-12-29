'''
Created on Nov 27, 2015

@author: apple
'''
import csv,numpy
root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/submit"
afterPruning = open(root + "/pruned.csv", "w+")
csvfile_doc_words = open(root + "/MatrixFormData.csv", 'r+');

reader = csv.reader(csvfile_doc_words)
x = list(reader);
result = numpy.array(x)
print result.shape
data =result[1:,:].astype(int)
print data.shape
columns_to_keep = numpy.sum(data, axis = 0) > 2
print columns_to_keep
# Prepending True means you keep the first column
new_data = result[:, columns_to_keep]
print new_data.shape

writer = csv.writer(afterPruning);
for i in range(302):
    writer.writerow(new_data[i,:])
