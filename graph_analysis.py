import snap
import argparse
import numpy as np
import networkx as nx
from itertools import permutations
from matplotlib import pyplot as plt
import glob, os

def load_graph(filename):
    Graphtype = nx.Graph()
    G = nx.read_edgelist(filename, create_using=Graphtype, nodetype=int)
    return G

def analyze(filename, G):
    # f = open("analysis.txt", "a")
    f = open("analysis_wo_centrality.txt", "a")
    f.write("Analyze file: %s\n" % filename)

    num_nodes = G.number_of_nodes()
    print "Num Nodes: %d" % num_nodes
    f.write("Num Nodes: %d\n" % num_nodes)

    num_edges = G.number_of_edges()
    print "Num Edges: %d" % num_edges
    f.write("Num Edges: %d\n" % num_edges)

    average_clustering = nx.average_clustering(G)
    print "Average Clustering Coefficient: %f" % average_clustering
    f.write("Average Clustering Coefficient: %f\n" % average_clustering)

    pagerank = nx.pagerank(G)
    print "Pagerank: %f" % avg_of_dict(pagerank)
    f.write("Pagerank: %f\n" % avg_of_dict(pagerank))

    number_connected_components = nx.number_connected_components(G)
    print "Number of Connected Components: %d" % number_connected_components
    f.write("Number of Connected Components: %d\n" % number_connected_components)

    degree_centrality = nx.degree_centrality(G)
    print "Average Degree Centrality: %f" % avg_of_dict(degree_centrality)
    f.write("Average Degree Centrality: %f\n" % avg_of_dict(degree_centrality))

    # Closeness takes a while
    # closeness_centrality = nx.closeness_centrality(G)
    # print "Average Closeness Centrality: %f" % avg_of_dict(closeness_centrality)
    # f.write("Average Closeness Centrality: %f\n" % avg_of_dict(closeness_centrality))

    # betweenness_centrality = nx.betweenness_centrality(G, k=min(5000, num_nodes))
    # print "Average Betweenness Centrality: %f" % avg_of_dict(betweenness_centrality)
    # f.write("Average Betweenness Centrality: %f\n" % avg_of_dict(betweenness_centrality))

    neighbor_degree = nx.average_neighbor_degree(G)
    print "Average Neighbor Degree: %f" % avg_of_dict(neighbor_degree)
    f.write("Average Neighbor Degree: %f\n" % avg_of_dict(neighbor_degree))

    degree_list = [val for (node, val) in G.degree()]
    print "Average Degree: %f" % avg_of_list(degree_list)
    f.write("Average Degree: %f\n" % avg_of_list(degree_list))

    print "Standard Deviation of Degree: %f" % np.std(degree_list)
    f.write("Standard Deviation of Degree: %f\n" % np.std(degree_list))

    f.write("End of %s\n\n" % filename)
    f.close()

def avg_of_dict(dict):
    return sum(dict.itervalues())/float(len(dict))

def avg_of_list(list):
    return sum(list)/float(len(list))

    ##########################################################################

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename", help="edge list file name")
    # args = parser.parse_args()

    # G = load_graph(args.filename)
    os.chdir(".")
    for file in glob.glob("*.txt"):
        if file == "analysis.txt" or file == "analysis_wo_centrality.txt":
            continue
        print(file)
        G = load_graph(file)
        analyze(file, G)
    # analyze(G)
