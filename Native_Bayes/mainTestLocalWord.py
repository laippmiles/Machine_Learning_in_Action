#现实用RSS爬虫并做朴素贝叶斯分析
from feedparser import parse
from RSS_ClassifyNativeBayes import localWord
print('Loading RSS data')
fromSfBay = parse('https://sfbay.craigslist.org/stp/index.rss')
fromNewYork = parse('https://newyork.craigslist.org/stp/index.rss')
print('Complate')
#就一行就能把数据读回来，简直厉害
# 1:from SfBay
# 0:from NewYork
localWord(fromSfBay,fromNewYork)