import multitlp_testing as tlp
import math 


def isNonQuadratic(d,p,q):
    # d is non quadratic mod N iff  d non quadratic mod p AND non quadratic mod q
    # i.e. (d|p)=-1 or (d|q)=-1
    # see https://crypto.stanford.edu/pbc/notes/numbertheory/qr.html

    if (tlp.jacobi(d, p)!=-1 or tlp.jacobi(d,q)!=-1):
        return True
    else:
        print(d,"is quadratic because")
        print("d|p=",tlp.jacobi(d,p))
        print("d|q=",tlp.jacobi(d,q))
        return False
        
Infinity=math.inf

h = 0;
p = 61696199
q = 52151039
n = p*q;
d = 4565;

assert(isNonQuadratic(d,p,q))
print("\n Primo test -- hdprodmod -value infinity in a")
a = Infinity
b = 143338416350200
primo=tlp.hdprodmod(a, b, 0, d, n)
print("primo",primo == b)


print("\n Second test -- hdprodmod -value infinity in b")
# a = RandomInteger({1, n - 1})
a = 541369662510009
# b = Infinity
b = Infinity
secondo = tlp.hdprodmod(a, b, 0, d, n)
print("secondo", secondo == a)

print("\n Third test -- hdprodmod - a and b random")
# a = RandomInteger({1, n - 1})
a = 173464984356006
# b = RandomInteger({1, n - 1})
b = 1674358333198127
terzo= tlp.hdprodmod(a, b, 0, d, n)
print("terzo", terzo==2152157872354060)
print("terzo value" , terzo) 

print("\n Fourth test -- hdprodmod - a and b random")
# a = RandomInteger({1, n - 1})
a = 2533010732781956
# b = RandomInteger({1, n - 1})
b = n - a 
quarto= tlp.hdprodmod(a, b, 0, d, n)
print("quarto", quarto==Infinity)
print("quarto value" , quarto) 

print("\n Fifth test -- hdpotmod - m^a - a and b random")
# a = RandomInteger({1, n - 1})
# hdprodmod(a, b, 0, d, n)
# ∞
# m = RandomInteger({1, n - 1})
m= 276524018109505
f = 19;
quinto= tlp.hdpotmod(f, 0, d, m, n)

print("quinto", quinto == 527550631251162)
# print("quinto value" , quinto) 
# print(498326899140316) 
# PowerMod(m, e, n)
# 1 113 802 055 526 982
# print("testing")
# a= 2251191278179932
# a2 = tlp.hdpotmod(2,0,d,a,n) 
# a3 = tlp.hdpotmod(3,0,d,a,n) 
# a5 = tlp.hdpotmod(5,0,d,a,n) 
# a9 = tlp.hdpotmod(9,0,d,a,n) 
# a14 = tlp.hdpotmod(14,0,d,a,n) 
# aaa = tlp.hdprodmod(a,a2,0,d,n) 
# aaaaa = tlp.hdprodmod(a3,a2,0,d,n) 
# a14a = tlp.hdprodmod(a9,a5,0,d,n) 
# print(a14a==a14) 

