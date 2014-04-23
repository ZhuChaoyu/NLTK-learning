#!/usr/bin/env python -*- coding: utf-8 -*-

bank_sents = ['I went to the bank to deposit my money',
'The river bank was full of dead fishes','The seats of my lousy Chevy are actually great',
              'The height of the bicycle seat is adjustable']

plant_sents = ['The workers at the industrial plant were overworked',
'The plant was no longer bearing flowers']

##print "======== TESTING simple_lesk ===========\n"
##from lesk import simple_lesk

##print "#TESTING simple_lesk() ..."
##print "Context:", bank_sents[0]
##answer = simple_lesk(bank_sents[0],'bank')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "#TESTING simple_lesk() with POS ..."
##print "Context:", bank_sents[2]
##answer = simple_lesk(bank_sents[2],'seat','n')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "#TESTING simple_lesk() with POS and stems ..."
##print "Context:", plant_sents[0]
##answer = simple_lesk(plant_sents[0],'plant','n', True)
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "======== TESTING adapted_lesk ===========\n"
####from myAdaptedLesk import adapted_lesk
##from lesk import adapted_lesk
##
##print "#TESTING adapted_lesk() ..."
##print "Context:", bank_sents[0]
##answer = adapted_lesk(bank_sents[0],'bank','n')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "======== TESTING cosine_lesk ===========\n"
##from lesk import cosine_lesk
##
##print "#TESTING cosine_lesk ..."
##print "Context:", bank_sents[2]
##answer = cosine_lesk(bank_sents[2],'great','s')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "======== TESTING baseline ===========\n"
##from baseline import random_sense, first_sense
##from baseline import max_lemma_count as most_frequent_sense

##print "#TESTING random_sense() ..."
##print "Context:", bank_sents[0]
##answer = random_sense('bank')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "#TESTING first_sense() ..."
##print "Context:", bank_sents[2]
##answer = first_sense('seat')
##print "Sense:", answer
##print "Definition:",answer.definition
##print

##print "#TESTING most_frequent_sense() ..."
##print "Context:", bank_sents[2]
##answer = most_frequent_sense('great')
##print "Sense:", answer
##print "Definition:",answer.definition
##print
