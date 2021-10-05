import time
import random
import math
import subprocess
from multitlp_testing import *

def nextprime(nbit):
    sum=0
    for i in range(nbit+1):
        e=random.random()*10
        e=int(e)
        sum=sum + e*2**i

    x=subprocess.Popen(["sh","-c", "./nextprime.sh " +str(sum)], stdout=subprocess.PIPE).communicate()[0]
    x=int(x[:-1])
    return (x,x.bit_length())

def genN(nbit):
    halfnbit=int(nbit/2)
    (p,pnbit) = nextprime(halfnbit)
    (q,qnbit) = nextprime(halfnbit)
    return (p,q,p*q,pnbit+qnbit)

def getGoodD(p,q):
    d=2;
    while (jacobi(d,p*q)==1):
        d=d+1
#        print("trying d=",d )


    return d

nbit=100
list={}

while (nbit<2200):
    print(nbit)
    (p,q,n,nbit)=genN(nbit)
    d=getGoodD(p,q)
    print("for p =",p,"and q =",q,"we have that d=",d )
    list[nbit]=(p,q,n,d)
    nbit=nbit+100

f=open("primes.txt",'a' )
f.write(str(list))
f.close()

# to import, do 
# import ast
# f=open('values.txt','r')
# x=f.read()
# and evaluate the file with
# ast.literal_eval(x)
