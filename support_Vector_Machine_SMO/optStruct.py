from numpy import shape , mat, zeros, exp
class optStruct:
    def __init__(self, inputData, inputLabels, C = 0.6, toler = 0.001,maxIter = 40, kPara = (('lin',0))):
        self.X = inputData
        #训练数据特征
        self.y = inputLabels
        #训练数据标签
        self.C = C
        #SVM常数参数
        self.toler = toler
        #SVM参数_容忍度
        self.maxIter = maxIter
        #SVM参数_最大迭代次数
        self.numOfData = list(shape(inputData))[0]
        #训练样本数目
        self.numOfFeature = list(shape(inputData))[1]
        #训练样本特征数
        self.alphas =  mat(zeros((self.numOfData,1)))
        #超参数
        self.b = 0
        #bias参数
        self.eCache = mat(zeros((self.numOfData,2)))
        #eCache是误差缓存
        self.kPara = kPara
        #核函数相关参数
        self.K = mat(zeros((self.numOfData,self.numOfData)))
        #初始化核函数矩阵
        self.K = self.kernelTrans()
        #开始构造核函数矩阵

    def kernelTrans(self):
        #输入参数不需要再输一次kPara了，self会自己参考整个初始化结构
        if self.kPara[0] == 'lin':
            #K默认初始化时就已先设置成线性形式
            for i in range(self.numOfData):
                self.K[:, i] = self.X * self.X[i, :].T
            return self.K
            #需要上return值的
        elif self.kPara[0] == 'rbf':
            for i in range(self.numOfData):
                for j in range(self.numOfData):
                    deltaRow = self.X[j,:] - self.X[i,:]
                    self.K[j,i] = deltaRow * deltaRow.T
            self.K = exp(self.K/(-1 * self.kPara[1] ** 2))
            return self.K
        else:
            raise NameError('无法识别该核函数')