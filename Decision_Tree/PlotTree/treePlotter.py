#coding=utf-8
#import operator
from matplotlib import pyplot
from getNumLeafs import getNumLeafs
from getTreeDepth import getTreeDepth

#绘制属性图
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrowArgs = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPosition, parentPosition, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPosition,  xycoords='axes fraction',
                            xytext=centerPosition, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrowArgs)

def plotMidText(centerPosition, parentPosition, txtString):
    xMid = (parentPosition[0]-centerPosition[0])/2.0 + centerPosition[0]
    yMid = (parentPosition[1]-centerPosition[1])/2.0 + centerPosition[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)

def plotTree(myTree, parentPosition, nodeTxt):
    numLeafs = getNumLeafs(myTree)  #计算树的宽度  totalW
    depth = getTreeDepth(myTree) #计算树的高度 存储在totalD
    #python3.x修改
    firstSides = list(myTree.keys())#firstStr = myTree.keys()[0]     #the text label for this node should be this
    firstStr = firstSides[0]  # 找到输入的第一个元素
    centerPosition = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalWidth, plotTree.yOff)#按照叶子结点个数划分x轴
    plotMidText(centerPosition, parentPosition, nodeTxt) #标注结点属性
    plotNode(firstStr, centerPosition, parentPosition, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalDepth #y方向上的摆放位置 自上而下绘制，因此递减y值

    for key in secondDict.keys():
        if type(secondDict[key]) is dict:#判断是否为字典 不是则为叶子结点
            plotTree(secondDict[key],centerPosition,str(key))        #递归继续向下找
        else:   #为叶子结点
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalWidth #x方向计算结点坐标
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPosition, leafNode)#绘制
            plotMidText((plotTree.xOff, plotTree.yOff), centerPosition, str(key))#添加文本信息
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalDepth #下次重新调用时恢复y

def createPlot(inTree): #主函数
    fig = pyplot.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = pyplot.subplot(111, frameon=False, **axprops)  # no ticks
    # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalWidth = float(getNumLeafs(inTree))
    plotTree.totalDepth = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalWidth
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    pyplot.show()
















