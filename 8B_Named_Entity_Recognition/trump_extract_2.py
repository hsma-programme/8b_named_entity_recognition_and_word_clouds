#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:23:22 2020

@author: dan
"""

# import spacy and the downloaded en_core_web_sm pre-trained model
import spacy
import en_core_web_sm

# Load the pre-trained model as a language model into a variable called nlp
nlp = en_core_web_sm.load()

# Read in the document for which we want to extract named entities
with open("TrumpArticle.txt", encoding='utf8') as f:
    # Read in the whole file as a single string but strip out any whitespace at
    # the start and end of the file
    raw_read = f.read().strip()
    
# Apply the pre-trained model to the raw text string to extract named entities
# All of SpaCy's predictions (including the named entity predictions) are
# stored as a Doc object.  Here, we call our Doc object 'article', but you
# may also see it commonly named 'doc'.
article = nlp(raw_read)

# Store the Named Entity categories (stored in label_ for each entity) in the 
# article in a list. The named entities themselves are stored in article.ents
labels = [x.label_ for x in article.ents]

# Print each predicted named entity, along with its predicted category
for i in range(len(article.ents)):
    print (f"{article.ents[i]} : {labels[i]}")

# Use displaCy to visualise the predicted named entities
spacy.displacy.serve(article, style="ent")

# Use displaCy to visualise the parsed dependencies in the text
#spacy.displacy.serve(article, style="dep")

# Use displaCy to visualise the parsed dependecies sentence by sentence
#sentences = list(article.sents)
#spacy.displacy.serve(sentences, style="dep")

