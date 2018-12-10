#File to generate the snap.py graphs; however, the input txt files already are the set of edges.
#This file merely constructs the graph.
import datetime as dt
import json
import snap
import os

dirname = 'QuarantinedPairsNormal'
dirnamenew = 'QuarantinedGraphsNormal'
for root, dirs, files in os.walk(dirname):
    for filename in files:
        if filename[-9:] != "pairs.txt":
            continue
        print(filename)
#files = [f for f in os.listdir('NonQuarantinedPairsNormal/') if os.path.isfile(f)]
#print(len(files))
        fil = open(dirname + "/" + filename, 'r')
        print(dirname+"/"+filename)
        stringid_to_intid = {}
        ids = []
        num_nodes = 0
        for line in fil:
            comment = line[:-1]
            ids.append(comment)
        G = snap.PUNGraph.New()

        for i in range(int(len(ids) / 2)):
            comment_id = ids[i*2]
            parent_id = ids[i*2+1]
            #print("Comment id is %s and parent id is %s" % (comment_id, parent_id))

            if not parent_id in stringid_to_intid:
                stringid_to_intid[parent_id] = num_nodes
                G.AddNode(num_nodes)
                num_nodes += 1
            if not comment_id in stringid_to_intid:
                stringid_to_intid[comment_id] = num_nodes
                G.AddNode(num_nodes)
                num_nodes += 1
            id1 = stringid_to_intid[parent_id]
            id2 = stringid_to_intid[comment_id]
            G.AddEdge(id1, id2)
            #print("Author is %s \n Id is %s \n Parent Id is %s \n Body is %s \n " % (cache[i].author, cache[i].id, s, cache[i].body))
        snap.SaveEdgeList(G, dirnamenew + "/" + filename[0:-9] + "Graphs.txt")

#print(stringid_to_intid['Jon_Tren_Yin'])
