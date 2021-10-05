import random
import subprocess

nbit=1024
sum=0
for i in range(nbit-2):
    e=random.random()*10
    e=int(e)
    sum=sum + e*2**i
    print (sum,sum.bit_length())

x=subprocess.Popen(["sh","-c", "./nextprime.sh " +str(sum)], stdout=subprocess.PIPE).communicate()[0]
x=int(x[:-1])
print("prime number"  )
print(x)
print("bit length"  )
print(x.bit_length())

