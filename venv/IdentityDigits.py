import os
from numpy import *
import operator

def readFile(filename):

    labels=[]
    index=0

    lists=os.listdir(filename)

    dataSet = zeros((len(lists), 1024))
    for i in range(len(lists)):
        path=os.path.join(filename,lists[i])
        # print(path)
        # print("\n")

        digitname=path.split('\\')
        labels.append(digitname[-1][0:1])
        # print(labels,file=fow)
        fo=open(path)
        filecontend=fo.read()
        filecontend=filecontend.replace("\n","")
        # print(filecontend)
        # print("\n")
        singleData=list(map(int,filecontend))
        dataSet[index:]=singleData
        index+=1
    return dataSet,labels

def judge(testDigit,dataSet):
    f=open("out.txt","a+")
    dataSize=dataSet.shape[0]
    testTwo=tile(testDigit,(dataSize,1))
    testTwo=testTwo-dataSet
    testTwo=testTwo**2
    testTwo=testTwo.sum(axis=1)
    testTwo = testTwo ** 0.5
    classCount={}
    testTwo=testTwo.argsort()
    for i in range(3):
        voteIlabel=labels[testTwo[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedClassCount[0][0],file=f)



def getTest(filename,dataSet):
    lists = os.listdir(filename)
    # print(len(lists))
    for i in range(len(lists)):
        path = os.path.join(filename, lists[i])
        fo = open(path)
        filecontend = fo.read()
        filecontend = filecontend.replace("\n", "")
        # print(filecontend)
        singleData = list(map(int,filecontend))
        judge(singleData,dataSet)



dataSet,labels=readFile(".\digits\\trainingDigits")
# print(dataSet)
testDigits=getTest(".\digits\\testDigits\sss",dataSet)
