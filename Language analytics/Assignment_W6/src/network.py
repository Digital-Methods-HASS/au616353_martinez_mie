#!/usr/bin/env python
"""
Specify file path of a weighted edgelist as a csv file containing three columns named "nodeA", "nodeB" and "weight". Also, specify a threshold for filtering based on weight. Optionally, specify whether to include labels in visualization. Draw and save a network visualization as png in viz folder. Measure degree, betweenness and eigenvector centrality and save as a csv file in output folder.

Parameters:
    input_file: str <filepath-of-csv-file>
    weight_threshold: int <filtering-threshold>
    include_labels: str <True-or-None>
Usage:
    network.py -f <filepath-of-csv-file> -w <filtering-threshold> -l <True-or-None>
Example:
    $ python3 network.py -f ../data/weighted_edgelist.csv -w 500 -l True
    
## Task
- It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB" and "weight".
- For any given weighted edgelist given as an input, your script should be used to create a network visualization, which will be saved in a folder called viz.
- It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.
"""

# importing libraries
import os
import pandas as pd
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
import argparse
from collections import Counter
import spacy
# initialise spacy 
nlp = spacy.load("en_core_web_sm")

# argparse 
ap = argparse.ArgumentParser()
# adding argument
ap.add_argument("-f", "--input_file", required = True, help= "Path to the csv-file")
ap.add_argument("-w", "--weight_threshold", required = True, help = "Threshold for the weight included in the network")
ap.add_argument("-l", "--include_labels", required = False, help = "Set to True to include labels on the visualization")
# parsing arguments
args = vars(ap.parse_args())


def main(args):
    # get path to the csv file
    input_file = args["input_file"]
    # define and make threshold integer
    threshold = int(args["weight_threshold"])
    # define label
    labels = args["include_labels"]
    
    # Create class
    network = Network(input_file = input_file, threshold = threshold, labels = labels)
    # use method network_viz
    network.network_viz()
    # use method calc_centrality
    network.calc_centrality()


class Network:
    def __init__(self, input_file, threshold, labels):
        '''
        Constructing the Network object
        '''
        self.input_file = input_file
        self.weight_threshold = threshold
        self.labels = labels
        
    def load_and_filter(self):
        '''
        Loading the input data frame and filtering based on weight threshold.
        Returns a filtered data frame
        '''
        # read csv file
        weighted_edgelist = pd.read_csv(self.input_file)
        # filtering the weights by user defined threshold
        filtered_df = weighted_edgelist[weighted_edgelist["weight"]>self.weight_threshold]
        
        return filtered_df
    
    def network_viz(self):
        '''
        Makes a viz directory if this doesn't exist already.
        Makes a network visualization based on the filtered data frame. If labels are specified as True labels will be added for each edge
        in the network. Otherwise, these will not be included in the graph. The visualization will be saved as a png file in the viz folder.
        '''
        # Create viz directory if it doesn't exist
        dirName = os.path.join("..", "data", "viz")
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ")
        else:   
            print("Directory " , dirName ,  " already exists")
            
        # use load_and_filter function to make the filtered df
        filtered_df = self.load_and_filter()
        # suppling the edges and nodes to the graph from pandas data frame
        G = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weight"])
        # creating node positions for G using Graphviz
        pos = nx.nx_agraph.graphviz_layout(G, prog = "neato")
    
        # if user wants labels draw graph with labels and save
        if self.labels == "True":
            # drawing and saving the graph with labels
            nx.draw(G, pos, with_labels=True, node_size = 20, font_size = 10)
            plt.savefig("../data/viz/network.png", dpi = 300, bbox_inches = "tight")
            # printing that it has saved
            print("Network visualization with labels is saved in directory " , dirName)
        else:
            # drawing and saving the graph without labels
            nx.draw(G, pos, with_labels=False, node_size = 20, font_size = 10)
            plt.savefig("../data/viz/network.png", dpi = 300, bbox_inches = "tight")
            # printing that it has saved
            print("Network visualization without labels is saved in directory " , dirName)
      
    
    def calc_centrality(self):
        '''
        Makes an output directory if this doesn't already exists.
        Calculates three measures of centrality (degree, betweenness and eigenvector) and saves these in a csv file in the output folder.
        '''
        # Create output directory if it doesn't exist
        outputDir = os.path.join("..", "data", "output")
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
            print("Directory " , outputDir ,  " Created ")
        else:
            print("Directory " , outputDir ,  " already exists")
        
        # use load_and_filter function to make the filtered df
        filtered_df = self.load_and_filter()
        # suppling the edges and nodes to the graph from pandas data frame
        G = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weight"])
        
        # calculate the degree centrality and save as dataframe
        d_metric = nx.degree_centrality(G)
        degree_df = pd.DataFrame(d_metric.items(), columns = ["node", "degree"])
    
        # calculate betweenness centrality and save as dataframe
        bc_metric = nx.betweenness_centrality(G)
        between_df = pd.DataFrame(bc_metric.items(), columns = ["node", "betweenness"])
    
        # calculate eigenvector centrality
        ev_metric = nx.eigenvector_centrality(G)
        eigen_df = pd.DataFrame(ev_metric.items(), columns = ["node", "eigenvector"])
    
        # merging degree and betweenness centrality dataframes
        centrality_df = pd.merge(degree_df, between_df, on='node')
        # merging the eigenvector centrality dataframe to the previously merged dataframe
        centrality_df = pd.merge(centrality_df, eigen_df, on = 'node')
    
    
        # save centrality dataframe in output directory
        centrality_df.to_csv("../data/output/centrality_measures.csv", index = False)
        print("Centrality measures are saved as csv in " , outputDir)
        

        
if __name__ == "__main__":
    main(args)
        
        