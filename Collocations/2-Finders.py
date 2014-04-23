# coding=utf-8
import nltk
from nltk.collocations import *
from nltk.corpus import stopwords

##text = "I do not like green eggs and ham, I do not like them Sam I am!"

ff = [',','(',')','-',':','the','.','"']
mm = {}
stop = stopwords.words('english')

with open('sample.txt', 'r') as f:
    text = f.read()

tokens = nltk.wordpunct_tokenize(text)
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

##3单词组
finder = TrigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(trigram_measures.raw_freq)
r = sorted((score,bigram) for bigram, score in scored)##按得分升序给出关联对
for s,(a,b,c) in  r:
    if a.isalnum() and b.isalnum() and c.isalnum():
        if a not in stop and b not in stop and c not in stop:
            print a,b,c

####2单词组
##finder = BigramCollocationFinder.from_words(tokens)
##scored = finder.score_ngrams(bigram_measures.raw_freq)
##r = sorted((score,bigram) for bigram, score in scored)##按得分升序给出关联对
##for s,(a,b) in  r:
##    if a.isalnum() and b.isalnum():
##        if a not in stop and b not in stop:
##            print s,a,b



####We could otherwise construct the collocation finder from manually-derived FreqDists:
##word_fd = nltk.FreqDist(tokens)##给出每个word在语料中出现的次数
####print word_fd
####print nltk.bigrams(tokens)##一段语料word和word两两组队以pair为元素的List输出
##bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))##计算组队的出现次数
####print bigram_fd
##finder = BigramCollocationFinder(word_fd, bigram_fd)
##print type(finder)
##print scored == finder.score_ngrams(bigram_measures.raw_freq)
##
