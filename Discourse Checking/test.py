# coding=utf-8
from nltk import *
from nltk.sem import logic
logic._counter._value = 0

dt = DiscourseTester(['a boxer walks', 'every boxer chases a girl'])

####test1
##print dt.sentences()

####test2
####We might also want to check what grammar the DiscourseTester is
####using (by default, book_grammars/discourse.fcfg)
##print dt.grammar() # doctest: +ELLIPSIS

######test3
##print dt.readings()


######test4
######iven that each sentence is two-ways ambiguous
######we potentially have four different discourse 'threads',
######taking all combinations of readings.
##print dt.readings(threaded=True)


######test5
######Checking Consistency
##print dt.models()

######test6
######add another sentence
##dt.add_sentence('John is a boxer')
##print dt.sentences()
##print dt.readings()

####test7
##dt = DiscourseTester(['A student dances', 'Every student is a person'])
##print dt.add_sentence('No person dances', consistchk=True)
####So let's retract the inconsistent sentence:
##print dt.retract_sentence('No person dances', verbose=True)
####We can now verify that result is consistent.
##print dt.models()
####Checking Informativity
##print dt.add_sentence('A person dances', informchk=True)
####In fact, we are just checking whether the new sentence is entailed by the preceding discourse
##print dt.models()

######test8
######Adding Background Knowledge
##dt = DiscourseTester(['Vincent is a boxer', 'Fido is a boxer', 'Vincent is married', 'Fido barks'])
##print dt.readings()
######This gives us a lot of threads:
##print dt.readings(threaded=True)
######We can eliminate some of the readings, and hence some of the threads,
######by adding background information.
##import nltk.data
##bg = nltk.data.load('grammars/book_grammars/background.fol')
##dt.add_background(bg)
##print dt.background()
######The background information allows us to reject three of the threads
####as inconsistent.
##print dt.readings(filter=True)

######test9
######In order to play around with your own version of background knowledge,
######you might want to start off with a local copy of background.fol:
######将背景信息文件保存到本地
##nltk.data.retrieve('grammars/book_grammars/background.fol')

####test10加载本地背景信息文件
from nltk.inference.discourse import parse_fol
mybg = parse_fol(open('background.fol').read())







