def calShannonEnt(dataSet):
    from math import  log
    numOfData = len(dataSet)
    labelCounts = {}
    for dataVector in dataSet:
        classOfData = dataVector[0]
        #个人习惯把标签集放第一列
        if classOfData not in labelCounts.keys():
        #如果目前样本信息集里头没有该类别的相关信息
            labelCounts[classOfData] = 0
            #进行初始化
        labelCounts[classOfData] += 1
    #print(labelCounts)
    #测试点，平时不开
    #上述过程记录了样本集每类样本的分布情况
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/numOfData
        shannonEnt -= prob * log(prob,2)
    return shannonEnt