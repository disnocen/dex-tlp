import time
import random
import math
import subprocess
import ast
import numpy as np

def getreturns(x):
    list=[]
    for i in range(len(x)-1):
        list.append(x[i+1]-x[i])
    return list

def getstats(x):
    return (np.mean(x), np.std(x))
    

f=open('values.txt','r')
x=f.read()
x=ast.literal_eval(x)

vals={}
for i in x.keys():
    a=getreturns(x[i])
    b=getstats(a)
    vals[i]=b

f=open("analysis-values.txt",'a' )
f.write(str(vals))
f.close()
