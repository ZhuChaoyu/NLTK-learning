# coding=utf-8

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import sys
import urllib2
 

##with open('sample.txt', 'r') as f:
##    text = f.read()
##
##stemmer = PorterStemmer()
##
##tokenizer = WordPunctTokenizer()
##tokens = tokenizer.tokenize(text)
##
####http://nltk.googlecode.com/svn/trunk/doc/howto/collocations.html
##bigram_finder = BigramCollocationFinder.from_words(tokens)
##bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)##给出500个得分最高的关联word对
########from nltk.metrics.association import BigramAssocMeasures
########    @classmethod
########    def chi_sq(cls, *marginals):
########        """Scores ngrams using Pearson's chi-square as in Manning and Schutze
########        5.3.3.
########        """
########        cont = cls._contingency(*marginals)
########        exps = cls._expected_values(cont)
########        return sum((obs - exp) ** 2 / (exp + _SMALL)
########                   for obs, exp in zip(cont, exps))
##
######将word对存成空格隔开的字符串
##for bigram_tuple in bigrams:
##    x = "%s %s" % bigram_tuple
##    print x


def get_feature(word):
    return dict([(word, True)])
print get_feature('a')


