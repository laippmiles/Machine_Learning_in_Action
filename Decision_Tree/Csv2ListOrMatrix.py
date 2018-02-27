def Csv2ListOrMatrix(path,type = 'Matrix'):
    #采用默认参数，这样只填第一个参数也能使用这个子函数
    #默认输出的是数据的矩阵形式
    from pandas import read_csv
    from numpy import matrix
    Data = read_csv(path,header=None)
    #现有的数据集头部都为空，所以要加上"header=None"
    if type == 'List':
        Data = list(row.tolist() for index,row in Data.iterrows())
        return Data
    #用这个语句可以将CSV的数据转化为嵌套列表
    else:
        Data = matrix(Data)
        return Data
    #加上这句可以转为矩阵，python的矩阵里头可以存字符串