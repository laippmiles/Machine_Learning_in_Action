def SMO_Platt(oS):
    #kPara是核函数参数，暂时用不上（18.03.07）
    from optStruct import optStruct
    from SMOSupportFunc import optTheAlphaIAndJ , calcWs
    from numpy import nonzero,zeros, mat
    numOfIter = 0
    entireSet = True
    alphaPairsChanged = 0
    weight = zeros((oS.numOfFeature,1))
    #初始化参数

    while((numOfIter < oS.maxIter) and (alphaPairsChanged > 0 ) or (entireSet)):
        alphaPairsChanged = 0
        #每次迭代复位一次alphaPairsChanged
        if entireSet:
            for i in range(oS.numOfData):
                alphaPairsChanged += optTheAlphaIAndJ(i,oS)
                print('对整个训练集进行参数优化；iter :%d i:%d ,pairs changed %d'%(numOfIter, i, alphaPairsChanged))
            numOfIter += 1
            #这个迭代机制和简化版不同，这个做完一轮优化算一次迭代。
        else:
            notInBound = list(nonzero((oS.alphas.A > 0) * (oS.alphas.A < oS.C)))[0]
            #(oS.alphas.A > 0)和(oS.alphas.A < C）出来都是元素只有Ture和False的布尔型数组
            #两个布尔型数组之间做逻辑运算，且的表达方法是用*（且用+应该能行吧..?）
            #notInBound是非边界点的索引集
            for i in notInBound:
                alphaPairsChanged += optTheAlphaIAndJ(i,oS)
                print('对非边界点进行参数优化；iter :%d i:%d ,pairs changed %d'%(numOfIter, i, alphaPairsChanged))
            numOfIter += 1
        if entireSet:entireSet = False
        #迭代完一次以后切换扫描形式
        elif (alphaPairsChanged == 0 ):entireSet = True
        print('iteration number : %d' %numOfIter)
        #当在非边界模式扫描结束时alphaPairsChanged仍等于0时停止迭代，输出优化参数组
        weight =mat(calcWs(oS.alphas , oS.X, oS.y))
    return weight , oS.b