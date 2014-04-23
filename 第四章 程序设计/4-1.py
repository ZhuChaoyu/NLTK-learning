# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

##for item in s 遍历 s 中的元素
##for item in sorted(s) 按顺序遍历 s 中的元素
##for item in set(s) 遍历 s 中的无重复的元素
##for item in reversed(s) 按逆序遍历 s 中的元素
##for item in set(s).difference(t) 遍历在集合 s 中不在集合 t 的元素
##for item in random.shuffle(s) ####按随机顺序遍历 s 中的元素
##要获得无重复的逆序排列的 s 的元素,可以使用 reversed(sorted(set(s)))。


####Python 有序列处理函数,如 sorted()和 reversed(),它们重新 排列序列中的项目
####zip()取两 个或两个以上的序列中的项目,将它们“压缩”打包成单个的配对链表。
####给定一个序列 s, enumerate(s)返回一个包含索引和索引处项目的配对。
##words = ['I', 'turned', 'off', 'the', 'spectroroute','off']
##tags = ['noun', 'verb', 'prep', 'det', 'noun','prep']
##print zip(words, tags)
##print list(enumerate(words))


######让我们综合关于这三种类型的序列的知识,一起使用链表推导处理一个字符串中的词,按它们的长度排序
##words = 'I turned off the spectroroute'.split()
##wordlens = [(len(word), word) for word in words]
##wordlens.sort()
##print ' '.join(w for (_, w) in wordlens)

######lambda表达式
##sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',
##        'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
##print sorted(sent, lambda x, y: cmp(len(y), len(x)))##逆序


########参数的命名
######我们可以定义一个函数,接受任意数量的未命名和命名参数,并通过一个就地的参数链表
######*args和一个就地的关键字参数字典**kwargs来访问它们
######当*args作为函数参数时,它实际上对应函数所有的未命名参数。
##song = [['four', 'calling', 'birds'],
##        ['three', 'French', 'hens'],
##        ['two', 'turtle', 'doves']]
##print zip(song[0], song[1], song[2])
##print zip(*song)
######应该从这个例子中明白输入*song仅仅是一个方便的记号,
######相当于输入了song[0],song[1],song[2]


####可以使用变量__file__定 位你的系统中任一NLTK模块的代码
##print nltk.metrics.distance.__file__
####nltk.metrics.distance.__file__


##递归
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial2(n-1)

print factorial2(3)








