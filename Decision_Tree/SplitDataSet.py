def SplitDataSet(Dataset,IndexOfFeature,ValueOfFeature):
    SubSataSet = []
    for DataVector in Dataset:
        if DataVector[IndexOfFeature] == ValueOfFeature:
            ReducedDataVector = DataVector[:IndexOfFeature]
            ReducedDataVector.extend(DataVector[IndexOfFeature+1:])
            SubSataSet.append(ReducedDataVector)
    return SubSataSet