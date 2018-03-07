from numpy import shape , mat, zeros
class optStruct:
    def __init__(self, inputData, inputLabels, C = 0.6, toler = 0.001):
        self.X = inputData
        self.y = inputLabels
        self.C = C
        self.toler = toler
        self.numOfData = list(shape(inputData))[0]
        self.numOfFeature = list(shape(inputData))[1]
        self.alphas =  mat(zeros((self.numOfData,1)))
        self.b = 0
        self.eCache = mat(zeros((self.numOfData,2)))
        #eCache是误差缓存