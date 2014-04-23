# coding=utf-8
##from __future__ import division
import nltk
import re,pprint

##用正则表达式为文本分词

#########
##raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
##though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
##well without--Maybe it's always pepper that makes people hot-tempered,'
##"""
##print raw
##
##print re.split(r' ', raw)
##print re.split(r'[ \t\n]+', raw) 
###########

###########
####text = 'That U.S.A. poster-print costs $12.40...'
##with open('sample3-1.txt', 'r') as f:
##    text = f.read()
##
##pattern = r'''(?x)      # set flag to allow verbose regexps
##    ([A-Z]\.)+
         # abbreviations, e.g. U.S.A.
##    | \w+(-\w+)*
   
   # words with optional internal hyphens
##    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
##    | \.\.\.           # ellipsis
##    | [][.,;"'?():-_`] # these are separate tokens
##'''
##
##r = nltk.regexp_tokenize(text, pattern)
####r = nltk.word_tokenize(text)
####print r
##
##r = nltk.pos_tag(r)####将每个单词标注词性，返回多个list
####    print r
##r = nltk.ne_chunk(r)####输入标注好词性的List，返回多个<class 'nltk.tree.Tree'>
##print r
##for chunk in r:
####        print chunk
##    if hasattr(chunk, 'node'):
####            print chunk.leaves()[0][0]
##        print chunk.node, ' '.join(c[0] for c in chunk.leaves())
###########


###########
fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in fdist:
    print word, '->', fdist[word], ';',
###########



##a = 'tim and Tom & june'
##
##print re.split(r' and | & ',a)
####>>['tim', 'Tom', 'june']

