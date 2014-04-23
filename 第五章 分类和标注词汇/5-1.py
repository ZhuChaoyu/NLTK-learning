# coding=utf-8
##from __future__ import division
import nltk
import re,pprint


####查看词性标签的具体含义
##print nltk.help.upenn_tagset('NNP')
##print nltk.help.upenn_brown_tagset('NN.*')


##考虑下面的分析,涉及woman(名词),bought(动词),over(介词)和 the(限定词)
##text.similar()方法为一个词w找出所有上下文w1ww2
##然后找出所有出现在相同上下文中的词w',即w1w'w2
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print text.similar('woman')
print text.similar('bought')
print text.similar('over')
print text.similar('the')
##一个标注器也可以为我们对未知词的认识过程建模;
##例如:我们可以根据词根scrobble猜测scrobbling可能是一个动词,
##并有可能发生在he_was_scrobbling这样的上下文中。



