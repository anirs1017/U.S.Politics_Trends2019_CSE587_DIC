# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 12:20:33 2019

@author: shash
"""

#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

import nltk
nltk.data.path.append("/usr/share/nltk_data")

from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english')) 

from nltk.stem import WordNetLemmatizer

from nltk.tokenize import RegexpTokenizer
  
lemmatizer = WordNetLemmatizer()

# Write CSV file
kwargs = {'newline': ''}
modew = 'w'
moder = 'r'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    modew = 'wb'
    mode = 'rb'

tokenizer = RegexpTokenizer(r'\w+')

with open(r'C:\Users\shash\OneDrive\Desktop\DIC\Lab2\sdhar2Lab2\Part1\Data\Twitter\data-topic6-clean.csv', modew, encoding = "Latin-1", **kwargs) as fw:
    writer = csv.writer(fw)
    with open(r'C:\Users\shash\OneDrive\Desktop\DIC\Lab2\sdhar2Lab2\Part1\Data\Twitter\data-topic6.csv', moder, encoding = "Latin-1", **kwargs) as fr:
        reader = csv.reader(fr)
        # next(reader, None)  # skip the headers
        for row in reader:
            if len(row):
                # remove leading and trailing whitespace
                line = row[0].strip()
                # split the line into words
                words = tokenizer.tokenize(line)
                # increase counters
                sentence = ""
                for word in words:
                    if not word.lower() in stop_words:
                        lemword = lemmatizer.lemmatize(word)  
                        sentence += lemword + " "
                writer.writerow([sentence])
         
    
            