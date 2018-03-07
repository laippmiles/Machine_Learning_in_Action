from csv2ListOrMatrix import csv2ListOrMatrix
from plotData import plotData
from SMO_Simple import SMO_Simple
from SMO_Platt import SMO_Platt
from optStruct import optStruct
loadData = csv2ListOrMatrix('testSet.csv')
lables = loadData[:,0]
data = loadData[:,1:]
#plotData(data,lables)
opt = optStruct(data,lables)
#b , alphas = SMO_Simple(data,lables)
weight,b = SMO_Platt(data,lables)
print(weight,b)
#简单测试一下
print(((opt.X[1,:])*weight+b)>0)
print(opt.y[1,:]>0)