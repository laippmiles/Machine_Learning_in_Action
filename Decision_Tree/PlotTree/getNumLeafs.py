def getNumLeafs(tree):
    numOfLeafs = 0
    #初始化
    firstStr = list(tree.keys())[0]
    #在python2.x中，dict.keys()返回一个列表，在python3.x中，dict.keys()返回一个dict_keys对象，比起列表，这个对象的行为更像是set，所以不支持索引的。
    #因此firstStr = tree.keys()[0]应再加一层list（）
    #取第一个特征开头
    secondTreeDict = tree[firstStr]
    #取起点底下的第一外层嵌套字典
    for key in secondTreeDict:
        if type(secondTreeDict[key]) is dict:
        #关于这句指令的细节参照
        #http://blog.csdn.net/qq_33363973/article/details/77878122
            numOfLeafs += getNumLeafs(secondTreeDict[key])
            #递归向下
        else:
            numOfLeafs += 1
            #到了某层底部，直接加一即可
    return numOfLeafs