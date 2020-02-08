#!/usr/bin/env python

"""mapper.py"""

import sys

trend_words = ["president", "house", "report", "mueller", "democrats", "campaign", "pete", "candidate", "people", "barr"]

for line in sys.stdin:
    line = line.strip()
    words = line.split() 
    for i in range(len(words)):
        for j  in range(i+1, len(words)):
            if words[i] == words[j]: continue
            if words[i] in trend_words or words[j] in trend_words:
                print "%s&%s\t%s" % (words[i],words[j], 1)