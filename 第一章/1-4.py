# coding=utf-8


from nltk.book import *

print len(text1)

print len(set(text1))

print len(set([word.lower() for word in text1]))

##由于我们不重复计算像This和this这样仅仅大小写不同的词
##就已经从词汇表 计数中抹去了2,000个!
##还可以更进一步,通过过滤掉所有非字母元素,从词汇表中消除数字和标点符号。

print len(set([word.lower() for word in text1 if word.isalpha()]))

