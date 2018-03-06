def selectJrand(i,numOfData):
    #这个子函数用来随机选择第i个alpha参数对应的alpha参数j（i不等于j）
    from random import uniform
    j = i
    while(j == i):
       j = int(uniform(0,numOfData))
    return j

def cilpAlpha(alphaJ,H,L):
    #H:限幅最大值，L:限幅最小值
    if alphaJ > H:
        alphaJ = H
    elif alphaJ < L:
        alphaJ = L
    return alphaJ
