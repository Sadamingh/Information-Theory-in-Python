# this is used to test the constant of the whole Information Content gained if we know the position of submariones
from math import *

def Entropy(p):
    infcont = log(1/p,2)
    return infcont

# given the number of overall attempts when shoot the submarione
N = int(input('please enter the number of shot that first hits the submariones (1-64):'))
while (N > 64 or N <= 0):
    print('Illegal value. Please enter another value.')
    N = int(input('please enter the number of shot that first hits the submariones:'))

# the information content of outcome 'Miss on the first 32 shots':
accumu = 0

for i in range(N - 1):
    c = 64 - i
    p = 1/c
    accumu += Entropy(1-p)
    
p = 1/(64 - (N - 1))
last = Entropy(p)
    
print('total information content:', round(accumu + last))
