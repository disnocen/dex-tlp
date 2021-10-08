import math
import time
import random


Infinity=math.inf


def jacobi(a, n):
#https://www.johndcook.com/blog/2019/02/12/computing-jacobi-symbols/
    assert(n > a > 0 and n%2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

def mcm(a,b):
    g=math.gcd(a,b)
    return a*b//g

def hexa(x):
    x=hex(x)
    x=x[2:]
    if len(x)%2==1:
        x='0'+x
    return x
    #return hex(x)[2:]

def Phi(x,y,n):
    #return (((1+x)%n)*InvMod(y,n))%n
    return Mod(Mod(1+x,n)*InvMod(y,n),n)

def InvPhi(m,D,n):
    x=Mod(Mod((pow(m,2,n)+D),n)*InvMod(pow(m,2,n)-D,n),n)
    # x=Mod(Mod((pow(m,2,n)+D),n)*InvMod(pow(m,2,n)-D,n),n)
    y=Mod(Mod(2*m,n)*InvMod(pow(m,2,n)-D,n),n)
    return (x,y)

def Dgen(mx,my,n):
    d=Mod(Mod(pow(mx,2)-1,n)*pow(my,-2,n),n)
    return d

def bmGenExp(t, p, q):
    n = (p+1)*(q+1)
    phi = mcm(p-1,q-1)
    e=pow(2, t, phi)
    return e

def bmGenPuzzle(mex_x,a,t,p,q,h):
    mex_y=1
    n=p*q
    start_time=time.time()
    e=bmGenExp(t,p,q)
   
    num=int(mex_x.encode('ascii').hex(),16)
    d=Dgen(num,mex_y,n)
    print("computing jacoby")
    while jacobi(d,n)!=-1:
        #print("jacobi is: ",jacobi(d,n))
        mex_y+=2
        #print(d)
        d=Dgen(num,mex_y,n)

    M=Phi(num,mex_y,n)
    print ("M is ", M)
    a=a%n
    A=hdpotmod(e,h,d,a,n)
    print("during generation num is",num )
    end_time=time.time()
    if(num<n):
        puzz=Mod(M+A,n)
        return (a,t,puzz,n,h,d,end_time-start_time, num,A)
    else:
        print("num",num) 
        print("n  ",n) 
        return 0

def bmSolExp(a,h,d,t, n):
    # for i in range(t):
    #     print("t is ",t,"\ts is",s)
    #     s = pow(s, 2, n)
    # return s
    s=a
    for i in range(t):
        #x = pow(s, 2, n)
        s=hdpotmod(2,h,d,s,n) #x0^n mod mod
    return s

def bmSolPuzzle(x):
    if(x!=0):
    #(a,t,puzz,n,h,d,end_time-start_time, num,A)
        a=x[0]
        t=x[1] 
        puzz=x[2] 
        n=x[3] 
        h=x[4]
        d=x[5]
        Agen=x[8]
        A=bmSolExp(a,h,d,t,n) 
        print("puzz is", puzz)
        print("A is\t", A)
        print("Agen is\t", Agen)
        print("d is", d)
        M=(puzz-A)%n
        print("M is", M)

        print("invphi", InvPhi(M,d,n))
        num= InvPhi(M,d,n)[0]
        print("during solution, num is", num)
        num=hexa(num)
        return bytes.fromhex(num).decode('ascii')
    else:
        return "puzzle submitted is broken"  

def Mod(a,mod):
    return a%mod

def InvMod(aaa,mod):
    return pow(aaa,-1,mod)

def hdprod(a,b,h,d):
    if (a==Infinity):
        return b
    elif (b==Infinity):
        return a
    elif (a+b+h ==0):
        return Infinity
    else:
        return (d + a*b)/(h+a+b) 

def hdprodn(a,b,d):
    return (d+a*b)/(a+b) 

def hdprodmod(a,b,h,d,mod):
    if (a==Infinity):
        return b
    elif (b==Infinity):
        return a
    elif (Mod(a+b+h, mod)==0):
        return Infinity
    else:
        return Mod((Mod(d, mod) + Mod(a,mod)*Mod(b,mod)) * InvMod( Mod(h,mod)+Mod(a,mod)+Mod(b,mod),mod),mod)

def hdpotmoddiff(n,h,d,z,mod): #z^n mod mod
    if (n == 0):
        return Infinity;
    temp = hdpotmoddiff(n/2,h,d,z,mod);
    if ((n%2)==0):
        return hdprodmoddiff(temp,temp,h,d,mod);
    else:
        return hdprodmoddiff(z,hdprodmod(temp,temp,h,d,mod),h,d,mod)



def hdpotmod(esp,h,d,x0,mod): #x0^esp mod mod
    z=bin(esp)[2:]
    #print(z)
    n=len(z)
    v=[0] * n
    v[0]=x0
    j=[]
    for i  in range(1,n):
        v[i]= hdprodmod(v[i-1],v[i-1],h,d,mod)
        #print("v[",i,"]=",v[i])
    for i in range(0,n):
        if (z[n-1-i]==str(1)):
            # print(nbit-i)
            j.append(v[i])
    #print(v)
    #print(j)
    
    n=len(j)
    ris=j[0]
    for i in range(1,n):
        ris =hdprodmod(j[i],ris,h,d,mod)
    return ris 

   
   
mydict= {106: (9736059014546863, 2945556800007421, 28678114835572062522265352270323, 2)}

mex='ciao'
t=10**6
bm=[]
for k in mydict.keys():
    nbit=k
    p=mydict[k][0]
    q=mydict[k][1]
    n=mydict[k][2]
    d=mydict[k][3]
    a=2#random.randrange(12,n)
    print("p is\t",p)
    print("q is\t",q)
    print("n is\t",n)
    # rswPuzzle=rswGenPuzzle(mex,a,t,p,q)
    # print("rsw gen time with",k,"bits is", rswPuzzle[4]  )
    # rsw.append((k,rswPuzzle[4]))
    bmPuzzle=bmGenPuzzle(mex,a,t,p,q,0)
    print("bm gen time with",k,"bits is", bmPuzzle[6]  )
    bm.append((k,bmPuzzle[6]))
    #print(rswSolPuzzle(rswPuzzle))
    print(bmSolPuzzle(bmPuzzle))
