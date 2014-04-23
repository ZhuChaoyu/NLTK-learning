# coding=utf-8

##参考http://n0b3l1a.blogspot.sg/2009/10/wordnet-verbnet-via-python-nltk.html

######WordNet as thesaurus
##from nltk.corpus import wordnet as wn
##print set([s.name.split('.')[0] for s in wn.synsets('trade') if s.name.find(".v.") != -1])

####VerbNet
##from nltk.corpus import verbnet
##print verbnet.classids('drink')
####['eat-39.1-2']
##v=verbnet.vnclass('39.1-2')
##print [t.attrib['type'] for t in v.findall('THEMROLES/THEMROLE/SELRESTRS/SELRESTR')]
####['comestible', 'solid']
##print [t.attrib['type'] for t in v.findall('THEMROLES/THEMROLE')]
####['Patient']


