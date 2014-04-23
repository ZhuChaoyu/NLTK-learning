# coding=utf-8
import nltk
from nltk import load_parser


##with open('sample.txt', 'r') as f:
##    sample = f.read()

##parser = load_parser('grammars/book_grammars/drt.fcfg', logic_parser=nltk.DrtParser())

dt = nltk.DiscourseTester(['A student dances', 'Every student is a person'])

print dt.readings()

print dt.add_sentence('No person dances', consistchk=True)
print dt.retract_sentence('No person dances', verbose=True)
print dt.add_sentence('A person dances', informchk=True)

##sL = sample.split('\n')
##for sl in sL:
####    print sl
##    for sent in nltk.sent_tokenize(sl):
##        print sent
##        try:
##            trees = parser.nbest_parse(sent.split())
##            print trees[0].node['SEM'].simplify()
##        except Exception as err:
##            print 'err'
