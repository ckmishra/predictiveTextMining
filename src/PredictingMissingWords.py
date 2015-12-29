#===============================================================================
# '''
# Created on Nov 24, 2015
# 
# @author: apple
# '''
# import csv
# document = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/cluster_1.csv", 'r+');
# frequentDoc = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final/dummy_xls.csv";
# documentReader= csv.reader(document);
# 
# freq = open(frequentDoc,'r+');
# for row in csv.reader(freq):
#     print row
#  
# import xlrd
# xl_workbook = xlrd.open_workbook(frequentDoc)
# xl_sheet = xl_workbook.sheet_by_index(0)
# mapping ={}
# for outerRow in documentReader:
#     docId = outerRow[0];
#     words=outerRow[1:]
#     for k in range(1,41):
#         row = xl_sheet.row(k)[0]
#         lhs = str(row.value).strip("\{\}").split(',')
#         row = xl_sheet.row(k)[1]
#         rhs = str(row.value).strip("\{\}").split(',')
#         flag = set(lhs).issubset(words);
#         if flag :
#             
#             if (docId) in mapping.keys():
#                 existing = mapping.get(docId)
#                 if rhs[0] not in existing :
#                     existing.append(rhs[0])
#             else:
#                 mapping[docId]=rhs
#             if (len(mapping.get(docId))==5) :
#                 break;
#             
# print len(mapping),"\n",mapping
# 
# finalResult = open("/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/doc_1_cluster.txt", 'w+');
# for key in mapping:
#         missingValues = mapping.get(key);
#         finalResult.write("%s" % key);
#         for item in missingValues:
#             finalResult.write(",%s" % item);
#         finalResult.write("\n");
#===============================================================================