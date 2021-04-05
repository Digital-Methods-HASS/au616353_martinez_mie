# Assignment 5 - (Un)supervised machine learning
For this assignment, I chose to examine the development of topics depicted in Donald Trump's tweets. For this, I found a dataset on Kaggle (https://www.kaggle.com/codebreaker619/donald-trump-tweets-dataset).
The tweets are from around 2011 (with a few tweets from 2009 and 2010) to the beginning of 2021.
I wanted to see if it was possible to train a model that could detect a development in trends that Trump wrote about. <br>

__Preprocessing__ <br>
The preprocessing steps can be seen in the script under the class methods ```load_and_prepare()``` and ```process_data()```.
In the former, I filtered away all tweets containing hyperlinks as these would have added noise to the data. Similarly, I removed all retweets, as I am only interested in the topics that Trump formulated on his own. This was fairly easy as the dataset had a column for whether the tweet was a retweet. <br>
Following this, I appended all tweets to a single list.
In the latter method, I build models for bigrams and trigrams and fitted these to the data. Furthermore, the words were lemmatized and part of speech tagging was performed keeping only nouns and verbs. This was done using the method ```process_words()```  from the utils script lda_utils.py.

I didn't have much time to play around with it too much so there might be more optimal ways/combinations for examining the tweets. 
However, to my opinion the best results were yielded when looking at nouns and verbs and setting number of topics to 10. <br>

When examining the outputs do note that the numbering of topics differ between the html and the png file. 
To examine the png file, I therefore suggest that you cross reference with the topics printed in the terminal. <br>


__Results__ <br>
When looking at the three most dominant topics (topics 1-3 in the html file), the topics that Trump has been most occupied with seems to be about the elections, 
making America great again (or at least "make" and "success" are words included in the topic), and immigration and crime.
This lines up with my expectation and knowledge about Trump and his agenda as a politician. <br>
I think using both nouns and verbs gave me the most clearly defined topics. In contrast, I also tried using adjectives and adjectives and nouns as well as just nouns. <br>
As I wanted to examine the development of topics, I created a lineplot with a rolling mean using seaborn. 
For this, 10 topics gave the most clear visibility as 15-20 topics made it almost impossible to make inferences about how the topics were distinct across time.
Looking at the plot in the png file, it is evident that the dominant topics are 2, 5 and 7. 
When looking at the print of topics in the terminal, it becomes evident that these topics are about running for president, 
deals and trades, and his political campaign, respectively. So, the development goes from being about Trump running for president for the first time, 
to being more about him doing different trades and deals and generally about his political work as a president (supported by topic 4). 
Then, when approaching the presidential campaign in 2020, the topics occupying his twitter switch to be about running for president again.
It should however be noted that the topic for running from president differ slightly from the first to the second time as these are represented by different feature spaces (2 and 7). <br>

__Further research__ <br>
I didn't have as much time as I would have wished, so there are of course some flaws in this work. If I were to take these results further I would start by cleaning 
the data even more so occurrences like "realdonaldtrump" and "foxnews" were maybe less prominents as these are not directly adding anything meaningful to the topics. 
Furthermore, some of the verbs are also not adding much to the meaning of the topics and could be seen as redundant. 

It would be interesting to run the model with fourgrams as well as bi- and trigrams as this might catch phrases like "make America great again". <br>

