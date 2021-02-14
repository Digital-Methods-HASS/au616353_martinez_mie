#!/usr/bin/env python
# coding: utf-8

# In[ ]:
__name__ = "__main__"

def tokenize(input_string):
    # Split at all characters except for letters (both lowercase and uppercase) and apostrophes
    tokenizer = re.compile(r"[^a-zA-Z']+") 
    # Tokenize
    token_list = tokenizer.split(input_string) # return a token list by splitting the input string using the compiling pattern
    # Return list of tokens
    return token_list

def collocates(path, keyword, window_size):
    # Defining empty list for all tokens (individual words) 
    token_list_all = []
    # Defining empty list for holding collocates
    collocates_list = []
    # Creating empty data frame
    data = pd.DataFrame(columns=["keyword", "collocate", "raw_frequency", "MI"])
    # Setting u to 0 
    u = 0 # this will be used to keep track of number of occurrences of keyword during the first loop
    
    # For loop going over all files in the path for the corpus 
    for filename in Path(path).glob("*.txt"):
        # opening and reading the file
        with open (filename, "r", encoding = "utf-8") as file:
            text = file.read()
            # creating a temporary list of lowercase words from the text corpus using the tokenize function
            token_list = tokenize(text.lower())
            # Appending the temporary token_list to a list containing all tokens from all files
            token_list_all.extend(token_list)
            # Finding the index for all occurrences of the keyword
            indices = [index for index, x in enumerate(token_list) if x == keyword]
            # Adding the number of keywords to the keyword count (u)
            u = u + len(indices)
            
            # For loop going over all occurrences of the keyword
            for index in indices:
                # Defining the window start
                window_start = max(0, index - window_size) # if index - window_size is a negative value, it will be 0.
                # Defining the window end
                window_end = index + window_size
                # Finding the tokens that surround the keyword
                keyword_string = token_list[window_start : window_end + 1] # adding 1 to the right side as python doesn't include the last index
                # Adding the keyword string to the list of collocates 
                collocates_list.extend(keyword_string)
                # Removing the keyword from the list of collocates
                collocates_list.remove(keyword)
                
    # Calculating collocate frequency and mutual information (MI)    
    # List of unique collocates
    unique_collocates = set(collocates_list)
    # For loop for unique collocates
    for collocate in unique_collocates:
        # Calculating v - all occurrences of collocate in corpus
        v = token_list_all.count(collocate)
        # Calculating O11 - all occurrences of collocate as a collocate
        O11 = collocates_list.count(collocate)
        # Calculating O12 - occurrences of keyword without collocate
        O12 = u - O11
        # Calculating O21 - occurrences of collocate without keyword
        O21 = v - O11
        # Calculating R1 - observed frequency of O11 and O12
        R1 = O11 + O12
        # Calculating C1 - observed frequency of O11 and O21
        C1 = O11 + O21
        # Calculating N - number of words in corpus 
        N = len(token_list_all)
        # Calculating E11 - expected frequency of keyword and collocate
        E11 = R1*C1/N
        # Calculating MI - mutual information, association measure of keyword and collocate
        MI = np.log(O11/E11)
        # Appending data to data frame
        data = data.append({"keyword": keyword, 
                     "collocate": collocate, 
                     "raw_frequency": O11,
                     "MI": MI}, ignore_index = True)
    # Sorting the MI values in ascending order so the collocate with highest correlation to the keyword is shown in the top of the data frame    
    data = data.sort_values("MI", ascending = False)
    # Returning data frame
    return data

def main():
    # Defining the path to the corpus - This can be changed to any available corpus 
    path = os.path.join("..", "data", "100_english_novels", "test_corpus")

    # Running the collocates function on the specified path using the keyword "he" and a window_size of 2.
    collocates_df = collocates(path, "he", 2)
    # Saving the collocates data frame to csv
    collocates_df.to_csv("Collocates.csv", index = False)


# Define behaviour when called from command line
if __name__=="__main__":
    import os
    import sys 
    sys.path.append(os.path.join("..")) # enabling communication with home directory
    import pandas as pd 
    from pathlib import Path
    import csv 
    import re
    import string
    import numpy as np
    main()

