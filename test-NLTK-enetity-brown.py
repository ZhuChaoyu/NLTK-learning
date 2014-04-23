# coding=utf-8
import nltk
import pickle
from nltk.data import load

tagger = pickle.load(open("/Users/JuneMAC/Downloads/infochimps_brown-simplifed-tags-part-of-speech-tagger-for-python-nltk/brown_simplify_tags/brown_simplify_tags.pickle"))

##test1 - sucess
with open('sample.txt', 'r') as f:
    sample = f.read()

for sent in nltk.sent_tokenize(sample):####将一段语料拆成各个句子，返回list
##    print sent
    r = nltk.word_tokenize(sent)####将每句话拆分成单词，返回多个list
##    print r
    r = tagger.tag(r)####将每个单词标注词性，返回多个list
##    print r
    r = nltk.ne_chunk(r)####输入标注好词性的List，返回多个<class 'nltk.tree.Tree'>
    for chunk in r:
##        print chunk
        if hasattr(chunk, 'node'):
##            print chunk.leaves()[0][0]
            print chunk.node, ' '.join(c[0] for c in chunk.leaves())
