# coding=utf-8

import nltk
from nltk.corpus import wordnet as wn
##from nltk.corpus.wordnet import WordNetCorpusReader


##nltk.app.wordnet()

####同义词
####motorcar 只有一个可能的含义,它被定义为 car.n.01,car的第一个名词意义
##print wn.synsets('motorcar')
####car.n.01被称为synset或“同义词集”,意义相同的词(或“词条”)的集合
##print wn.synset('car.n.01').lemma_names

####同义词集中的每个词可以有多种含义,例如:car也可能是火车车厢、一个货车或电梯厢。
####但我们只对这个同义词集中所有词来说最常用的一个意义感兴趣。
####同义词集也有一些一 般的定义和例句
##
##print wn.synset('car.n.01').definition
##print wn.synset('car.n.01').examples

######WordNet使在概念之间漫游变的容易--上下层次漫游
######例如:一个如摩托车这样的概念,我们可以看到 它的更加具体(直接)的概念——下位词。
##car = wn.synset('car.n.01')
##print car
##types_of_car = car.hyponyms()
##print types_of_car
####print types_of_car[26]
####print sorted([lemma.name for synset in types_of_car for lemma in synset.lemmas])

######我们也可以通过访问上位词来浏览层次结构。
######有些词有多条路径,因为它们可以归类在一个以上的分类中。
######car.n.01与 entity.n.01之间有两条路径
####因为wheeled_vehicle.n.01 可以同时被归类为车辆和容器。
##print car.hypernyms()
##paths = car.hypernym_paths()
##print [synset.name for synset in paths[0]]
##print [synset.name for synset in paths[1]]
##print car.root_hypernyms()

######WordNet使在概念之间漫游变的容易--整体部分漫游
####例如:一棵树的部分是它的树干,树冠等;这些都是part_meronyms()
####一棵树的实质是包括心材和边材组成的,即substance_meronyms()
####树木的集合形成了一个森林,即 member_holonyms()
##print wn.synset('tree.n.01').part_meronyms()
##print wn.synset('tree.n.01').substance_meronyms()
##print wn.synset('tree.n.01').member_holonyms()


######考虑具有几个密切相关意思的词 mint
####我们可以看到mint.n.04是mint.n.02的一部分,是组成mint.n.05的材质
##for synset in wn.synsets('mint', wn.NOUN):
##    print synset.name + ':', synset.definition
##
##print wn.synset('mint.n.04').part_holonyms()
##
##print wn.synset('mint.n.04').substance_holonyms()


######动词之间也有关系。例如:走路的动作包括抬脚的动作,所以走路蕴涵着抬脚。
##print wn.synset('walk.v.01').entailments()
##print wn.synset('eat.v.01').entailments()
##print wn.synset('tease.v.03').entailments()

#######反义词
##print wn.lemma('supply.n.02.supply').antonyms()


########语义相似度
####回想一下每个同义词集都有一个或多个上位词路径连接到一个根上位词,如entity.n. 01
####连接到同一个根的两个同义词集可能有一些共同的上位词
####如果两个同义词集共用一个非常具体的上位词——在上位词层次结构中处于较低层的上位词
##它们一定有密切的联系
##right = wn.synset('right_whale.n.01')##脊美鲸
##orca = wn.synset('orca.n.01')##逆戟鲸
##minke = wn.synset('minke_whale.n.01')##小须鲸
##tortoise = wn.synset('tortoise.n.01')##乌龟
##novel = wn.synset('novel.n.01')##小说
##print right.lowest_common_hypernyms(minke)##脊美鲸和小须鲸最低一层的上位词
####[Synset('baleen_whale.n.01')]##长须鲸
##print right.lowest_common_hypernyms(orca)##脊美鲸和逆戟鲸最低一层的上位词
####[Synset('whale.n.02')]##鲸鱼
##print wn.synset('baleen_whale.n.01').lowest_common_hypernyms(orca)
##print right.lowest_common_hypernyms(tortoise)##脊美鲸和乌龟最低一层的上位词
##[Synset('vertebrate.n.01')]##脊椎动物
##print right.lowest_common_hypernyms(novel)##脊美鲸和小说最低一层的上位词
####当然,我们知道,鲸鱼是非常具体的(须鲸更是如此),脊椎动物是更一般的
####而实体完全是抽象的一般的。我们可以通过查找每个同义词集深度量化这个一般性的概念:
##print wn.synset('baleen_whale.n.01').min_depth()
##print wn.synset('whale.n.02').min_depth()
##print wn.synset('vertebrate.n.01').min_depth()
##print wn.synset('entity.n.01').min_depth()
####path_similarityassigns是基于上位词层次结构中相互连接的概念之间的
####最短路径在0-1范围的打分(两 者之间没有路径就返回-1)
####同义词集与自身比较将返回1
####考虑以下的相似度:露脊鲸与 小须鲸、逆戟鲸、乌龟以及小说
####数字本身的意义并不大,当我们从海洋生物的语义空间转 移到非生物时它是减少的
##print right.path_similarity(minke)
##print right.path_similarity(orca)
##print right.path_similarity(tortoise)
##print right.path_similarity(novel)



###### my example #########
##ww = 'seats'
##for sy in wn.synsets(ww,wn.NOUN):
##    print sy
##    print sy.lemma_names
##    print sy.definition
##    print sy.examples
##    print sy.part_meronyms()
##    print sy.substance_meronyms()
##    print sy.member_holonyms()
##    if sy.part_meronyms() !=[]:
##        for ssy in sy.part_meronyms():
##            print ssy.part_meronyms()
##            if ssy.part_meronyms()!=[]:
##                for sssy in ssy.part_meronyms():
##                    print sssy.part_meronyms()
######################
##ww = 'great'
##for sy in wn.synsets(ww):
##    print sy
##    print sy.part_holonyms()
##    print sy.substance_holonyms()
######################
##ww = 'fight'
##for sy in wn.synsets(ww,wn.VERB):
##    print sy
##    print sy.entailments()
######################
##ww = 'attack'
##for sy in wn.synsets(ww,wn.VERB):
####    print dir(sy)
####    for sn in sy.lemma_names:
##    for sn in sy.lemmas:
##        print sn
##        print sn.antonyms()
######################
##ww = 'taliban'
##for sy in wn.synsets(ww,wn.NOUN):
####    print dir(sy)
####    for sn in sy.lemma_names:
##    print sy.min_depth()
##    print sy.hyponyms()##向下
##    print sy.hypernym_paths()##向上

####上下漫游
##ws = wn.synset('seat.n.03')
##for s in ws.lemmas:
##    print s.name
##    print s.count()
##print dir(ws)
####向下
##types_of_word = ws.hyponyms()
##print types_of_word
####print types_of_car[26]
####print sorted([lemma.name for synset in types_of_car for lemma in synset.lemmas])
######向上
##paths = ws.hypernym_paths()
##print paths
##print ws.part_meronyms()
##print ws.member_holonyms()
##print ws.instance_hyponyms()


###demo-nltk/corpus/reader/wordnet.py


