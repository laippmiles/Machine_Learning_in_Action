#现实用RSS爬虫并做朴素贝叶斯分析
from feedparser import parse
from RSS_ClassifyNativeBayes import localWord
from math import exp
print('Loading RSS data')
fromSfBay = parse('https://sfbay.craigslist.org/stp/index.rss')
fromNewYork = parse('https://newyork.craigslist.org/stp/index.rss')
print('Complate')
#就一行就能把数据读回来，简直厉害
# 1:from SfBay
# 0:from NewYork
#训练并测试
vocabList, pFromSfBayVector , pFromNewYorkVector = localWord(fromSfBay,fromNewYork)
#显示词频
thresholdFromSfBayVector = (min(pFromSfBayVector) + max(pFromSfBayVector)) / 2.0
thresholdFromNewYorkVector = (min(pFromNewYorkVector) + max(pFromNewYorkVector)) / 2.0

topFromSfBay = []
topFromNewYork = []

for wordIndexForSfBay in range(len(pFromSfBayVector)):
    if pFromSfBayVector[wordIndexForSfBay] > thresholdFromSfBayVector :
        topFromSfBay.append((vocabList[wordIndexForSfBay],pFromSfBayVector[wordIndexForSfBay]))

sortedOfTopFromSfBay = sorted(topFromSfBay , key=lambda pair : pair[1] , reverse = True)

for wordInSfBay in sortedOfTopFromSfBay:
    print(wordInSfBay[0],exp(wordInSfBay[1]))

print('-'*20)

for wordIndexForNewYork in range(len(pFromNewYorkVector)):
    if pFromNewYorkVector[wordIndexForNewYork] > thresholdFromNewYorkVector:
        topFromNewYork.append((vocabList[wordIndexForNewYork], pFromNewYorkVector[wordIndexForNewYork]))

sortedOfTopFromNewYork = sorted(topFromNewYork, key=lambda pair: pair[1], reverse=True)

for wordInForNewYork in sortedOfTopFromNewYork:
    print(wordInForNewYork[0], exp(wordInForNewYork[1]))

#不去高频词的话没啥差别，去了高频词又会损失信息。反正要取舍