from numpy import array

from  AutoNorm import *
from  File2Matrix import *
from  K_NN import *

Mat,Lables = File2Matrix('datingTestSet.txt',3)
NormDataSet,MaxMinusMin,MinVals = AutoNorm(Mat)
#print(NormDataSet)
Input = (array([14488,7.153469,1.673904]) - MinVals)/MaxMinusMin
Answer = KNN(Input,NormDataSet,Lables,3)
print(Answer,end='')