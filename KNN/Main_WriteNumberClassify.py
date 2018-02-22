from  K_NN import *
from LoadData import *
from numpy import zeros
#Ctrl+左键，可以跳转到任何子函数里头
#listdir(path)作用为列出给定目录的文件名
K = 10
NumOfPixel_height = 32
NumOfPixel_width = 32
#在转化为矩阵后，高对应行数，宽对应列数
NumOfClass = 10
TrainDataPath = 'trainingDigits'
TestDataPath = 'testDigits'
#载入训练数据
TrainLables = LoadData(TrainDataPath,NumOfPixel_height,NumOfPixel_width)[0]
TrainDataMat = LoadData(TrainDataPath,NumOfPixel_height,NumOfPixel_width)[1]
#如果一个子函数返回a，b，c，而目前只需要a,b
#可将这个问题转化为:
#Python中看似有多个返回值，实际上多返回值时返回的都是一个tuple，那问题就变成了如何分割tuple
#即func（）本身是个按return顺序排列的tuple
TestLables,TestDataMat,NumOfTestData = LoadData(TestDataPath,NumOfPixel_height,NumOfPixel_width)
ClassifyerAnswer = []
NumOfError = 0
for i in range(NumOfTestData):
    ClassifyerOfIthTestData = KNN(TestDataMat[i,:],TrainDataMat,TrainLables,K)
    print('ClassifyerOfIthTestData :%s  ActualOfIthTestData :%s' %(ClassifyerOfIthTestData,TestLables[i]))
    if ClassifyerOfIthTestData != TestLables[i]:
        NumOfError += 1
print(NumOfError/NumOfTestData)