from csv2ListOrMatrix import csv2ListOrMatrix
from plotData import plotData
from SMO_Simple import SMO_Simple
from SMO_Platt import SMO_Platt
from optStruct import optStruct
from numpy import shape
#试着跑了个病马
loadData = csv2ListOrMatrix('horseColic.csv')
lables = loadData[:,0]
data = loadData[:,1:]
#plotData(data,lables)
opt = optStruct(data,lables,kPara = ('rbf',1.3))
print(opt.K)
#b , alphas = SMO_Simple(data,lables)
weight,b = SMO_Platt(opt)
print(weight,b)
#简单测试一下

loadTestData = csv2ListOrMatrix('horseColicTest.csv')
testLables = loadTestData[:,0]
testData = loadTestData[:,1:]
numOfTestData = list(shape(testData))[0]
error = 0.0
for i in range(numOfTestData):
    if ( (testData[i,:]*weight+b>0) != (testLables[i,:] > 0) ):
        print('classify :', testData[i,:]*weight+b>0,'actual :', testLables[i,:]>0 ,'i: %d' %i)
        error += 1
print(error)
print('acc: %f' %(1-error/numOfTestData))