def majorityVote(classList):
    from operator import itemgetter
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    SortClassCount = sorted(classCount.items(),key=itemgetter(1),reverse=True)
    #itemgetter和sorted的配合详见
    #https://jingyan.baidu.com/article/f3ad7d0ffe8e1409c2345b48.html
    #key=itemgetter(1)指以字典的键来作排序标准
    #这个写法可能还挺常用的
    #在3.x 里 用 items()替换iteritems() ，可以用于 for 来循环遍历。
    return SortClassCount[0][0]