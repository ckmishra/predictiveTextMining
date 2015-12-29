'''
Created on Nov 20, 2015

@author: chandan
'''
import csv
import numpy, random


def main():
    root = "/Users/apple/SFU_Term1_Materials/DM/Project/ProjectData/cluster/predict/final"
    collabration_doc = open(root + "/Collaboration.txt", "r+")
    csvfile_doc_words = open(root + "/pruned.csv", 'r+');
    reader = csv.reader(csvfile_doc_words)
    x = list(reader);
    result = numpy.array(x[1:]).astype('int')
    
    num_rows, num_cols = result.shape;
    print num_rows, num_cols;
    
    # preparing collab matrix
    collab = {}
    for row in csv.reader(collabration_doc):
        if len(row) == 0 : 
            break
        collab[row[-1]] = [row[0], row[1]];
        
    # selecting initial seed points
    k = 4;  # number of cluster
    num_iteration = 20;  # number of iteration
    initial = random.sample(result, k)
    initial = numpy.array(initial)
    mu = [initial[0][1:], initial[1][1:], initial[2][1:], initial[3][1:]];
    # Create k clusters using those centroids
    while num_iteration > 0:
        num_iteration = num_iteration - 1;
        misclassification = 0
        clusters_k = [[], [], [], []]
        for i in range(num_rows):
            item = result[i];
            # before appending check
            item_doc_id = result[i, 0];
            doc_members = collab.get(str(item_doc_id));
            # print item
            distance = distanceComputation(item, mu);
            clusters = dict(zip(distance, clusters_k));
            # sort by distance
            distance.sort();
            for dist in distance :
                selectedCluster = clusters.get(dist);
                clustermembers = []
                for clusterItem in selectedCluster:
                    members = collab.get(str(clusterItem[0]));
                    for m in members :
                        clustermembers.append(m);
                        
                commonElement = list(set(doc_members).intersection(clustermembers))
                if len(commonElement) == 0:
                    selectedCluster.append(item)
                    break;
                # not in any cluster than put in minimum distance
                if dist == distance[-1] :
                    misclassification = misclassification + 1;
                    selectedCluster = clusters.get(distance[0]);
                    selectedCluster.append(item)
        # update seed
        mu_1 = numpy.array(clusters_k[0])[:, 1:].mean(axis=0)
        mu_2 = numpy.array(clusters_k[1])[:, 1:].mean(axis=0)
        mu_3 = numpy.array(clusters_k[2])[:, 1:].mean(axis=0)
        mu_4 = numpy.array(clusters_k[3])[:, 1:].mean(axis=0)
        mu = [mu_1, mu_2, mu_3, mu_4]

    cluster_ids = []
    for i in range(k):
            cluster_ids.append(numpy.array(clusters_k[i])[:, 0].tolist());
    for n in range(k):
        print len(clusters_k[n]), cluster_ids[n];
    
    print "misclassification ", misclassification
    
    
    # writing to final result
    finalResult = open(root + "/clustering.txt", 'w+');
    for i in range(k):
        for m in cluster_ids[i]:
            finalResult.write("%s,%d\n" % (m, i + 1));
    
    # clustering 
    document = open(root + "/DocumentWords.txt", 'r+');
    cluster_doc_1 = open(root + "/cluster_1.csv", 'w+');
    cluster_doc_2 = open(root + "/cluster_2.csv", 'w+');
    cluster_doc_3 = open(root + "/cluster_3.csv", 'w+');
    cluster_doc_4 = open(root + "/cluster_4.csv", 'w+');
    
    reader = csv.reader(document);
    for row in reader :
        doc_id = int(row[0]);
        del row[1]  # deleting unique
        if doc_id in cluster_ids[0]:
            writer = csv.writer(cluster_doc_1);
            writer.writerow(row);
        elif doc_id in cluster_ids[1] :
            writer = csv.writer(cluster_doc_2);
            writer.writerow(row);
        elif doc_id in cluster_ids[2] :
            writer = csv.writer(cluster_doc_3);
            writer.writerow(row);
        elif doc_id in cluster_ids[3] :
            writer = csv.writer(cluster_doc_4);
            writer.writerow(row);
            
# distance function          
def distanceComputation(item, mu):
            dist1 = numpy.linalg.norm(item[1:] - mu[0]);  # ignoring doc id
            dist2 = numpy.linalg.norm(item[1:] - mu[1]);
            dist3 = numpy.linalg.norm(item[1:] - mu[2]);
            dist4 = numpy.linalg.norm(item[1:] - mu[3]);
            return [dist1, dist2, dist3, dist4];
        
if __name__ == '__main__':
        main()
