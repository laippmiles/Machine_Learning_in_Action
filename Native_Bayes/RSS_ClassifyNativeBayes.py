#现实用RSS爬虫并做朴素贝叶斯分析
from textParse import *
#textParse(string)
from loadDataSet import *
#loadDataSet()
from createVocabList import *
#createVocabList(dataSet)
from words2Vector import *
#setOfWords2Vector(vocabList,dataSet)
from nativeBayes import *
#trainNativeBayes(trainData,trainLabel)  ;return p1Vector , p0Vector, pClass1
#classifyNativeBayes(inputData,p1Vector,p0Vector,pClass1)  ,
from random import uniform

def localWord(inPutClass1,inPutClass2):
    postList = []
    classList = []

    numOfSfBay = len(inPutClass1['entries'])
    numOfNewYork = len(inPutClass2['entries'])

    for dataSfBay in range(numOfSfBay):
        post = inPutClass1['entries'][dataSfBay]['summary']
        #parse读出来是一个嵌套字典的形式，用这种办法提取字符串
        post = textParse(post)
        postList.append(post)
        classList.append(1)

    for dataNewYork in range(numOfNewYork):
        post = inPutClass2['entries'][dataNewYork]['summary']
        post = textParse(post)
        postList.append(post)
        classList.append(0)

    #----------------------------------从这开始除了数据集变量不同，和mainTestEmail相应部分是一样的------------------------------
    vocabList = createVocabList(postList)

    trainSetIndex = list(range(len(postList)))
    #注意python2与python3 range的差别
    #python3的range出来不是list，而是一个迭代变量
    testSetIndex = []

    NumOfTestData = int(len(trainSetIndex)/5)

    for i in range(NumOfTestData):
        index = int(uniform(0,len(trainSetIndex)))
        #要转换为整型
        testSetIndex.append(trainSetIndex[index])
        del trainSetIndex[index]

    trainData = []
    trainLabel = []
    testData = []
    testLabel = []

    for indexTrain in trainSetIndex:
        trainData.append(bagOfWords2Vector(vocabList,postList[indexTrain]))
        #记得不要直接导入文本，要调用Words2Vector转换成数字矩阵形式
        trainLabel.append(classList[indexTrain])

    p1Vector , p0Vector, pClass1 = trainNativeBayes(trainData,trainLabel)

    error = 0.0

    #指标用的准确率
    for indexTest in testSetIndex:
        testVector = bagOfWords2Vector(vocabList,postList[indexTest])
        answer = classifyNativeBayes(testVector,p1Vector , p0Vector, pClass1)
        if answer != classList[indexTest]:
            error += 1

    accuracy = 1 - float(error / len(postList))
    print('The accuracy is : %f' % accuracy)

    return vocabList, p1Vector , p0Vector