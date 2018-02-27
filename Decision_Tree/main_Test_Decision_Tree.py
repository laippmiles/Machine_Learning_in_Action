from csv2ListOrMatrix import *
from shannonEnt import *
from splitDataSet import *
data = csv2ListOrMatrix('Test.csv','List')
print(calShannonEnt(data))
print(splitDataSet(data,1,1))