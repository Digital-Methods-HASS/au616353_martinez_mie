#!/usr/bin/env python
# coding: utf-8

# ## Assignment 1 - Basic scripting with Python

# __Using the corpus called 100-english-novels found on the cds-language GitHub repo, write a Python programme which does the following:__
# - Calculate the total word count for each novel
# - Calculate the total number of unique words for each novel
# - Save result as a single file consisting of three columns: filename, total_words, unique_words

# __Importing libraries and data__

# In[43]:


import os
from pathlib import Path
import pandas as pd # This is used to make the dataframe
import numpy as np # This is used for unique word count

# defining path to corpus
corpus_path = os.path.join("..", "data", "100_english_novels", "corpus")


# __Making the dataframe__ <br>
# _A for loop is made to iterate over each file in the path that ends in .txt. Then these are read into the loop to count total words and total unique words._ <br>
# _Lastly, these are saved to an empty dataframe._

# In[44]:


# making an empty dataframe using pandas
word_count_df = pd.DataFrame(columns = ['filename', 'total_words', 'unique_words'])

# for loop to split and count words
for filename in Path(corpus_path).glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        loaded_text = file.read()
        # split on whitespaces
        split_text = loaded_text.split()
        # save word count
        total_words = len(split_text)
        # count unique words with numpy
        values, unique = np.unique(split_text, return_counts=True)
        unique_words = len(unique)
        # saving the filename, total_words and unique_words in a temporary dataframe (this will be overwritten by new iteration)
        temp_df = ({'filename': filename, 'total_words': total_words, 'unique_words': unique_words})
        # appending the temporary dataframe to the empty dataframe
        word_count_df = word_count_df.append(temp_df, ignore_index=True)


# In[46]:


print(dataframe)


# _Printing the dataframe, we see that there are 100 rows (corresponding to number of novels) and 3 columns (holding filename, total_words and unique_words)._

# __Saving the dataframe__

# In[47]:


# defining the path for results
path2results = os.path.join("..", "data", "100_english_novels", "word_count_df.csv")
# saving the dataframe as csv file
word_count_df.to_csv(path2results)


# In[ ]:




