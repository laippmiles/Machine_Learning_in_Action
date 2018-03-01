from loadDataSet import *
#loadDataSet()
from createVocabList import *
#createVocabList(dataSet)
from words2Vector import *
#setOfWords2Vector(vocabList,dataSet)
from nativeBayes import *
#trainNativeBayes(trainData,trainLabel)   ;return p1Vector , p0Vector, pClass1
#classifyNativeBayes(inputData,p0Vector,p1Vector,pClass1)   ;return 1 or 0



dataOfPost,classOfPost = loadDataSet()
vocabList  = createVocabList(dataOfPost)
print(vocabList)

setWordVector = []
for post in dataOfPost:
    vector = setOfWords2Vector(vocabList,post)
    setWordVector.append(vector)
    #此处应注意append和extend的区别
    #append是把输入参数“一整个”当作接入列表的元素，可用来构造嵌套列表
    #extend用来连接两个列表，
    #如列表A = [1,2],B=[1,2]
    # A.append（B）=[1,2,[1,2]]
    # A.extend(B) =[1,2,1,2]

bagWordVector = []
for post in dataOfPost:
    vector = bagOfWords2Vector(vocabList,post)
    bagWordVector.append(vector)

p1Vector , p0Vector, pClass1 = trainNativeBayes(bagWordVector,classOfPost)
vector = bagOfWords2Vector(vocabList, ['love','my'] )
print(classifyNativeBayes(vector,p1Vector , p0Vector, pClass1))