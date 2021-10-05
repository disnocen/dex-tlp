import math
import time

Infinity=math.inf
def Mod(a,mod):
    return a%mod

def InvMod(a,mod):
    return pow(a,-1,mod)

def hdprodmod(a,b,h,d,mod):
    if (a==Infinity):
        return b
    elif (b==Infinity):
        return a
    elif (Mod(a+b+h, mod)==0):
        return Infinity
    else:
        return Mod((Mod(d, mod) + Mod(a,mod)*Mod(b,mod)) * InvMod( Mod(h,mod)+Mod(a,mod)+Mod(b,mod),mod),mod)

def hdpotmoddiff(n,h=0,d,z,mod): #z^n mod mod; recursive version
    if (n == 0):
        return Infinity;
    temp = hdpotmoddiff(n/2,h,d,z,mod);
    if ((n%2)==0):
        return hdprodmoddiff(temp,temp,h,d,mod);
    else:
        return hdprodmoddiff(z,hdprodmod(temp,temp,h,d,mod),h,d,mod)


def hdpotmod(n,h,d,x0,mod): #x0^n mod mod
    z=bin(n)[2:]
    print(z)
    nbit=len(z)
    v=[0] * nbit
    v[0]=x0
    j=[]
    for i  in range(1,nbit):
        v[i]= hdprodmod(v[i-1],v[i-1],h,d,mod)
    for i in range(0,nbit):
        if (z[nbit-1-i]==str(1)):
            # print(nbit-i)
            j.append(v[i])
    print(v)
    print(j)
    
    nbit=len(j)
    ris=j[0]
    for i in range(1,nbit):
        ris =hdprodmod(j[i],ris,h,d,mod)
    return ris 

a=14896984069081
b=20429454591295
m=2251191278179932
d=2;e=23
n=3261397*8394863
n2=3217520880200761
d2=4565
m2=276524018109505
e2=19
print(hdprodmod(a,b,0,d,n))
print(hdpotmod(e,0,d,m,n))
print("real=",498326899140316)
print(hdpotmod(e2,0,d2,m2,n2))
print("real=",527550631251162)
#print(hdpotmoddiff(23,0,2,2251191278179932,3261397*8394863))