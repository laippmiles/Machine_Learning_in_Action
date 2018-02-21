def KNN(Input,DataSet,Labels,K):
    from numpy import tile,shape,argsort
    from operator import itemgetter
    DataSetSize = DataSet.shape[0]
    #也能写作shape(DataSet)[0]，但IDE会报错
    DiffMat = tile(Input,(DataSetSize,1)) - DataSet
    SqDiffMat = DiffMat**2
    SqDistances = SqDiffMat.sum(axis=1)
    #加入axis=1以后就是将一个矩阵的每一行向量相加
    Distances = SqDistances**0.5
    SortDistanceIndex = Distances.argsort()
    #argsort函数是Numpy模块中的函数,返回的是数组值从小到大的索引值
    ClassCount = {}
    for i in range(K):
        VoteLable = Labels[SortDistanceIndex[i]]
        ClassCount[VoteLable] = ClassCount.get(VoteLable,0)+1
        #get(VoteLable,0)只取VoteLable中的值，如没有VoteLable这个键，赋初值0
    SortClassCount = sorted(ClassCount.items(),key=itemgetter(1),reverse=True)
    #在3.x 里 用 items()替换iteritems() ，可以用于 for 来循环遍历。
    return SortClassCount[0][0]
