#coding=utf-8
from matplotlib import pyplot
from getNumLeafs import getNumLeafs
from getTreeDepth import getTreeDepth

arrowArgs = dict(arrowstyle="<-")
#这里曾经打成了arrowArgs = dict(arrowsyle="<-")
#少了一个字母，程序不认...
#arrowstyle是annotate里的关键参数名，用的时候要确认好。IDE好像不会负责帮忙联想这一块
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")

def plotNode(nodeTxt, centerPosition, parentPosition, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPosition,  xycoords='axes fraction',
                            xytext=centerPosition, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrowArgs)

def plotMidText(centerPosition, parentPosition, txtString):
    xMid = (parentPosition[0] - centerPosition[0])/2.0 + centerPosition[0]
    yMid = (parentPosition[1] - centerPosition[1])/2.0 + centerPosition[1]
    createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(tree,parentPosition, nodeTxt):
    numLeafs = getNumLeafs(tree)
    #只需要计算叶节点数就够了
    firstStr = list(tree.keys())[0]
    centerPosition = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalWidth, plotTree.yOff)
    #计算下一个节点的中央坐标
    plotMidText(centerPosition, parentPosition, nodeTxt)
    #显示文本
    plotNode(firstStr, centerPosition, parentPosition, decisionNode)
    #计算节点，其实计算节点这个子函数只有一句指令，每个子树最顶端都是一个决策节点。
    secondDict = tree[firstStr]
    #取目前节点下的子树，子树也是个字典（没到最后一层时是嵌套字典）
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalDepth
    ##求下一层的y坐标，在上一层的基础上下移

    for key in secondDict.keys():
        #扫描子树嵌套字典下的每个键（对应树的分支）
        if type(secondDict[key]) is dict:
            plotTree(secondDict[key],centerPosition, str(key))
            #子树没到底，继续递归
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalWidth
            #每个待画节点的坐标，在上一分支的基础上右移
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPosition, leafNode)
            #到底后画叶节点
            plotMidText((plotTree.xOff, plotTree.yOff), centerPosition, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalDepth

def createPlot(tree):
    fig = pyplot.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks = [],yticks = [])
    #带入可变参数？
    createPlot.ax1 = pyplot.subplot(111,frameon = False ,**axprops)
    #frameon:Frame on =.=
    plotTree.totalWidth = float(getNumLeafs(tree))
    plotTree.totalDepth = float(getTreeDepth(tree))

    plotTree.xOff = -0.5/plotTree.totalWidth
    plotTree.yOff = 1.0
    #追踪下一个节点的坐标位置
    #plotTree里头需要用到的初值

    plotTree(tree, (0.5,1.0), '')
    #plotTree是递归程序，只用调用一次，调用时赋初值即可

    #根节点坐标

    pyplot.show()