# Assignment 5 - (Un)supervised machine learning
This repository contains all of the code and data related to Assignment 5 for Language Analytics.
For a write-up of the results, see RESULTS.md. <br>

In the data folder there is a csv file with tweets from Trumps twitter account up until he was banned in the beginning of 2021. 
The output of the python script is also provided in the data folder in the created output folder. This contains a visualization of the created topics saved as an interactive html file.
Furthermore, the scripts creates a lineplot that illustrates Trumps development of topics across time. This is saved as a png file.

The script development_of_trump.py is in the src and it takes the filepath to a csv as input. Optionally, you can define the filename of the lineplot, the number of topics and the types of words you wish to examine.
If nothing is chosen for the three parameters, defaults are set instead. <br>
__Parameters:__ <br>
```
    input_file: str <filepath-of-csv-file>
    output_filename: str <name-of-png-file>, default = "trumps_development.png"
    n_topics: int <number-of-topics>, default = 15
    word_types: list <list-of-word-types>, default = "NOUN"
```
    
__Usage:__ <br>
```
    development_of_trump.py -f <filepath-of-csv-file> -o <name-of-png-file> -n <number-of-topics> -w <list-of-word-types>
```
    
__Example:__ <br>
```
    $ python3 development_of_trump.py -f ../data/Trump_tweets.csv -o trumps_development.png -n 15 -w "['NOUN', 'VERB']"
```

To ensure dependencies are in accordance with the ones used for the script, you can create the virtual environment "classifier_venv" by running the bash script create_classify_venv.sh
```
    $ bash ./create_classify_venv.sh
```
After creating the environment, you have to activate it. And then you can run the script with the dependencies:
```
    $ source classifier_venv/bin/activate
    $ cd src
    $ python3 development_of_trump.py -f ../data/Trump_tweets.csv -o trumps_development.png -n 10 -w "['NOUN', 'VERB']"
```
The outputs will appear in the output folder in data.
