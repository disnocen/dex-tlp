import multitlp as tlp
import time
import random
#not secure for crypto purposes!

d=2
p=240517
#p=tlp.nthprime(212640) 
print(p) 
print(tlp.jacobi(d,p))
q=582623
#q=tlp.nthprime(477838) 
print(q) 
print(tlp.jacobi(d,q))

n=p*q
print(n) 
message="ciao"  

a=random.randrange(10,n)
t = 100000000000000000000 #number of time slots desired
start_time = time.time()
puzzle=tlp.rswGenPuzzle(message,a,t, p, q)
print(puzzle)
print( 'tlp.rswGenPuzzle took', time.time() - start_time, "seconds\n")

start_time = time.time()
message=tlp.rswSolPuzzle(puzzle)
print(message)
print('tlp.rswSolPuzzle took', time.time() - start_time, "seconds")


