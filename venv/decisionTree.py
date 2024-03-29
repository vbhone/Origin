from math import log
def getEntropy(dataSet):
    dirFeature={}
    for example in dataSet:
        if example[-1] not in dirFeature.keys():
            dirFeature[example[-1]]=0
        dirFeature[example[-1]]+=1
    feature=0.0
    for key in dirFeature:
        prob = float(dirFeature[key])/len(dataSet)
        feature-=prob * log(prob,2)
    return feature




def chooseBestFeatureToSplit(dataSet):
    dataSize=len(dataSet[0])-1
    initBestFeature=getEntropy(dataSet)
    bestInfo=0
    bestFeature=-1
    for i in range(dataSize):
        featList=[example[i] for example in dataSet]
        uniqueVal=set(featList)
        newEntropy=0.0
        for value in uniqueVal:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannnonEnt(subDataSet)
        info=best
    return bestInfo



def splitDataSet(dataSet,axis,value):
    returnMat=[]
    for example in dataSet:
        if(example[axis]==value):
            subexample=example[:axis]
            subexample.extend(example[axis+1:])
            returnMat.append(subexample)
    return returnMat




def creattree(dataSet,labels):
    classList=[exampe[-1] for exampe in dataSet]
    if classList.count(classList[0])==len(classList) :
        return classList[0]
    if len(dataSet[0])==1:
        return maximum(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(dataSet[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=creattree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree





dataSet=[[1,1,'y'],[1,1,'y'],[1,0,'n'],[0,1,'n'],[0,1,'n']]
labels=["no surfacing","flippers"]
creattree(dataSet,labels)