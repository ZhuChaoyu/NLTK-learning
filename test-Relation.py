# coding=utf-8
import nltk
from nltk.data import load
import os
import sys 
##reload(sys) 
##sys.setdefaultencoding('utf8')
import pickle

##tagger = pickle.load(open("/Users/JuneMAC/nltk_data/taggers/treebank_brill_aubt/treebank_brill_aubt.pickle"))


def addEM(EntityMap,emkey,Name,Etype,loc):
    emkey += 1
    EntityMap[emkey] = {'Name':Name,'e-type':Etype,'Loc':loc}
    return (emkey,EntityMap)

def relation(atype,btype,middleMap):
    if middleMap == {}:
        return 'null'
    else:
        relation = ''
        verbTag = []
        inTag = []
        for key in sorted(middleMap.keys()):
    ##        print middleMap[key][1]
    ##        print middleMap[key][0]
            ttag = middleMap[key][1]
            if ttag[:2]=='VB':
                if verbTag ==[]:
##            if ttag in ['VBD','VBN','VB','VBZ']:
                    verbTag = [middleMap[key][0]]
            if ttag in ['IN','OF']:
                if len(verbTag)==1 and middleMap[key][0]!='of':
                    verbTag += [middleMap[key][0]]
                else:
                    if len(inTag)<2:
                        inTag += [middleMap[key][0]]
        if len(verbTag) > 0:
            for word in verbTag:
                relation += word + ' '
        else:
            for word in inTag:
                relation += word + ' '
        if relation.strip()=='':
            return 'null'
        else:
            return relation.strip()

def getBeginIndex(d):
    if d - 10<1:
        return 1
    else:
        return (d-10)

def getEndIndex(d,total):
    if d + 10 > total -1:
        return (total - 1)
    else:
        return (d + 10)


def getRelation(inputString,relationFileName,pMap):
    
    j = 0
    mmap = {}
    emKey = 0
    EntityMap = {}
    test = 0
    
    
    sample = inputString

    for sent in nltk.sent_tokenize(sample):####将一段语料拆成各个句子，返回list
    ##    print sent
        r = nltk.word_tokenize(sent)####将每句话拆分成单词，返回多个list
    ##    print r
        r = nltk.pos_tag(r)####将每个单词标注词性，返回多个list
##        r = tagger.tag(r)
    ##    print r
        r = nltk.ne_chunk(r)####输入标注好词性的List，返回多个<class 'nltk.tree.Tree'>
        for chunk in r:
            if hasattr(chunk, 'node'):
                j += 1
                EntityType = chunk.node
                EntityName = ' '.join(c[0] for c in chunk.leaves())
                mmap[j] = (EntityName,EntityType)
                (emKey,EntityMap) = addEM(EntityMap,emKey,EntityName,mmap[j][1],j)
            else:
                word = chunk[0]
                cx = chunk[1]
                j += 1
                mmap[j] = (word,cx)
                if cx in ['.',':']:
                    if not (EntityType=='separator' and EntityMap[emKey]['e-type']=='separator'):
                        (emKey,EntityMap) = addEM(EntityMap,emKey,word,'separator',j)

##    ##输出文本map观察
##    for i in sorted(mmap.keys()):
##        print '%d\t%s' % (i,mmap[i])
##
##    ##输出实体MAP观察
##    for key in sorted(EntityMap.keys()):
##        print '%d\t%s' % (key,EntityMap[key])

    for index in sorted(EntityMap.keys()):       
        if index < len(EntityMap) and EntityMap[index]['e-type'] != 'separator' :
            if EntityMap[index+1]['e-type'] != 'separator' :
                middle = {}
                for Hindex in range(EntityMap[index]['Loc']+1,EntityMap[index+1]['Loc']):
                     middle[Hindex] = mmap[Hindex]
##                print middle
                rules = relation(EntityMap[index]['e-type'],EntityMap[index+1]['e-type'],middle)
##                if rules!='null':
                if rules!='null' and ((EntityMap[index]['Name'] in pMap) or (EntityMap[index+1]['Name'] in pMap)):
                    pl1 = '%s:%s\t%s\t%s:%s' % (EntityMap[index]['e-type'],EntityMap[index]['Name'],rules, \
                                            EntityMap[index+1]['e-type'],EntityMap[index+1]['Name'])
##                    print rules
##                    print pl1
                    pl = ''
                    bindex = getBeginIndex(EntityMap[index]['Loc'])
                    eindex = getEndIndex(EntityMap[index]['Loc'],len(mmap))
                    for Hindex in range(bindex,eindex):
                        pl += mmap[Hindex][0] + ' '
##                    print pl.strip()
                    outputFile = open(relationFileName,'a')
                    outputFile.write('%s\t%s\n' % (pl1,pl))
                    outputFile.close()


