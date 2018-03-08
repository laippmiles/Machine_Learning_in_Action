from optStruct import optStruct
from numpy import  multiply , nonzero
def selectJrand(i,numOfData):
    #这个子函数用来简化版SMO随机选择第i个alpha参数对应的alpha参数j（i不等于j）
    from random import uniform
    j = i
    while(j == i):
       j = int(uniform(0,numOfData))
    return j

def cilpAlpha(alphaJ,H,L):
    #H:限幅最大值，L:限幅最小值
    if alphaJ > H:
        alphaJ = H
    elif alphaJ < L:
        alphaJ = L
    return alphaJ

def calcEk(oS, k):
    #计算Ek，因为寻找最优参数对时常有这个动作，所以单独拎出来
    fXk = float(multiply(oS.alphas, oS.y).T * \
                (oS.X * oS.X[k, :].T) +oS.b)
    Ek = fXk -float(oS.y[k])
    return Ek

def selectJ(i, oS, Ei):
    #用于选择对于alphaI对应的另一个alpha参数J
    maxK = -1 ; maxDetaE = 0 ; Ej =0
    #参数初始化
    validEcacheList = list(nonzero(oS.eCache[:, 0].A))[0]
    #nonzero的输入需要是数组，所以需要用.A将矩阵转化为数组
    #循环前提取第一个已经计算好Ek的样本，nonzero提取出的是它的索引
    if(len(validEcacheList) >1 ):
        #如果存在已经计算好Ek的样本的话，用这种方法找参数对
        for k in validEcacheList:
            if k == i : continue
            Ek = calcEk(Ei, k)
            deltaE = abs(Ei - Ek)
            if( deltaE > maxDetaE ) :
                maxDetaE = deltaE
                maxK = k
                Ej = Ek
        return maxK ,Ej
    else:
        # 如果不存在，用最原始的随机找对法找配对
        j = selectJrand(i, oS.numOfData)
        Ej = calcEk(oS, j)
    return j, Ej

def updateEk(oS,k):
    #更新误差缓存
    Ek = calcEk(oS,k)
    oS.eCache[k] = [1,Ek]

def optTheAlphaIAndJ(i, oS):
    Ei = calcEk(oS,i)
    if (
            ((oS.y[i] * Ei < -oS.toler) and (oS.alphas[i] < oS.C))  or
            ((oS.y[i] * Ei > oS.toler) and (oS.alphas[i] > 0))
    ): #检查alpha值在0与C之间，并测试正负间隔
        #注意不要抄错Data和Label

        j,Ej = selectJ(i,oS,Ei)
        alphaIOld = oS.alphas[i].copy()
        alphaJOld = oS.alphas[j].copy()
        #用复制的方法获取i ， j 的alpha历史参数

        if (oS.y[i] != oS.y[j]):
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            #不要抄错公式
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        #设定新的上下界限幅
        if L == H :#print('L == H');
             return  0
            #这个子函数不会直接输出得数，计算结果通过数据结构传递
            #这个return传递的是这次优化的alphaPairsChanged情况

        eta = (2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j])
        if eta >= 0 :#print('eta >= 0') ;
            return 0
        #eta 的取值与Mercer值相关

        #先更新alpha[j]
        oS.alphas[j] -= oS.y[j] * (Ei - Ej) / eta
        oS.alphas[j] = cilpAlpha(oS.alphas[j], H, L)
        if(abs(oS.alphas[j]-alphaJOld) < 0.0001): #print('j not moving enough') ;
            return 0

        #更新alpha[i]
        oS.alphas[i] += oS.y[j] * oS.y[i] * (alphaJOld - oS.alphas[j])
        #alpha[i]不需要再次限幅

        b1 = oS.b - Ei - oS.y[i] * (oS.alphas[i] - alphaIOld) * oS.K[i,i] - \
                         oS.y[j] * (oS.alphas[j] - alphaJOld) * oS.K[i,j]

        b2 = oS.b - Ej - oS.y[i] * (oS.alphas[i] - alphaIOld) * oS.K[i,i] - \
                         oS.y[j] * (oS.alphas[j] - alphaJOld) * oS.K[j,j]
        #先计算b1 ， b2

        if (oS.alphas[i] > 0) and (oS.alphas[i] < oS.C) :
            oS.b = b1
        elif (oS.alphas[j] > 0) and (oS.alphas[j] < oS.C):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0
        #更新b值
        return 1
        #完成一次迭代，增加计数
    else:return 0

def calcWs(alphas, inputData, inputLabels):
    from numpy import shape, zeros, multiply
    numOfData, numOfFeature = shape(inputData)
    weight = zeros((numOfFeature,1))
    for i in range(numOfData):
        weight += multiply(alphas[i]*inputLabels[i] , inputData[i,:].T)
    return weight