# coding=utf-8
import nltk
from nltk.tag.stanford import NERTagger

st = NERTagger('/Users/JuneMAC/nltk_data/taggers/stanford/all.3class.distsim.crf.ser.gz',
               '/Users/JuneMAC/nltk_data/taggers/stanford/stanford-ner.jar')
               
##test1 - sucess
with open('sample.txt', 'r') as f:
    sample = f.read()

for sent in nltk.sent_tokenize(sample):
    r = nltk.word_tokenize(sent)
    r = st.tag(r)
    for s in r:
        if s[1]!='O':
            print s
