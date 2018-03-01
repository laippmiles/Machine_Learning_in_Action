from numpy import *
def trainNativeBayes(trainData,trainLabel):
    numOfData = len(trainData)
    numOfWord = len(trainData[0])
    #得到词汇库总数，不过训练时用不上词汇库，转换成向量时才用
    pClass1 = float(sum(trainLabel)/numOfData)
    #得到P(c1);此处1类为恶意言论，0类为正常言论

    #先初始化p(w|ci)的分子,为了防止最后w算出来是0，初值设为1
    p0Num = ones(numOfWord)
    p1Num = ones(numOfWord)
    #先初始化p(w|ci)的分母,为了防止最后w算出来是0，初值设为2
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numOfData):
        if trainLabel[i] == 1:
            #第i个样本为第1类
            p1Num += trainData[i]
            #这里实际上是向量相加，相加结果就是第1类所有样本每个词总共的使用频率
            p1Denom += sum(trainData[i])
            #p1Denom最后是第一类所有样本一共包含的字数
        else:
            p0Num += trainData[i]
            p0Denom += sum(trainData[i])

    p1Vector = log(p1Num/p1Denom)
    #计算p(w|c1),按照特征，这是一个向量
    p0Vector = log(p0Num/p0Denom)
    #计算p(w|c1),按照特征，这是一个向量
    return p1Vector , p0Vector, pClass1

def classifyNativeBayes(inputData,p1Vector,p0Vector,pClass1):
    p1 = sum(inputData * p1Vector) + log(pClass1)
    p0 = sum(inputData * p0Vector) + log(1.0 - pClass1)
    #原理：log（a*b） = log(a) + log(b)
    #无论是p1还是p0，inputdata第i个特征的值每多一个1，整个p就多乘一个相应的p（wi|c）(每个词独立分布)

    if p1 > p0:
        return 1
    else:
        return 0
