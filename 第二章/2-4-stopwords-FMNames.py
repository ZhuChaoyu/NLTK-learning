# coding=utf-8
import nltk

##停用词语料库
from nltk.corpus import stopwords

##print stopwords.words('english')

for s in stopwords.words('english'):
    print s



####男女名字
##names = nltk.corpus.names
##print names.fileids()
##
####male_names = names.words('male.txt')
####female_names = names.words('female.txt')
####
####找出同时出现在两个文件中的名字即性别暧昧的名字
####print [w for w in male_names if w in female_names]
####找到以字母A开头的女性名字
####print [w for w in male_names if w[0]=='S' and w not in female_names]
######S开头男性名且不是女姓名，名字字母长度大于6
####print [w for w in male_names if w[0]=='S' and w not in female_names and len(w)>6]
####print len([w for w in male_names if w[0]=='S' and w not in female_names and len(w)>6])
##
####条件频率分布:此图显示男性和女性名字的结尾字母;大多数以a,e
####或i结尾的名字是女性;以h和l结尾的男性和女性同样多;
####以k,o,r,s和t结尾的更可能是男性。
##cfd = nltk.ConditionalFreqDist(
##     (fileid, name[-1])
##     for fileid in names.fileids()
##     for name in names.words(fileid))
##
##cfd.plot()
