def AutoNorm(DataSet):
        from numpy import zeros,shape,tile
        #这样载入使用模板的子函数时可以直接打名字
        MinVals = DataSet.min(0)
        MaxVals = DataSet.max(0)
        MaxMinusMin = MaxVals-MinVals
        NormDataSet = zeros(shape(DataSet))
        NumOfData = shape(DataSet)[0]
        NormDataSet = DataSet - tile(MinVals,(NumOfData,1))
        NormDataSet = NormDataSet/tile(MaxMinusMin,(NumOfData,1))
        return NormDataSet,MaxMinusMin,MinVals

