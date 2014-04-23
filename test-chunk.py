# coding=utf-8
import nltk

sent = 'The seats of my lousy Chevy are actally great'

r = nltk.word_tokenize(sent)
r = nltk.pos_tag(r)
print r

##grammar = r"""
##  
##  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
##      {<NNP>+}                # chunk sequences of proper nouns
##  GP:{<IN>?<PRP\$>?<NN><NNP>+}
##"""
grammar = r"""
  NP: {<DT|PP\$|PRP\$>?<JJ>?<NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><RB>?<NP|PP|JJ|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
"""


cp = nltk.RegexpParser(grammar)
result = cp.parse(r)
print result
result.draw()

