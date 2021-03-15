# Assignment 4 - Network Analysis
This repository contains all of the code and data related to Assignment 4 for Language Analytics.
In the data folder there is a csv file with a weighted edgelist containing the headers "nodeA", "nodeB" and "weight". 
The output of the python script is also provided in the viz and output folders, containing a network visualization and dataframe with centrality measures, respectively.

The script network.py is in the src and it takes the filepath to a csv and an integer as input. Optionally, you can add whether you want labels on your graph or not.
The output of the script is a png file of the network graph and a csv file of the centrality measures. <br>
__Parameters:__ <br>
```
    input_file: str <filepath-of-csv-file>
    weight_threshold: int <filtering-threshold>
    labels: str <True-or-None>
```
    
__Usage:__ <br>
```
    network.py -f <filepath-of-csv-file> -w <filtering-threshold> -l <True-or-None>
```
    
__Example:__ <br>
```
    $ python3 network.py -f ../data/weighted_edgelist.csv -w 500 -l True
```

To ensure dependencies are in accordance with the ones used for the script, you can create the virtual environment "network_environment" by running the bash script create_network_venv.sh
```
    $ bash ./create_sentiment_venv.sh
```
After creating the environment, you have to activate it. And then you can run the script with the dependencies:
```
    $ source network_environment/bin/activate
    $ cd src
    $ python3 network.py -f ../data/weighted_edgelist.csv -w 500 -l True
```
The outputs will appear in the output and viz folder.
