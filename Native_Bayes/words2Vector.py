def setOfWords2Vector(vocabList,dataSet):
    #这个子函数调用一次只能处理一个样本
    dataVector = [0] * len(vocabList)
    #建立一个长度和词汇库相同的，初值全部设为0的列表作为表达一个样本用词情况的向量

    for word in dataSet:
        if word in vocabList:
            dataVector[vocabList.index(word)] = 1
            #如果某词在词汇库，取其在词汇库上的索引，向量相应位置置1
            #这个子函数是词集模型，向量中只包含是否使用了某词的信息，不包含词频信息。
        else:
            print('%s is not in vocablist.' %word)
            #vocabList.append(word)
            #dataVector.append(1)
            #试着加入新词汇追加功能看看,后续有点麻烦，先跳过

    return dataVector


def bagOfWords2Vector(vocabList,dataSet):
    #这个子函数调用一次只能处理一个样本
    dataVector = [0] * len(vocabList)
    #建立一个长度和词汇库相同的，初值全部设为0的列表作为表达一个样本用词情况的向

    for word in dataSet:
        if word in vocabList:
            dataVector[vocabList.index(word)] += 1
            #如果某词在词汇库，取其在词汇库上的索引，向量相应位置置1
            #这个子函数是词袋模型，向量中包含是否使用了某词的信息和词频信息。
            #实际上实现时之比词集模型多了一个加号
        else:
            print('%s is not in vocablist.' %word)

    return dataVector