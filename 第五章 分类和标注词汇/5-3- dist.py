# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

####自从Python2.5以来,一种特殊的称为defaultdict的字典已经出现
##pos = nltk.defaultdict(lambda: 'N')
##pos['colorless'] = 'ADJ'
##print pos['blog'] 

##############################
####颠倒字典
##counts = nltk.defaultdict(int)
##for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
##    counts[word] += 1
##print [key for (key, value) in counts.items() if value == 32]

######下一个例子演示了用键-值对初始化字典pos的另一种方式
##pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
##pos2 = dict((value, key) for (key, value) in pos.items())
##print pos2['N']
####使用字典的update()方法加入再一些词到pos中
##pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
####print pos
####pos2 = nltk.defaultdict(list)
####for key, value in pos.items():
####    pos2[value].append(key)
####print pos2['ADV']
####可以使用NLTK中的索引支持更容易的做同样的事
##pos2 = nltk.Index((value, key) for (key, value) in pos.items())
##print pos2['ADV']
##############################


