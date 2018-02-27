def CalShannonEnt(Dataset):
    from math import  log
    NumOfData = len(Dataset)
    LabelCounts = {}
    for DataVector in Dataset:
        ClassOfData = DataVector[0]
        #个人习惯把标签集放第一列
        if ClassOfData not in LabelCounts.keys():
        #如果目前样本信息集里头没有该类别的相关信息
            LabelCounts[ClassOfData] = 0
            #进行初始化
        LabelCounts[ClassOfData] +=1
    #上述过程记录了样本集每类样本的分布情况
    ShannonEnt = 0
    for key in LabelCounts:
        prob = float(LabelCounts[key])/NumOfData
        ShannonEnt -= prob * log(prob,2)
    return ShannonEnt