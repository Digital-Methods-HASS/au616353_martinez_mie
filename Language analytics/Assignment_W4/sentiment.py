#!/usr/bin/env python
"""
Specify directory of file and filename of a csv file containing headlines from news articles, calculate sentiment scores for each headline, smooth the sentiment scores using a rolling average over one week and month, respectively. Save output plots as png.
Parameters:
    path: str <path-to-image-dir>
    filename: str <filename-of-csv-file>
Usage:
    sentiment.py -p <path-to-directory> -t <filename-of-csv>
Example:
    $ python3 sentiment.py -p ../data/ -f abcnews-date-text.csv
## Task
- Calculate sentiment scores and save plot of smoothed sentiments using a rolling average over one week and month as png file.
"""

# importing libraries
import os
import pandas as pd
import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
import matplotlib.pyplot as plt
import argparse

# initialise spacy 
nlp = spacy.load("en_core_web_sm")



# define a rolling mean plotting function
def smoothed_plot(rolling_df, days_for_window):
    
    """ 
    Function to make the plot of the smoothed sentiment scores using a rolling average over a specified number of days.
    
    Parameters:
        rolling_df: dataframe <dataframe-with-sentiment-scores-and-dates>
        days_for_window: int <number-of-days>
        
    """

    # defining a string with converted days into either a week if 7 days is specified
    if days_for_window == 7:
        time = "one week"
        save_time = "week"
    # or a month if 30 days is specified
    elif days_for_window == 30:
        time = "one month"
        save_time = "month"
    # else just keep number of days
    else:
        time = days_for_window + " days"
        save_time = days_for_window + "_days"
    
    # defining the smoothed sentiment scores from the dataframe with date as index
    # and define the number of days for calculating the rolling average
    smoothed_df = rolling_df.rolling(f"{days_for_window}d").mean()
    
    # Plotting the smoothed sentiment scores
    plt.figure()
    # adding title
    plt.title(f"Sentiment over time with a {time} rolling average")
    # adding x-label
    plt.xlabel("Date")
    # rotating x-labels for visibility
    plt.xticks(rotation=45)
    # adding y-label
    plt.ylabel("Sentiment score")
    # plotting with label 
    plt.plot(smoothed_df, label = f"{time} rolling average")
    # using label as legend in the upper right corner
    plt.legend(loc="upper right")
    # saving plot as week_sentiment in current working directory
    plt.savefig(f'{save_time}_sentiment.png', bbox_inches='tight')
    print(f"Plot '{save_time}_sentiment.png' is saved in current directory")

    
    
# Define main function
def main():
    
    # argparse 
    ap = argparse.ArgumentParser()
    # adding arguments
    ap.add_argument("-p", "--path", required = True, help= "Path to directory of csv-file")
    ap.add_argument("-f", "--filename", required = True, help= "Filename of the csv file containing headers")
    # parsing arguments
    args = vars(ap.parse_args())
    
    # get path to image directory
    path = args["path"]
    # get name of the target image
    filename = args["filename"]
    
    # read file as a pandas data frame
    in_file = os.path.join(path, filename)
    data = pd.read_csv(in_file)
    
    # take a subset
    # data = data[:50000]
    
    # add spacy text blob to nlp pipeline
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    
    # Making an empty list for the sentiment scores
    sentiment_scores = []
    
    # Looping over each headline and extracting a polarity score (using a batch size of 500 to increase speed).
    for doc in nlp.pipe(data["headline_text"], batch_size = 5000):
        sentiment = doc._.sentiment.polarity
        # appending the score to the empty list
        sentiment_scores.append(sentiment)
    
    # Adding the scores to the dataframe by inserting it as the last column in the dataframe 
    # (specified with the length of the number of columns)
    data.insert(len(data.columns), "sentiment", sentiment_scores)

    # Defining a new dataframe that holds the publish date as the index (formatted as a date) and sentiment scores
    rolling_data = pd.DataFrame({"sentiment": sentiment_scores}, 
                            index = pd.to_datetime(data["publish_date"], format='%Y%m%d', errors='ignore'))
    
    # Plot and save the smoothed sentiment with a rolling average across a week (using the smoothed_plot function defined above)
    smoothed_plot(rolling_data, 7)

    # Plot and save the smoothed sentiment with a rolling average across a month
    smoothed_plot(rolling_data, 30)
    
    
    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()