#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:00:48 2020

@author: dan
"""

# You need to pip install wordcloud
from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt

# Read text in for which we want to generate word cloud
with open("wordcloud_example_text.txt", "r") as f:
    full_text = f.read()
    
# STOPWORDS has a list of common stopwords (words such as "the", "and",
# "because", "isn't" etc that we're probably not interested in here).  We'll
# take a copy of STOPWORDS (which we'll call stopwords) in case we want to
# add our own etc.  We won't here, but we need them to remain as a set.
# Note - we're just setting up the set of stopwords here, we're not removing
# them from our text yet.
stopwords = set(STOPWORDS)

# Tokenize the text (split into individual words and put them in a list - we 
# can see this if we look at the tokens list after we run this)
tokens = full_text.split()

###

# Set up a translation table that maps punctuation characters (stored in
# string.punctuation) to 'None'.  This allows us to get rid of punctuation 
# (which you'll have seen was still in the tokens list).  The maketrans()
# method of a string object takes up to three arguments.  If we supply three,
# then the characters passed in the third argument are mapped to 'None' -
# ie it gets rid of them.  So we set pass three inputs here - the first two
# we just pass empty strings (so it doesn't do anything with them), and then
# we pass string.punctuation (which contains a list of punctuation characters)
# as the third input.  It will then set up a translation table that we ca
# use to remove punctuation from text.
punctuation_mapping_table = str.maketrans('', '', string.punctuation)

# The translate() function maps one set of characters to another.  Here, we
# use that to translate tokens with punctuation to ones without punctuation
# by using the mapping table we specified above.
tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]

###

# Convert all tokens to lowercase (so we don't count capitalised words
# differently)
lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

###

# We need to put everything back into a single string of text for the word
# cloud to be generated.  Here, we just use the join function to join our
# list of cleansed words with spaces, and put them in a single string.
joined_string = (" ").join(lower_tokens)

###

# Generate a wordcloud - specify the size, background colour, and the minimum
# font size.  We also specify the set of stopwords we want excluded that we
# set up earlier.  Specify that the word cloud should be generated on our text
# string by passing that string into the generate method of WordCloud.  
# Note that the minimum font size specified will exclude words that would 
# appear smaller than this (as they are too uncommon).  So reducing minimum
# font size acts as a filter where more uncommon words are allowed in to the
# cloud.
wordcloud = WordCloud(width=1800,
                      height=1800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).generate(joined_string)

# Now we plot the wordcloud using matplotlib

# We set the size of the figure
plt.figure(figsize=(30,40))

# Turn off axes
plt.axis("off")

# Then use imshow to plot an image (here, our wordcloud)
plt.imshow(wordcloud)

# Then save the image as a png
plt.savefig("wordcloud.png")

