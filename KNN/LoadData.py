def LoadData(path,NumOfPixel_height,NumOfPixel_width):
    from os import listdir
    import Img2Vector
    from numpy import zeros
    HandWriteLables = []
    FileList = listdir(path)
    NumOfData = len(FileList)
    DataMat = zeros((NumOfData, NumOfPixel_height * NumOfPixel_width))
    for i in range(NumOfData):
        FileNameStr = FileList[i]
        #得到第i个样本对应的文件名
        FileStr = str(FileNameStr.split('.')[0])
        #以.分割，在前头的是文件名，后面的是文件格式（用不着）
        #加入str，要不这个傻逼IDE会报错（其实不加也能跑）
        ClassNumStr = FileStr.split('_')[0]
        #以_分割，在前头的是这个样本对应的类别
        HandWriteLables.append(ClassNumStr)
        #加入标签集
        DataMat[i,:] = Img2Vector.Img2Vector('trainingDigits/%s' % FileNameStr, NumOfPixel_height, NumOfPixel_width)
    return HandWriteLables,DataMat,NumOfData