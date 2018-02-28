def createTree(dataSet,labels):
    from majorityVote import majorityVote
    from chooseBestFeatureToSplit import chooseBestFeatureToSplit
    from splitDataSet import splitDataSet
    classList = [example[0] for example in dataSet]
    #提取dataSet的样本标签集
    if classList.count(classList[0]) == len(classList):
        #dataSet只有一类
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityVote(classList)
        #当递归算法使用完所有特征后，这里不用单纯的一类作返回值，而是以majorityVote投票选多数类作返回值
    Trainlabels = labels.copy()
    #不要直接用labels，copy一下，要不会破坏原数据

    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = Trainlabels[bestFeature-1]
    #这里和书中不同，要-1
    tree = {bestFeatureLabel:{}}
    #结构初始化

    del(Trainlabels[bestFeature-1])
    #已写入树结构的标签可以去掉了
    #这里和书中不同，要-1

    #以下步骤为基于目前的最佳分割特征来分割现有的数据集
    featureValues = [example[bestFeature] for example in dataSet]
    featureValuesSet = set(featureValues)
    for value in featureValues:
        subLabels = Trainlabels[:]
        tree[bestFeatureLabel][value] = createTree(splitDataSet(dataSet,bestFeature,value),subLabels)
        #用递归的方法建立嵌套字典
        #字典先成型的是最底下的叶节点，然后再自下而上往上层嵌套构造的整个树

    return tree