"""
Pre-Processing Text Data:
>> Cleaning up the text data by removing punctuation, stop words, and stemming
>> Removing stop words and stemming
"""

import pandas as pd
import string
import re

dataSet = pd.read_csv("Natural-Language-Processing/data/SMSSpamCollection.tsv", sep='\t', header=None)
dataSet.columns = ['label', 'message']

def remove_punct(text):
    textCleaned = "".join([char for char in text if char not in string.punctuation])
    return textCleaned

dataSet['cleaned'] = dataSet['message'].apply(lambda x: remove_punct(x))
print(dataSet.head())