def Img2Vector(FileName,NumOfPixel_height,NumOfPixel_width):
    from numpy import zeros
    ReturnVector = zeros((1,NumOfPixel_height * NumOfPixel_width))
    FileRead = open(FileName)
    for i in range(NumOfPixel_height):
        #range（x）从0算起，共x个数
        LineStr = FileRead.readline()
        #这里只读一行就够了
        for j in range(NumOfPixel_width):
            ReturnVector[0,NumOfPixel_height*i+j] = int(LineStr[j])
    return ReturnVector