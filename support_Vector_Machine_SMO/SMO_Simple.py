from  numpy import shape, mat, zeros, multiply
from SMOSupportFunc import selectJrand, cilpAlpha
def SMO_Simple(inputData, inputLabels, C=0.6, toler=0.001, maxIter=40):
    #SVM具体推导公式如下：
    #http://blog.csdn.net/shiyanwei1989/article/details/38708973
    #SMO公式介绍比较好的一篇文章：
    #http://blog.csdn.net/luoshixian099/article/details/51227754
    #转置好像在后面直接.T即可
    #multiply是矩阵点乘
    b = 0
    numOfData , numOfFeature = shape(inputData)
    alphas = mat(zeros((numOfData,1)))
    #zeros出来的输出类型是：<class 'numpy.ndarray'>
    iter = 0
    #初始化

    while(iter < maxIter):
        alphaPairsChanged = 0
        #初始化参数对更新计数

        for i in range(numOfData):
            fXi = float(multiply(alphas, inputLabels).T * (inputData * inputData[i,:].T)) + b
            #每个样本都有其对应的alpha参数
            #计算输入第i个样本时基于目前alpha组的输出值
            Ei = fXi - float(inputLabels[i])
            #对第i个样本的误差

            if (
                    ((inputLabels[i] * Ei < -toler) and (alphas[i] < C))  or
                        ((inputLabels[i] * Ei > toler) and (alphas[i] > 0))
            ): #检查alpha值在0与C之间，并测试正负间隔

                j = selectJrand(i,numOfData)

                fXj = float(multiply(alphas, inputLabels).T * (inputData * inputData[j,:].T)) + b
                #计算输入第j个样本时基于目前alpha组的输出值
                Ej = fXj - float(inputLabels[j])
                # 对第j个样本的误差

                alphaIOld = alphas[i].copy()
                alphaJOld = alphas[j].copy()
                #用复制的方法获取i ， j 的alpha历史参数

                if (inputLabels[i] != inputLabels[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    #不要抄错公式
                    H = min(C, alphas[j] + alphas[i])
                #设定新的上下界限幅
                if L == H :#print('L == H');
                    continue

                eta = (2.0 * inputData[i,:] * inputData[j,:].T) - \
                      (inputData[i, :] * inputData[i, :].T) - \
                      (inputData[j, :] * inputData[j, :].T)
                if eta >= 0 :#print('eta >= 0') ;
                    continue
                #eta 的取值与Mercer值相关

                #先更新alpha[j]
                alphas[j] -= inputLabels[j] * (Ei - Ej) / eta
                alphas[j] = cilpAlpha(alphas[j], H, L)
                if(abs(alphas[j]-alphaJOld) < 0.0001): #print('j not moving enough') ;
                    continue

                #更新alpha[i]
                alphas[i] += inputLabels[j] * inputLabels[i] * (alphaJOld - alphas[j])
                #alpha[i]不需要再次限幅

                b1 = b - Ei - inputLabels[i] * (alphas[i] - alphaIOld) * inputData[i,:] * inputData[i,:].T - \
                              inputLabels[j] * (alphas[j] - alphaJOld) * inputData[i,:] * inputData[j,:].T

                b2 = b - Ej - inputLabels[i] * (alphas[i] - alphaIOld) * inputData[i,:] * inputData[j,:].T - \
                              inputLabels[j] * (alphas[j] - alphaJOld) * inputData[j,:] * inputData[j,:].T
                #先计算b1 ， b2

                if (alphas[i] > 0) and (alphas[i] < C) :
                    b = b1
                elif (alphas[j] > 0) and (alphas[j] < C):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                #更新b值

                alphaPairsChanged += 1
                #完成一次迭代，增加计数
                print(' iter : %d ,i: %d pairs changed %d' %(iter ,i, alphaPairsChanged ))
        if (alphaPairsChanged == 0) : iter += 1
        else: iter = 0
        #要连续maxIter次alphaPairs不被优化的情况下才算参数组已经收敛，这时优化完成
        print('iteration nuber : %d' %iter)
    return b , alphas