from  File2Matrix import *
from  AutoNorm import *
Mat,Lables = File2Matrix('datingTestSet.txt',3)
NormDataSet,MaxMinusMin,MinVals = AutoNorm(Mat)