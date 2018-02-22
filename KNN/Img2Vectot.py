def Img2Vector(FileName,NumOfPixel):
    from numpy import zeros
    ReturnVector = zeros((1,NumOfPixel**2))
    FileRead = open(FileName)
    for i in range(NumOfPixel):
        #range（x）从0算起，共x个数
        LineStr = FileRead.readline()
        #这里只读一行就够了
        for j in range(NumOfPixel):
            ReturnVector[0,NumOfPixel*i+j] = int(LineStr[j])
    return ReturnVector