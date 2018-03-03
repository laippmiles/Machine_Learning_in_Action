from feedparser import parse
from datetime import datetime
from loadOrSaveFile import saveFile
from re import sub
print('Loading RSS data')
fromSfBay = parse('https://sfbay.craigslist.org/stp/index.rss')
fileNameSfBay = 'SfBay_' + sub('[:.\s]','_',str(datetime.now())) + '.txt'
#去把蟒蛇书P137-142看一遍背下来吧...
saveFile(fromSfBay,fileNameSfBay)

fromNewYork = parse('https://newyork.craigslist.org/stp/index.rss')
fileNameNewYork  = 'NewYork_' +sub('[:.\s]','_',str(datetime.now())) + '.txt'
saveFile(fromNewYork,fileNameNewYork)
print('Complate')