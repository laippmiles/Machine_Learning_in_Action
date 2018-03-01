from csv2ListOrMatrix import *
from shannonEnt import *
from splitDataSet import *
from chooseBestFeatureToSplit import *
from createTree import *
from decisionTreeClassify import *
from treePlot4In1 import *
datasetName = 'fish'
data = csv2ListOrMatrix('Test_'+ datasetName +'.csv','list')
labels = csv2ListOrMatrix('Test_labels_' + datasetName + '.csv','list')[0]
#这个出来的是嵌套列表，所以自己动手取第一行才是我们想要的东西
print(calShannonEnt(data))
print(chooseBestFeatureToSplit(data))
print(data)
print(labels)
tree = createTree(data,labels)
print(tree)
createPlot(tree)
#testVector = [0,1]
#print(decisionTreeClassify(tree,labels,testVector))
