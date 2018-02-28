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
    from getNumLeafs import getNumLeafs
    from getTreeDepth import getTreeDepth
    numLeafs = getNumLeafs(tree)
    depth = getTreeDepth(tree)
    firstStr = list(tree.keys())[0]
    centerPosition = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalWidth, plotTree.yOff)
    plotMidText(centerPosition, parentPosition, nodeTxt)
    plotNode(firstStr, centerPosition, parentPosition, decisionNode)
    secondDict = tree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalDepth

    for key in secondDict.keys():
        if type(secondDict[key]) is dict:
            plotTree(secondDict[key],centerPosition, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalWidth
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPosition, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), centerPosition, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalDepth

def createPlot(tree):
    fig = pyplot.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks = [],yticks = [])
    createPlot.ax1 = pyplot.subplot(111,frameon = False ,**axprops)
    #frameon:Frame on =.=
    plotTree.totalWidth = float(getNumLeafs(tree))
    plotTree.totalDepth = float(getTreeDepth(tree))

    plotTree.xOff = -0.5/plotTree.totalWidth
    plotTree.yOff = 1.0
    #追踪下一个节点的坐标位置

    plotTree(tree, (0.5,1.0), '')
    #根节点坐标

    pyplot.show()