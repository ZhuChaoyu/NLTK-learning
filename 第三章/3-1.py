# coding=utf-8
##from __future__ import division
import nltk,re,pprint

####编号2554的文本是《罪与罚》的英文翻译
##from urllib import urlopen
##
##url = "http://gutenberg.org/files/2554/2554.txt"
##
##raw = urlopen(url).read()
##
##print raw[:75]
##
##
##tokens = nltk.word_tokenize(raw)
##print type(tokens)
##print len(tokens)
##
##text = nltk.Text(tokens)
##print type(text)
##
##print text.collocations()


######nltk用来练习正则的工具
##nltk.app.nemo()


with open('sample3-1.txt', 'r') as f:
    sample = f.read()

tokens = nltk.word_tokenize(sample)
text = nltk.Text(tokens)


######规范化小写
##set(w.lower() for w in text)

####词干提取
##porter = nltk.PorterStemmer()##porter提取器
##print [porter.stem(t) for t in tokens]
##lancaster = nltk.LancasterStemmer()##lancaster提取器
##print [lancaster.stem(t) for t in tokens]

######使用词干提取器索引文本
##class IndexedText(object):
##    def __init__(self,stemmer,text):
##        self._text = text
##        self._stemmer = stemmer
##        self._index = nltk.Index((self._stem(word),i)
##                                 for (i,word) in enumerate(text))
##    def concordance(self,word,width=40):
##        key = self._stem(word)
##        wc = width/4   ##words of context
##        for i in self._index[key]:
####            print i
##            if i<wc:
##                lcontext = ' '.join(self._text[0:i])
##            else:
##                lcontext = ' '.join(self._text[i-wc:i])
##            if i+wc >= len(self._text):
##                rcontext = ' '.join(self._text[i:])
##            else:
##                rcontext = ' '.join(self._text[i:i+wc])
##            ldisplay = '%*s' % (width,lcontext[-width:])
##            rdisplay = '%-*s' % (width,rcontext[:width])
##            print ldisplay,rdisplay
##    def _stem(self,word):
##        return self._stemmer.stem(word).lower()
##
##porter = nltk.PorterStemmer()
##rr = IndexedText(porter,text)
##print rr.concordance('attack')

####词形归并
####wordNet词形归并器删除词缀产生的词都是在他的字典中的词
wnl = nltk.WordNetLemmatizer()
print [wnl.lemmatize(t) for t in tokens]



####html解析工具介绍
##import feedparser
##
##llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
##
##print llog[feed][title]
