import time
import random
import math
import subprocess

def nextprime(nbit):
    sum=0
    for i in range(nbit-2):
        e=random.random()*10
        e=int(e)
        sum=sum + e*2**i
        #print (sum,sum.bit_length())

    x=subprocess.Popen(["sh","-c", "./nextprime.sh " +str(sum)], stdout=subprocess.PIPE).communicate()[0]
    x=int(x[:-1])
    return (x,x.bit_length())

def ord(x,n):
    x=x%n
    s=x
    flag=1

    expn=8
    coeff=1

    count=0
    aa=[]
    nn=n.bit_length()
    start_time=time.time()
    #while(flag):
    for i in range(coeff*10**expn):
        s=pow(s,2,n)
        count=count+1
        #print(count)
        if(count%(coeff*10**(expn-2))==0):
            now=abs(start_time - time.time())
            print("made",  count, "in",now , "seconds with a", nn,"bit length of module"   )  
            aa.append(now)
    return aa


def mcm(a,b):
    g=math.gcd(a,b)
    return a*b/g


nbit=100
list={}

towrite="did 10^8 squaring and recorded data once every 10^6; therefore 100 mesurements. Various bit lengths from 100 to 2000 (inrc. by 100)"  
while (nbit<2048):
#while (nbit<200):
    p=nextprime(nbit/2)[0]
    q=nextprime(nbit/2)[0]
    n=p*q
    e=random.randrange(12,n)
    list[str(n.bit_length())]=ord(e,n)
    nbit=nbit+100

f=open("values.txt",'a' )
#f.write(towrite)
f.write(str(list))
f.close()

# to import, do 
# import ast
# f=open('values.txt','r')
# x=f.read()
# and evaluate the file with
# ast.literal_eval(x)
