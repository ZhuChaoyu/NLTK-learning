# coding=utf-8
import nltk
from nltk.collocations import *

####Overview

##nltk.corpus.genesis.words('english-web.txt')根据语料提取单词表list，有重复

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
     nltk.corpus.genesis.words('english-web.txt'))##找出有关联的词对
print type(finder)
##finder.nbest(bigram_measures.pmi, 10)  
