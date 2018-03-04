def LRClassify():
    from csv2ListOrMatrix import csv2ListOrMatrix
    from gradDescend import gradDescend,stocGradDescend,stocGradAscentPlus
    from numpy import shape, column_stack, ones
    from LRclassifyVector import LRclassVector
    # 载入数据
    path = r'D:\桌面\18_spring\机器学习实战\ML-in-Action-Code-and-Note-master\Machine_Learning_in_Action\Data'
    fileOfTrainData = r'\ecoli_0_1_4_7_vs_5_6\ecoli_0_1_4_7_vs_5_6-test1.csv'
    fileOfTestData = r'\ecoli_0_1_4_7_vs_5_6\ecoli_0_1_4_7_vs_5_6-test1.csv'
    train = csv2ListOrMatrix(path + fileOfTrainData)
    test = csv2ListOrMatrix(path + fileOfTestData)

    trainLabel = train[:, 0]
    trainData = train[:, 1:]
    testLabel = test[:, 0]
    testData = test[:, 1:]


    trainweights = stocGradAscentPlus(trainData, trainLabel)

    numOfTestData = list(shape(testData))[0]
    error = 0.0
    for i in range(numOfTestData):
        answer = LRclassVector(testData[i], trainweights)
        actual = testLabel[i]
        print(answer , '----', actual)
        if (answer != actual):
            error += 1

    acc = float(1 - error / numOfTestData)
    # 输出准确率
    print(acc)
    return acc
