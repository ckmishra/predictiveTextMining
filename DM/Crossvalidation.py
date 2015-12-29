'''
Created on Dec 1, 2015

@author: apple
'''
import csv, numpy
from _csv import reader


root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/submit"
cv = open(root + "/301280815.txt", "r+")
for i in range(1,11):
    print i
    IndexArray = [True]*301;
    IndexArray[(i-1)*30:30*i] =[False]*30;
    cv_modified = open(root + "/301280815_cv" + str(i) + ".txt", "w+")
    reader = csv.reader(cv)
    x = list(reader);
    result = numpy.array(x).astype('int')
    print result.shape
    print numpy.where(IndexArray)[0]
    initial = numpy.array(result[numpy.where(IndexArray)[0],:])
    print initial.shape
    writer = csv.writer(cv_modified);
    for item in initial:
        writer.writerow(item);
    cv.seek(0);
