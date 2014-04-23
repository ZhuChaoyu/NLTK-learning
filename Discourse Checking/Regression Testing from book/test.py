# coding=utf-8
import nltk
import pickle
from nltk import *
from nltk.sem import logic


######test1
##logic._counter._value = 0
##
##from nltk.tag import RegexpTagger
##tagger = RegexpTagger(
##    [('^(chases|runs)$', 'VB'),
##     ('^(a)$', 'ex_quant'),
##     ('^(every)$', 'univ_quant'),
##     ('^(dog|boy)$', 'NN'),
##     ('^(He)$', 'PRP')]) 
##
##rc = DrtGlueReadingCommand(depparser=MaltParser(tagger=tagger))
##dt = DiscourseTester(map(str.split, ['Every dog chases a boy', 'He runs']), rc)
##print dt.readings()
##print dt.readings(show_thread_readings=True)


######test2
##logic._counter._value = 0
##from nltk.parse import FeatureEarleyChartParser
##from nltk.sem.drt import DrtParser
##grammar = nltk.data.load('grammars/book_grammars/drt.fcfg', logic_parser=DrtParser())
##parser = FeatureEarleyChartParser(grammar, trace=0)
##trees = parser.nbest_parse('Angus owns a dog'.split())
##print(trees[0].node['SEM'].simplify())



######test3
##logic._counter._value = 0
##
##with open('sample.txt', 'r') as f:
##    sample = f.read()
##sL = sample.split('\n')
##sLL = []
##for sl in sL:
####    print sl
##    for sent in nltk.sent_tokenize(sl):
##        try:
##            sLL += [sent]
##        except Exception as err:
##            print 'err'
##
####for s in sLL:
####    print s
##
##testL = sLL[-2:]
##
##tagger = pickle.load(open("/Users/JuneMAC/nltk_data/taggers/brown_simplify_tags/brown_simplify_tags.pickle"))

##patterns = []
##for sent in testL:
##    r = nltk.word_tokenize(sent)
##    r = nltk.pos_tag(r)
##    patterns += r
##
##print patterns

from nltk.tag import RegexpTagger
##patterns = [
##    ('^Musharraf$', 'NNP'),
##    ('^Chak$', 'NNP'),
##    ('^AFIC$', 'NNP'),
##    ('^Shahzad$', 'NNP'),
##    
##    ('^(have|has)$', 'VBZ'),
##    ('^been$','VBN'),
##    ('^.*ed$', 'VBN'),
##    ('^(from|after)$','IN'),
##    ('^to$','TO'),
##    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
##    ('^(every)$', 'univ_quant'),
##    ('^(a)$', 'ex_quant'),
##]

##tagger = RegexpTagger(
##    [('^(chases|runs)$', 'VB'),
##     ('^(a)$', 'ex_quant'),
##     ('^(every)$', 'univ_quant'),
##     ('^(dog|boy)$', 'NN'),
##     ('^(He)$', 'PRP')]) 
####<class 'nltk.tag.sequential.RegexpTagger'>
##tagger = RegexpTagger(patterns)

rc = DrtGlueReadingCommand(depparser=MaltParser(tagger=tagger))
####rc -- <class 'nltk.inference.discourse.DrtGlueReadingCommand'>
dt = DiscourseTester(map(str.split, testL), rc)
print dt.readings()

##print dt.readings(show_thread_readings=True)


