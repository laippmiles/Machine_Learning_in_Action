def textParse(string):
    import re
    listOfTokens = re.split(r'\W+',string)
    #第一个正则式指被切出来的匹配的文本形式（？不完全确定）
    #这部分正则式参考了以下网址
    #https://www.cnblogs.com/yuxc/archive/2011/08/06/2129699.html
    #多个分隔符，复杂的分隔情况，使用re.split
    #\W*,指配对一连串字母数字知道出现标点符号为止
    return [tokens.lower() for tokens in listOfTokens if len(tokens) > 2 ]
    #只留下长度大于2的词汇
    #l上面使用了推导式
    #详见https://www.cnblogs.com/tkqasn/p/5977653.html
    #简单地说就是先for in 再在后面追加if