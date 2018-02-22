from  File2Matrix import *
from  AutoNorm import *
from  K_NN import *
from numpy import array
from Img2Vectot import *
from os import listdir
#listdir(path)作用为列出给定目录的文件名
HandWriteLables = []

Vector = Img2Vector(r'testDigits\0_0.txt',32
)

print(Vector)