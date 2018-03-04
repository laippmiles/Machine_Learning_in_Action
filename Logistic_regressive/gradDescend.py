from numpy import shape,ones,max,transpose
from sigmoid import *
from random import uniform
def gradDescend(inputData, inputLabels, alpha, maxIter):
    numOfData , numOfFeature = shape(inputData)
    weights = ones((numOfFeature,1))
    #记得这里是双括号

    for k in range(maxIter):
        #print('%d th iter' %(k+1))
        h = sigmoid(inputData * weights)
        error = (h - inputLabels)
        weights = weights - alpha * inputData.transpose() *error
        #这里是梯度下降的代价函数
    return weights

def stocGradDescend(inputData, inputLabels, alpha):
    numOfData , numOfFeature = shape(inputData)
    weights = ones((numOfFeature,1))
    #记得这里是双括号
    for i in range(numOfData):
        h = sigmoid(sum(inputData[i]*weights))
        error = (h[0] - inputLabels[i])
        weights = weights - alpha * error[0, 0] * inputData[i].transpose()
        #这里是梯度下降的代价函数
    return weights

def stocGradAscentPlus(dataMatrix, classLabels,numIter = 150):
    numOfData ,numOfFeature = shape(dataMatrix)
    weights = ones((numOfFeature,1))   #initialize to all ones
    for i in range(numIter):
        dataIndex = list(range(numOfData))
        #print(' %d th iter' %i)
        for j in range(numOfData):
            alpha = 4 / (1+i+j) + 0.01
            #改进随机梯度下降有自动调节的学习率
            randIndex = int(uniform(0,len(dataIndex)))
            #随机抽取用于更新梯度下降的样本
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = h[0] - classLabels[randIndex]
            weights = weights - alpha * error[0,0] * dataMatrix[randIndex].transpose()
            #error出来是一个只有一个元素的矩阵，真的是天大恶意了......
            # 把所有变量搞出来以后对个尺寸就知道了，dataMatrix[i].transpose()要转置
            del (dataIndex[randIndex])
    return weights


