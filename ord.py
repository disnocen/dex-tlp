import time
import random
import math

def ord(x,n,N):
    x=x%n
    s=x
    list=[]
    flag=1
    expn=7
    coeff=5
    count=0
    #while(flag):
    for i in range(coeff*10**expn):
        s=pow(s,2,n)
        count=count+1
        #print(count)
        if(count%(coeff*10**(expn-1))==0):
            print(count,"length of list is",len(list), "a is",x, "tentative",N )
            if(s in list):
                print("ord",x,"is",count)
                flag=0
                return count
                break
        list.append(s)
    return 'nada'


def mcm(a,b):
    g=math.gcd(a,b)
    return a*b/g

        
# prime list
# 63254647
# 63252961
# 56089981
# 74076757
# 74076689
# 74080301
# 74442869

p=74442869
q=56089981
n=p*q
print(n)
results={1:"nada"}
good=[]

for i in range(1,1000):
    time.sleep(3)
    print("new tentative!" )
    a=random.randrange(10,n)
    print(a)
    results[a]=ord(a,n,i)
    print(results[a])

print("finished test. counting")
for k in results:
    if(results[k]!='nada'):
        good.append(k)

print( "over 1000 test, good ones are in number of:", len(good))


# start_time=time.time()
# ord_x=ord(x,n)
# ord_y=ord(y,n)
# print ("ord",a,"will be",mcm(ord_x,ord_y))
# print("separate computation took",start_time - time.time(),"seconds" )
# 
# 
# start_time=time.time()
# ord_a=ord(a,n)
# print ("ord",a,"is",ord_a)
# print("ord_a computation took",start_time - time.time(), "seconds" )


