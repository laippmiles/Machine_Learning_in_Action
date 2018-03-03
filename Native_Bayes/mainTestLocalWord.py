#现实用RSS爬虫并做朴素贝叶斯分析
from RSS_ClassifyNativeBayes import localWord
from loadOrSaveFile import loadFile
from sys import path
print(path)
path = r'D:\桌面\18_spring\机器学习实战\ML-in-Action-Code-and-Note-master\Machine_Learning_in_Action\someUsefulCode\dataOfRSS'
fileNameSfBay = r'\SfBay_2018-03-03_21_57_16_407572.txt'
fileNameNewYork = r'\NewYork_2018-03-03_21_57_21_949788.txt'
fromSfBay = loadFile(path + fileNameSfBay)
fromNewYork = loadFile(path + fileNameNewYork)
#就一行就能把数据读回来，简直厉害
# 1:from SfBay
# 0:from NewYork
#训练并测试
vocabList, pFromSfBayVector , pFromNewYorkVector = localWord(fromSfBay,fromNewYork)
#显示词频
thresholdFromSfBayVector = (min(pFromSfBayVector) + max(pFromSfBayVector))
thresholdFromNewYorkVector = (min(pFromNewYorkVector) + max(pFromNewYorkVector))

topFromSfBay = []
topFromNewYork = []

for wordIndexForSfBay in range(len(pFromSfBayVector)):
    if pFromSfBayVector[wordIndexForSfBay] > thresholdFromSfBayVector :
        topFromSfBay.append((vocabList[wordIndexForSfBay],pFromSfBayVector[wordIndexForSfBay]))

sortedOfTopFromSfBay = sorted(topFromSfBay , key=lambda pair : pair[1] , reverse = True)
sortedOfTopFromSfBay = sortedOfTopFromSfBay[int(len(sortedOfTopFromSfBay)/5):int(len(sortedOfTopFromSfBay)/5)+10]
for wordInSfBay in sortedOfTopFromSfBay:
    print(wordInSfBay[0])

print('-'*20)

for wordIndexForNewYork in range(len(pFromNewYorkVector)):
    if pFromNewYorkVector[wordIndexForNewYork] > thresholdFromNewYorkVector:
        topFromNewYork.append((vocabList[wordIndexForNewYork], pFromNewYorkVector[wordIndexForNewYork]))

sortedOfTopFromNewYork = sorted(topFromNewYork, key=lambda pair: pair[1], reverse=True)
sortedOfTopFromNewYork = sortedOfTopFromNewYork[int(len(sortedOfTopFromNewYork)/5):int(len(sortedOfTopFromNewYork)/5)+10]
for wordInForNewYork in sortedOfTopFromNewYork:
    print(wordInForNewYork[0])

#不去高频词的话没啥差别，去了高频词又会损失信息。反正要取舍