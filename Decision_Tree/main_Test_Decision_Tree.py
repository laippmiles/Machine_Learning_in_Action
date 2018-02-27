from csv2ListOrMatrix import *
from shannonEnt import *
from splitDataSet import *
from chooseBestFeatureToSplit import *
from createTree import *
data = csv2ListOrMatrix('Test.csv','List')
print(calShannonEnt(data))
print(splitDataSet(data,1,1))
print(chooseBestFeatureToSplit(data))
lables = ['No surfacing','flippers']
print(createTree(data,lables))