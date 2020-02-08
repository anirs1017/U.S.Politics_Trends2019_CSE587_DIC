# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 12:20:33 2019

@author: shash
"""

#!/usr/bin/env python
"""mapper.py"""

import sys

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

with open(r'C:\Users\shash\OneDrive\Desktop\DIC\Lab2\sdhar2Lab2\Part1\Data\CommonCrawl\data-CC-clean.txt', modew, encoding= "Latin-1" ,**kwargs) as fw:
    with open(r'C:\Users\shash\OneDrive\Desktop\DIC\Lab2\sdhar2Lab2\Part1\Data\CommonCrawl\data-CC.txt', moder, encoding= "Latin-1" , **kwargs) as fr:
        # next(reader, None)  # skip the headers
        for row in fr:
            # remove leading and trailing whitespace
            line = row.strip()
            # split the line into words
            words = tokenizer.tokenize(line)
            # increase counters
            sentence = ""
            for word in words:
                if not word.lower() in stop_words:
                    lemword = lemmatizer.lemmatize(word)  
                    sentence += lemword + " "
            fw.write(sentence + "\n")
                
         
    
            