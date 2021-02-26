# Assignment 3 - Sentiment Analysis
This repository contains all of the code and results related to Assignment 3 for Language Analytics.
The data used is a csv file containing 1.000.000 headlines from news articles. The data can be retrieved from Kaggle: https://www.kaggle.com/therohk/million-headlines

The script sentiment.py takes a path to the data directory and the filename of the csv file as inputs.
The outputs of the script are two png files that display the plots of the smoothed sentiment scores for the headlines with a rolling average of 1 week and 1 month, respectively.

__Parameters:__ <br>
```
    path: str <path-to-dir> 
    filename: str <filename-of-csv> 
```
    
__Usage:__ <br>
```
    sentiment.py -p <path-to-dir> -f <filename-of-csv>
```
    
__Example:__ <br>
```
    $ python3 sentiment.py -p ../data/ -f abcnews-date-text.csv
```

For running the code install relevant dependencies in a virtual environment. Remember to move to the correct directory in which you saved the bash script, then execute this code in the terminal:
```bash
$ bash ./create_sentiment_venv.sh
```

After creating the environment, you have to activate it. And then you can run the script with the dependencies:
```
$ source sentiment_environment/bin/activate
$ cd /<directory_of_the_python_script>/
$ python3 sentiment.py -p path2directory -f filename
```
The resulting csv file will appear in the current directory.

__To test the script I recommend uncommenting line 96 to make the script only run on a subset of the data (otherwise it will run for a few hours...).__
