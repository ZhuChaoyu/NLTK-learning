# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

######一元标注(Unigram Tagging)
######一元标注器基于一个简单的统计算法:对每个标识符分配这个独特的标识符最有可能的标记
####不分离训练和测试数据
####unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
####print unigram_tagger.tag(brown_sents[2007])
####print unigram_tagger.evaluate(brown_tagged_sents)
####分离训练和测试数据
##unigram_tagger = nltk.UnigramTagger(train_sents)
##print unigram_tagger.evaluate(test_sents)

#########n-gram标注器
####一个n-gram标注器是一个unigram标注器的一般化
####它的上下文是当前词和它前面n-1个标识符的词性标记
####1-gram 标注器是一元标注器(unigram tagger)另一个名称:
####即用于标注一个标识符的上下文的只是标识符本身。
####2-gram标注器也称为二元标注器(bigram taggers),
####3-gram标注器也称为三元标注器(trigram taggers)
##bigram_tagger = nltk.BigramTagger(train_sents)
##print bigram_tagger.tag(brown_sents[2007])
##unseen_sent = brown_sents[4203]
##print bigram_tagger.tag(unseen_sent)
####请注意,bigram标注器能够标注训练中它看到过的句子中的所有词,但对一个没见过的句子表现很差。
####只要遇到一个新词(如13.5),就无法给它分配标记
####它不能标注下面的词(如:million),即使是在训练过程中看到过的,只是因为在训练过程中从来没有见过它
####前面有一个None标记的词。因此,标注器标注句子的其余部分也失败了.它的整体准确度得分非常低:
##print bigram_tagger.evaluate(test_sents)


#############组合标注器
####1.尝试使用 bigram 标注器标注标识符。
####2.如果bigram 标注器无法找到一个标记,尝试unigram标注器
####3.如果unigram 标注器也无法找到一个标记,使用默认标注器。
##t0 = nltk.DefaultTagger('NN')
##t1 = nltk.UnigramTagger(train_sents, backoff=t0)
##t2 = nltk.BigramTagger(train_sents, backoff=t1)
##print t2.evaluate(test_sents)
##    ###########存储标注器
##from cPickle import dump
##output = open('t2.pkl', 'wb')
##dump(t2, output, -1)
##output.close()
##    ###########载入我们保存的标注器
##from cPickle import load
##input = open('t2.pkl', 'rb')
##tagger = load(input)
##input.close()
##text = """
##The board's action shows what free enterprise
##is up against in our complex maze of regulatory laws.
##"""
##tokens = text.split()
##print tagger.tag(tokens)

###########性能限制
####下面这段代码计算有多少单词存在词性奇异现象
cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in brown_tagged_sents
    for x, y, z in nltk.trigrams(sent))
ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()
##说明1/20的trigrams是有歧义的
##根据训练数据,在5%的情况中,有一个以上的标记可能合理地分配给当前词。
##假设我们总是挑选在这种含糊不清的上下文中最有可能的标记,可以得出trigram标注器性能的一个下界。






