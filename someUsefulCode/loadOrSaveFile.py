from pickle import dump,load
from shutil import move
def saveFile(data,fileName):
    fw = open(fileName,'wb')
    #write() argument must be str, not bytes出现这个的时候，将‘w’改为‘wb’即可
    dump(data,fw)
    fw.close()
    newpath = 'dataOfRSS\\' + fileName
    move(fileName,newpath)

def loadFile(fileName):
    fw = open(fileName,'rb')
    #open的默认模式是'r',ctrl+左键可以看到的
    return load(fw)