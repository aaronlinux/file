#!/usr/bin/python
#coding=utf-8
###########################

import math
#输入一个数组，该函数把它变成0-1的区间的数组。
###########################################################################
def biaozhun(x,maxd,mind):
  output=[]
  for i in x:
    i=float(i)
    out=(i-float(mind))/float((maxd-mind))
    output.append(out)
  return output
###########################################################################
#输入一个0-1区间的数组，该函数把它还原成原来的数组，前提是给定确定的极值（最大，最小）。
def arcbiaozhun(input,maxd,mind):
  output=[]
  for i in input:
    i=float(i)
    out=i*(float(maxd)-float(mind))+float(mind)
    output.append(out)
  return output
###########################################################################
#输入一个数字，返回这个数字的激活值。
def active(x):
  y=1/(1+math.e**(-x))
  return y
###########################################################################
def mdata(x):#取文件中数组x中最大值和最小值
  data=[]
  n=len(x)#行
  m=len(x[0])#列
  for i in range(0,n):
      for j in range(0,m):
          data.append(x[i][j])
  num=len(data)
  maxdata=float(data[0])
  mindata=float(data[0])
  for b in range(0,num):
      if maxdata<float(data[b]):
          maxdata=float(data[b])
      else:
          maxdata=maxdata
      if mindata>float(data[b]):
          mindata=float(data[b])
      else:
          mindata=mindata
  mdata=[maxdata,mindata]
  return mdata
###########################################################################
def size(x):
    n=len(x)#行，就是文件里的一行
    m=len(x[0])#列
    return m,n
###########################################################################
def form(source,layer):
    n=len(source)
    x=[]
    for i in range(0,n):
        tmp=0
        for j in range(0,n):
            tmp+=float(source[j])*float(layer[i][j])
        x.append(tmp)
    return x
###########################################################################
def readdata(fileopened):#读数据文件到二维数组
  data=[]
  dataf=[]
  answer=[]
  while True:
    i=fileopened.readline()
    if len(i)==0:
      break
    else:
      arg=i.split()
      dataf.append(arg)
      x=arg.pop()
      data.append(arg)
      answer.append(x)
  return data,dataf,answer
###########################################################################
def passm(sc,layer):#两个参数都是数组
  sr=form(sc,layer)
  tmp=[]
  for i in sr:
    x=active(i)
    tmp.append(x)
  return tmp
###########################################################################

###########################################################################
def back(n,maxd,mind):
  m=float(n)*(maxd-mind)+mind
  return m
###########################################################################
def fnerror(output,answer):
  m=(float(answer)-float(output))*float(output)(1-float(output))
  return m
###########################################################################

###########################################################################
def change(error,output):
  x=(0.2)*float(error)*float(output)
  return x
###########################################################################
#这个是主文件
f=open("/Users/liusong/Documents/a.txt","r")#打开文件。
data=readdata(f)#读文件到数组。
dataf=data[1]
answerf=data[2]#读取文件答案到数组。
data=data[0]
mind=mdata(dataf)[1]#取得最大值。
maxd=mdata(dataf)[0]#取得最小值。
col=size(data)[0]
row=size(data)[1]
bzdata=[]
for i in data:
    ata=biaozhun(i,maxd,mind)
    bzdata.append(ata)
answer=biaozhun(answerf,maxd,mind)
print answer,col,row
inputdata=bzdata
f.close
#完成初始化的数据载入。
layer=[[[0.5 for sc in range(0,col)] for sr in range(0,col)] for t in range(0,col)]
finallayer=[0.5 for fn in range(0,col)]
#完成新的节点参数的初始化。
count=0
for j in inputdata:#对于每新的一行数据"
    print "新的一行数据的answer是",answer
    count+=1
    for times in range(0,col):#对于每个层,就是每一列的node
        j=passm(j,layer[times])
        final=0
        for fncount in range(0,col):
          final+=j[fncount]*finallayer[fncount]
          finalres=active(final)
        result=back(finalres,maxd,mind)
        dif=result-answer[count-1]
        print dif
#        print finallayer
#        for fncount in range(0,col):#对于每一个输出节点。          
#          print finallayer

###########################################################################
