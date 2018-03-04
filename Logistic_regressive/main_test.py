from csv2ListOrMatrix import *
from gradDescend import *
from numpy import shape,column_stack,ones
from plotBestFit import *
#载入数据
path = r'D:\桌面\18_spring\机器学习实战\ML-in-Action-Code-and-Note-master\Machine_Learning_in_Action\Data'
testSet = r'\testSet.csv'
test = csv2ListOrMatrix(path + testSet)
#trainData = train[:,1:]
#trainLabel = train[:,0]
testData = column_stack((ones((list(shape(test))[0],1)),test[:,1:]))
testLabel = test[:,0]
#weights = gradDescend(testData,testLabel,0.001,500)
#weights = stocGradDescend(testData,testLabel,0.01)
weights = stocGradAscentPlus(testData,testLabel)
print(weights)
plotBestFit(testData,testLabel,weights)

