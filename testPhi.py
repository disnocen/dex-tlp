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

def Mod(a,mod):
    return a%mod

def InvMod(aaa,mod):
    return pow(aaa,-1,mod)

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



# mx=5
# my=6
# n=13*17
# d=Dgen(mx,my,n)
# m=Phi(5,6,17)
# print("m=",m)
# (x,y)=InvPhi(m,d,n)
# print((x,y))

p3=888161167
q3=372281951
n3=p3*q3

d3=558782244922733789
d3=55878224492273788
m3=832918376442

print(InvPhi(m3,d3,n3))

M=InvPhi(m3,d3,n3)
d=Dgen(M[0],M[1],n3)
print("on d",d==d3)
print("on phi",Phi(M[0],M[1],n3)==m3)


mx=81921463405935260
my=171234750880303278
nn=330646372053196817
dd=55878224492273788
print(dd==Dgen(mx,my,nn))