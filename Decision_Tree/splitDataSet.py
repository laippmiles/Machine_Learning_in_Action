def splitDataSet(dataSet,indexOfFeature,valueOfFeature):
    subSataSet = []
    for dataVector in dataSet:
        if dataVector[indexOfFeature] == valueOfFeature:
            ReducedDataVector = dataVector[:indexOfFeature]
            ReducedDataVector.extend(dataVector[indexOfFeature+1:])
            subSataSet.append(ReducedDataVector)
    return subSataSet