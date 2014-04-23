# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')


######正则表达式标注器,20%正确
##patterns = [
##    (r'.*ing$', 'VBG'),# gerunds

##    (r'.*ed$', 'VBD'),# simple past
##    (r'.*es$', 'VBZ'),
# 3rd singular present
##    (r'.*ould$', 'MD'),# modals
##    (r'.*\'s$', 'NN$'),
# possessive nouns
##    (r'.*s$', 'NNS'),
# plural nouns
##    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
##    (r'.*', 'NN') # nouns (default)
##]
##regexp_tagger = nltk.RegexpTagger(patterns)
##print regexp_tagger.tag(brown_sents[3])
##regexp_tagger.evaluate(brown_tagged_sents)


##查找标注器的性能,使用不同大小的模型
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Perfor mance')
    pylab.show( )


display()





