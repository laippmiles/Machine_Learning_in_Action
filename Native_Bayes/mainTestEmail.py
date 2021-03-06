from textParse import *
from loadDataSet import *
#loadDataSet()
from createVocabList import *
#createVocabList(dataSet)
from words2Vector import *
#setOfWords2Vector(vocabList,dataSet)
from nativeBayes import *
#trainNativeBayes(trainData,trainLabel)  ;return p1Vector , p0Vector, pClass1
#classifyNativeBayes(inputData,p1Vector,p0Vector,pClass1)  ,
#print(textParse(r"Hello world , I'm a corgi."))
#测试分词功能
from os import listdir
from random import uniform
listOfHamEmail = listdir('email/ham')
numOfHamEmail = len(listOfHamEmail)

listOfSpamEmail = listdir('email/spam')
numOfSpamEmail = len(listOfSpamEmail)

emailList = []
classList = []

for i in range(1,numOfSpamEmail+1):
    #这里记得+1
    email = open('email/spam/%d.txt' %i, "rb").read().decode('GBK', 'ignore')
    #这个对比书上的代码要麻烦一点，属于python2和python3之间编码差异问题
    # wordList=textParse(open('email/spam/%d.txt' %i).read()) 照书写会 unicode error
    wordList = textParse(email)
    emailList.append(wordList)
    classList.append(1)

for i in range(1,numOfHamEmail+1):
    email = open('email/ham/%d.txt' %i, "rb").read().decode('GBK', 'ignore')
    wordList = textParse(email)
    emailList.append(wordList)
    classList.append(0)

vocabList = createVocabList(emailList)

trainSetIndex = list(range(len(emailList)))
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
    trainData.append(bagOfWords2Vector(vocabList,emailList[indexTrain]))
    #记得不要直接导入文本，要调用Words2Vector转换成数字矩阵形式
    trainLabel.append(classList[indexTrain])

p1Vector , p0Vector, pClass1 = trainNativeBayes(trainData,trainLabel)

error = 0.0

#指标用的准确率
for indexTest in testSetIndex:
    testVector = bagOfWords2Vector(vocabList,emailList[indexTest])
    answer = classifyNativeBayes(testVector,p1Vector , p0Vector, pClass1)
    if answer != classList[indexTest]:
        error += 1

accuracy = 1 - float(error / len(emailList))
print('The accuracy is : %f' % accuracy)