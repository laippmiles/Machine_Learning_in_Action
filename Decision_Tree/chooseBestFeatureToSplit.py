def chooseBestFeatureToSplit(dataSet):
    import shannonEnt
    numOfFeature = len(dataSet[0])-1
    #减1是因为第一列是标签，不是特征
    baseEnrtopy = shannonEnt.calShannonEnt(dataSet)
    #在子函数调用自制模组只有这样不报错...不懂
    bestInfoGain = 0.0
    bestFeature = -1
    #初始化
    for indexOfFeature in range(1,numOfFeature+1):
        featureValueList = [example[indexOfFeature] for example in dataSet]
        featureValueSet = set(featureValueList)
        #取第IndexOfFeature个特征所右可能的取值
        newEntropy = 0.0