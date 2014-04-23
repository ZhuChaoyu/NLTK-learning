# coding=utf-8

##saying = ['After', 'all', 'is', 'said', 'and', 'done',
##          'more', 'is', 'said', 'than', 'done']
##
##print saying
##tokens = set(saying)
##print tokens
##tokens = sorted(tokens)
##print tokens
##print tokens[-2:]


from nltk.book import *

##fdist1 = FreqDist(text1)
##vocabulary1 = fdist1.keys()
##
##print vocabulary1[:50]
##
##print fdist1['whale']
##
####《白鲸记》中 50 个最常用词的累积频率图,这些词占了所有标识符的将近一半
##fdist1.plot(50, cumulative=True)
##
####查看低频词
##a = len(fdist1.hapaxes())
##print type(fdist1.hapaxes())
##print fdist1.hapaxes()[a-10:]
##
####查看长词
##V = set(text1)
##long_words = [w for w in V if len(w) > 15]
##print sorted(long_words)
##
####聊天语料库中所有长度超过 7 个字符出现次数超过 7 次的词
##fdist5 = FreqDist(text5)
##print sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])

##词语搭配和双连词( bigrams)
##要获取搭配,我们先从提取文本词汇中的词对也就是双连词开始
print bigrams(['more', 'is', 'said', 'than', 'done'])
##在这里我们看到词对than-done是一个双连词,在Python中写成('than','done')
##除非我们更加注重包含不常见词的的情况,搭配基本上就是频繁的双连词
##我们希望找到比我们基于单个词的频率预期得到的更频繁出现的双连词。
##collocations()函数为我 们做这些
print text4.collocations()
print text8.collocations()

####NLTK频率分布类中定义的函数
##fdist = FreqDist(samples) ##创建包含给定样本的频率分布
##fdist.inc(sample) ##增加样本
##fdist['monstrous' ] ##计数给定样本出现的次数
##fdist.freq('mons trous')##给定样本的频率
##fdist.N() ##样本总数
##fdist.keys( ) ##以频率递减顺序排序的样本链表
##for sample in fdist: ##以频率递减的顺序遍历样本
##fdist.max() ##数值最大的样本
##fdist.tabulate() ##绘制频率分布表
##fdist.plot() ##绘制频率分布图
##fdist.plot(cumulative=True) ##绘制累积频率分布图
##fdist1 < fdist2 ##测试样本在 fdist1 中出现的频率是否小于 fdist2

####my example
##saying = ['After', 'all', 'is', 'said', 'and', 'done',
##          'more', 'is', 'said', 'than', 'done']
##fdist1 = FreqDist(saying)
##print fdist1['said']


