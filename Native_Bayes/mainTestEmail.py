from textParse import *
from loadDataSet import *
#loadDataSet()
from createVocabList import *
#createVocabList(dataSet)
from words2Vector import *
#setOfWords2Vector(vocabList,dataSet)
from nativeBayes import *

print(textParse(r"Hello world , I'm a corgi."))