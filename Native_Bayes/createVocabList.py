def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    vocabList = list(vocabSet)
    return vocabList  # , len(vocabList
    #词汇量词数先不输出来了