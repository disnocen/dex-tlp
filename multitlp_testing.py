import math
import time

Infinity=math.inf

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

def isprime(n):  # First the primality test
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
            break
    else:
        return True

def nthprime(n):   # then generic code for nth prime number
    x=[]
    j=2
    while len(x)<n:
        if (isprime(j)) == True:
            x.append(j)
        j =j+1
    return x[n-1]

def jacobi(a, n):
#https://www.johndcook.com/blog/2019/02/12/computing-jacobi-symbols/
    if a>n:
        a %=n
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == 3 % 4 == 3:
            t = -t
        n=int(n) # needed bc n is a float after the steps
        a %= n
    if n == 1:
        return t
    else:
        return 0

def isNonQuadratic(d,p,q):
    # d is non quadratic mod N iff  d non quadratic mod p AND non quadratic mod q
    # i.e. (d|p)=-1 or (d|q)=-1
    # see https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html

    if (jacobi(d, p)!=-1 or jacobi(d,q)!=-1):
        return True
    else:
        # print(d,"is quadratic because")
        # print("d|p=",jacobi(d,p))
        # print("d|q=",jacobi(d,q))
        return False

def rswGenExp(t, p, q):
   n = p*q
   phi = (p-1)*(q-1)
   return pow(2, t, phi)

def rswGenPuzzle(mex,a,t,p,q):
    n=p*q
    start_time=time.time()
    e=rswGenExp(t,p,q)
    a=a%n
    A=pow(a,e,n) 
    num=int.from_bytes(mex,'big')
    end_time=time.time()
    if(num<n):
        puzz=(num+A)%n
        return (a,t,puzz,n,end_time-start_time)
        
    else:
        print("num",num) 
        print("n  ",n) 
        return 0

def bmGenExp(t, p, q):
    n = (p+1)*(q+1)
    phi = mcm(p-1,q-1)
    e=pow(2, t, phi)
    return e

def Phi(x,y,n):
    return (((1+x)%n)*InvMod(y,n))%n

def InvPhi(m,D,n):
    x=Mod(Mod((m^2+D),n)*InvMod(m^2-D,n),n)
    y=Mod(Mod((2*m),n)*InvMod(m^2-D,n),n)
    return (x,y)

def Dgen(mx,my,n):
    d=Mod(Mod(pow(mx,2)-1,n)*pow(my,-2,n),n)
    return d 

def bmGenPuzzle(mex_x,a,t,p,q,h):
    mex_y=1
    n=p*q
    start_time=time.time()
    e=bmGenExp(t,p,q)
   
    num=int.from_bytes(mex_x,'big')
    d=Dgen(num,mex_y,n)
    print("computing jacoby")
    while not isNonQuadratic(d,p,q):
        #print("jacobi is:\t",jacobi(d,n),"mex_y is\t",mex_y,end="\r")
        mex_y+=1
        # print(d,end="\r")
        d=Dgen(num,mex_y,n)

    M=Phi(num,mex_y,n)
    a=a%n
    A=hdpotmod(e,h,d,a,n)
    end_time=time.time()
    if(num<n):
        puzz=Mod(M+A,n)
        return (a,t,puzz,n,h,d,end_time-start_time, num,A)
    else:
        print("num",num) 
        print("n  ",n) 
        return 0

# def bmGenPuzzle(mex_x,a,t,p,q,h):
#     mex_y=1
#     n=p*q
#     start_time=time.time()
#     e=bmGenExp(t,p,q)
   
#     num=int(mex_x.encode('ascii').hex(),16)
#     d=Dgen(num,mex_y,n)
#     print("computing jacoby")
#     while jacobi(d,n)!=-1:
#         #print("jacobi is: ",jacobi(d,n))
#         mex_y+=2
#         #print(d)
#         d=Dgen(num,mex_y,n)

#     M=Phi(num,mex_y,n)
#     print ("M is ", M)
#     a=a%n
#     A=hdpotmod(e,h,d,a,n)
#     print("during generation, A is", A)

#     print("during generation num is",num )
#     end_time=time.time()
#     if(num<n):
#         puzz=(num+A)%n
#         return (a,t,puzz,n,h,d,end_time-start_time, num,A)
#     else:
#         print("num",num) 
#         print("n  ",n) 
#         return 0

def rswSolExp(t, n):
   s = 2
   for i in range(t):
       s = pow(s, 2, n)
   return s

def rswSolExp2(a,t, n):
   s = a
#    t1=int(t/100.0)
   for i in range(t):
       s = pow(s, 2, n)

   return s



def rswSolPuzzle(x):
    if(x!=0):
        a=x[0]
        t=x[1] 
        puzz=x[2] 
        n=x[3] 
#        e=rswSolExp(t,n) 
#        A=pow(a,e,n) 
        start_time=time.time()
        A=rswSolExp2(a,t,n) 
        end_time=time.time()
        num=(puzz-A)%n
        num=hex(num) 
        #print(num)
        return (bytes.fromhex(num[2:]),end_time-start_time)
    else:
        return "puzzle submitted is broken"  

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
   
#    s = a
#    x=s
#    for i in range(t):
#        #x = pow(s, 2, n)
#        x=hdpotmod(2,h,d,x,n) #x0^n mod mod
#    return s

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
        M=(puzz-A)%n
        num=hexa(M-1)
        return bytes.fromhex(num)
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
   
   
   
   
   
   
    # if (n==0):
    #     return Infinity
    # else:
    #     return hdprodmod(z,hdpotmod(n-1,h,d,z,mod),h,d,mod)

# def pona(x0,esp,h,d,mod): #x0^esp with ^=oper
#     z=bin(x0)[2:]
#     n=len(z)
#     v=[0] * n
#     v[0]=x0
#     for i  in range(2,n):
#         v[i]= oper[v[i-1], v[i-1]]

def main():
    pass

if __name__ == '__main__':
    main()

