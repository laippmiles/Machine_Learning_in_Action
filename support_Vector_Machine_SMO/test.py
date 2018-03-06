from csv2ListOrMatrix import csv2ListOrMatrix
from plotData import plotData
from SMO_Simple import SMO_Simple
loadData = csv2ListOrMatrix('testSet.csv')
lables = loadData[:,0]
data = loadData[:,1:]
#plotData(data,lables)
b , alphas = SMO_Simple(data,lables)
print(b , alphas)