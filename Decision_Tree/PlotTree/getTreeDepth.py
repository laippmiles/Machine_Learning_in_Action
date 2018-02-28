def getTreeDepth(tree):
    maxDepth = 0
    #初始化
    firstStr = list(tree.keys())[0]
    #Depth部分和NumLeaf一样的就不再记笔记了
    secondDict = tree[firstStr]

    for key in secondDict.keys():
        if type(secondDict[key]) is dict:
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1

        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth