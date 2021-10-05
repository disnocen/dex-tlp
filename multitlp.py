import math
import time

Infinity=math.inf

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

def rswGenExp(t, p, q):
   n = p*q
   phi = (p-1)*(q-1)
   return pow(2, t, phi)

def rswGenPuzzle(mex,a,t,p,q):
    n=p*q
    e=rswGenExp(t,p,q)
    a=a%n
    A=pow(a,e,n) 
    num=int(mex.encode().hex(),16)
    if(num<n):
        puzz=(num+A)%n
        return (a,t,puzz,n)
    else:
        print("num",num) 
        print("n  ",n) 
        return 0

def bmGenExp(t, p, q):
   n = p*q
   phi = (p+1)*(q+1)
   return pow(2, t, phi)

def bmGenPuzzle(mex,a,t,p,q,h,d):
    n=p*q
    e=bmGenExp(t,p,q)
    a=a%n
    A=hdpotmod(e,h,d,a,n)
    num=int(mex.encode().hex(),16)
    if(num<n):
        puzz=(num+A)%n
        return (a,t,puzz,n,h,d)
    else:
        print("num",num) 
        print("n  ",n) 
        return 0

def rswSolExp(t, n):
   s = 2
   for i in range(t):
       s = pow(s, 2, n)
   return s

def rswSolExp2(a,t, n):
   s = a
   t1=int(t/100.0)
   for i in range(t):
       s = pow(s, 2, n)
       if ( s == a):
           print("ord of ",a,"is",i)
       if (i%t1==0):
           print("we are at ",int(i/t1),"%")
           print(time.time())

   return s

def bmSolExp(t, n):
   s = 2
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
        A=rswSolExp2(a,t,n) 
        num=(puzz-A)%n
        num=hex(num) 
        return bytes.fromhex(num[2:]).decode('ascii')
    else:
        return "puzzle submitted is broken"  

def bmSolPuzzle(x):
    if(x!=0):
        a=x[0]
        t=x[1] 
        puzz=x[2] 
        n=x[3] 
        h=x[4]
        d=x[5]
        e=bmSolExp(t,n) 
        A=pow(a,e,n) 
        num=(puzz-A)%n
        num=hex(num) 
        return bytes.fromhex(num[2:]).decode('ascii')
    else:
        return "puzzle submitted is broken"  

def Mod(a,mod):
    return a%mod

def InvMod(a,mod):
    return pow(a,-1,mod)

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

def hdpotmod(n,h,d,z,mod): #z^n mod mod
    if (n==0):
        return Infinity
    else:
        return hdprodmod(z,hdpotmod(n-1,h,d,z,mod),h,d,mod)

def main():
    pass

if __name__ == '__main__':
    main()

