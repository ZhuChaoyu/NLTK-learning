# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

#############################
######表示已标注的标识符
####str2tuple
####一个已标注的标识符使用一个由标识符和标记组成的元组来表示
####我们可以使用函数 str2tuple()从表示一个已标注的标识符的标准字符串创建一个这样的特殊元组
##tagged_token = nltk.tag.str2tuple('fly/NN')
##print tagged_token
##sent = '''
##The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
##other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
##Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PP
##said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/R
##accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
##interest/NN of/IN both/ABX governments/NNS ''/'' ./.
##'''
##print [nltk.tag.str2tuple(t) for t in sent.split()]
#############################

#############################
######读取已标注的语料库
##print nltk.corpus.brown.tagged_words()
##print nltk.corpus.brown.tagged_words(simplify_tags=True)##简化的标记集
##
####可以使用这些标记做强大的搜索,结合一个图形化的POS一致性工具
####用它来寻找任一词和POS标记的组合
##nltk.app.concordance()
#############################

#############################
##探索已标注的语料库

#############################
