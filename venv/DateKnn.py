from numpy import *
import operator

inX=[0,0,0]
group = array([[0.8,400,0.5],[12,134000,0.9],[0,20000,1.1],[67,32000,0.1]])
labels=['1','3','2','2']
dataSetSize=group.shape[0]
minVal=group.min(0)
maxVal=group.max(0)
range=maxVal-minVal
group=group-minVal
group=group/range
diffMat=tile(inX,(dataSetSize,1))-group
diffMat=diffMat**2
diffMat=diffMat.sum(axis=1)
diffMat=diffMat**0.5
print(diffMat)
sortedgroup=diffMat.argsort()
print(sortedgroup)
classCount={}


# for i in range(3):
voteIlabel=labels[sortedgroup[0]]
classCount[voteIlabel]=classCount.get([voteIlabel],0)+1
# sortedClassCount=sorted(ClassCount.items(),key=operator.itemgetter(1),reverse=True)
# print(sortedClassCount[0][0])

