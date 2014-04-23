# coding=utf-8
from nltk.corpus import conll2000


print conll2000.chunked_sents('train.txt')[99]


print conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99]


