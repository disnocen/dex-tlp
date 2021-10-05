import multitlp as tlp
import math 


def isNonQuadratic(d,p,q):
    # d is non quadratic mod N iff  d non quadratic mod p AND non quadratic mod q
    # i.e. (d|p)=-1 or (d|q)=-1
    # see https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html

    if (tlp.jacobi(d, p)==-1 or tlp.jacobi(d,q)==-1):
        return True
    else:
        return False
        
Infinity=math.inf

h = 0;
p = 3261397
q = 8394863
n = p*q;
d = 2;

assert(isNonQuadratic(d,p,q))
print("\n Primo test -- hdprodmod -value infinity in a")
a = Infinity
b = 14379999608863
primo=tlp.hdprodmod(a, b, 0, d, n)
print("primo",primo == 14379999608863)


print("\n Second test -- hdprodmod -value infinity in b")
# a = RandomInteger({1, n - 1})
a = 835348340628
# b = Infinity
b = Infinity
secondo = tlp.hdprodmod(a, b, 0, d, n)
print("secondo", secondo == 835348340628)

print("\n Third test -- hdprodmod - a and b random")
# a = RandomInteger({1, n - 1})
a = 14896984069081
# b = RandomInteger({1, n - 1})
b = 20429454591295
terzo= tlp.hdprodmod(a, b, 0, d, n)
print("terzo", terzo==830052648327)
print("terzo value" , terzo) 

print("\n Forth test -- hdpotmod - m^a - a and b random")
# a = RandomInteger({1, n - 1})
# hdprodmod(a, b, 0, d, n)
# ∞
# m = RandomInteger({1, n - 1})
m= 2251191278179932
f = 23;
quarto= tlp.hdpotmod(f, 0, d, m, n)

print("quarto", quarto == 498326899140316)
print("quarto value" , quarto) 
print(498326899140316) 
# PowerMod(m, e, n)
# 1 113 802 055 526 982
print("testing")
a= 2251191278179932
a2 = tlp.hdpotmod(2,0,d,a,n) 
a3 = tlp.hdpotmod(3,0,d,a,n) 
a5 = tlp.hdpotmod(5,0,d,a,n) 
a9 = tlp.hdpotmod(9,0,d,a,n) 
a14 = tlp.hdpotmod(14,0,d,a,n) 
aaa = tlp.hdprodmod(a,a2,0,d,n) 
aaaaa = tlp.hdprodmod(a3,a2,0,d,n) 
a14a = tlp.hdprodmod(a9,a5,0,d,n) 
print(a14a==a14) 

