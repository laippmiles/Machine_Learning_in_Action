def decisionTreeClassify(inputTree,featureLabels,testVector):
    firstStr = list(inputTree.keys())[0]
    secondTreeDict = inputTree[firstStr]
    featureIndex = featureLabels.index(firstStr)
    #程序是无法自己得到特征在数据集的具体位置的
    #所以需要借助index得到目前需要分析的特征的索引
    for key in secondTreeDict.keys():
        if testVector[featureIndex] == key:
            #找到了目前要对照的特征索引
            if type(secondTreeDict[key]) is dict:
                classifyTheDataClass = decisionTreeClassify(secondTreeDict[key],featureLabels,testVector)
            else:
                classifyTheDataClass = secondTreeDict[key]
                #到达底部，分类结果即为该底部指向的分类值

    return  classifyTheDataClass