# coding=utf-8

##from nltk.book import *
##
##print sent1


###本节重点介绍python List,索引和切片

##为 Python 变量选择名称(或标识符)时请注意:首先,应该以字母开始,
##后面跟数字(0 到 9)或字母。因此,abc23 是好的,23abc 会导致一个语 法错误。
##名称是大小写敏感的。这意味着 myVar 和 myvar 是不同的变量。
##变量名不能包含空格,但可以用下划线把单词分开,如 my_var。
##注意不要 插入连字符来代替下划线:my-var不对,因为 Python 会把-解释为减号。


##我们可以把词用链表连接起来组成单个字符串,或者把字符串分割成一个链表,如下面 所示:
print ' '.join(['Monty', 'Python'])
print 'Monty Python'.split()
