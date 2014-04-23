# coding=utf-8
import nltk
from nltk.data import load

##test1 - sucess
with open('sample.txt', 'r') as f:
    sample = f.read()

##sample = 'He was taken to hospital on January 02 as he suffered a "heart problem" when he was on his way to appear before the special court hearing treason case against him.'
for sent in nltk.sent_tokenize(sample):####将一段语料拆成各个句子，返回list
##    print sent
    r = nltk.word_tokenize(sent)####将每句话拆分成单词，返回多个list
##    print r[32:33]
##    print r
    r = nltk.pos_tag(r)####将每个单词标注词性，返回多个list
##    print r
    r = nltk.ne_chunk(r)####输入标注好词性的List，返回多个<class 'nltk.tree.Tree'>
    for chunk in r:
##        print chunk
        if hasattr(chunk, 'node'):
##            print chunk.leaves()[0][0]
            print chunk.node, ' '.join(c[0] for c in chunk.leaves())

####test2 -
##_MULTICLASS_NE_CHUNKER = 'chunkers/maxent_ne_chunker/english_ace_multiclass.pickle'
##chunker_pickle = _MULTICLASS_NE_CHUNKER
##chunker = load(chunker_pickle)
##cor = [chunker._parse_to_tagged(s) for s in corpus]


     
##sentences = nltk.sent_tokenize(sample)
##tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
##tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
##chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
##
##print chunked_sentences
## 
##def extract_entity_names(t):
##    entity_names = []
##    
##    if hasattr(t, 'node') and t.node:
##        if t.node == 'NE':
##            entity_names.append(' '.join([child[0] for child in t]))
##        else:
##            for child in t:
##                entity_names.extend(extract_entity_names(child))
##                
##    return entity_names
## 
##entity_names = []
##for tree in chunked_sentences:
##    # Print results per sentence
##    # print extract_entity_names(tree)
##    
##    entity_names.extend(extract_entity_names(tree))
## 
### Print all entity names
###print entity_names
## 
### Print unique entity names
##print set(entity_names)


##def extract_entities(text):
##     for sent in nltk.sent_tokenize(text):
##         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
##             if hasattr(chunk, 'node'):
##                 print chunk.node, ' '.join(c[0] for c in chunk.leaves())
##
##
##
##print extract_entities(sample)



