# coding=utf-8
import nltk


##from nltk.book import *
####*** Introductory Examples for the NLTK Book ***
####Loading text1, ..., text9 and sent1, ..., sent9
####Type the name of the text or sentence to view it.
####Type: 'texts()' or 'sents()' to list the materials.
####text1: Moby Dick by Herman Melville 1851
####text2: Sense and Sensibility by Jane Austen 1811
####text3: The Book of Genesis
####text4: Inaugural Address Corpus
####text5: Chat Corpus
####text6: Monty Python and the Holy Grail
####text7: Wall Street Journal
####text8: Personals Corpus
####text9: The Man Who Was Thursday by G . K . Chesterton 1908
##

####查一下《白鲸记》中的词 monstrous
##print text1.concordance("monstrous")
##
####我们看到monstrous出现的上下文,如 the ___ pictures和the ___ size。还有哪些词出现在相似的上下文中?我们可以通过在被查询的 文本名后添加函数名 similar,然后在括号中插入相关的词来查找到
##print text1.similar("monstrous")
##print text2.similar("monstrous")
##
####函数common_contexts允许我们研究两个或两个以上的词共同的上下文,如monstro us和very
##print text2.common_contexts(["monstrous", "very"])
##
####判断词在文本中的位置:从文本开头算起在它前面有多少词。这个位置信息 可以用离散图表示。每一个竖线代表一个单词,每一行代表整个文本
##text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])




########try my example
##fileName = "sample1-1.txt"
fileName = "result.xml"
with open(fileName, 'r') as f:
    sample = f.read()

text = nltk.word_tokenize(sample)
text = nltk.Text(text)

print text.concordance("CORPORATE")
##print text.concordance("traffic")
##print text.concordance("Taliban")

##print text.similar("leader")
##print text.common_contexts(["Bannu", "Razmak"])
##print text.collocations()

##print text.findall(r'<\w*><attack><\w*>')




