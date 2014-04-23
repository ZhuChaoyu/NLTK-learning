# coding=utf-8
import nltk

##载入你自己的语料库
from nltk.corpus import PlaintextCorpusReader

corpus_root = '/Users/JuneMAC/Desktop/NLTK-learning/corpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print wordlists.fileids()

print wordlists.words('sample.txt')

print len(wordlists.words('sample.txt'))



