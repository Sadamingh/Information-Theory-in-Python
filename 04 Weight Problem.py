import numpy as np
from random import *

def generater(N):
    weight = np.zeros(N)
    x = random()
    y = int(12 * x)
    p = random()
    
    if (p <= .5):
        weight[y] = -1
    else:
        weight[y] = 1
    
    return weight
    
def measure(A,B):
    sum_a = np.sum(A)
    sum_b = np.sum(B)
    if (sum_a > sum_b):
        bull = 1
    elif (sum_a < sum_b):
        bull = -1
    else:
        bull = 0
        
    return bull


weight =  generater(12)
print(weight)
i = measure(weight[0:4],weight[4:8])

if (i == 1 or i == -1):
    j = measure(weight[[0,1,5]],weight[2:5])
else:
    j = measure(weight[8:11],weight[0:3])

if (i == 0 and j == 0):
    print('the number of the odd ball is: 12\n')
elif (i != 0 and j == 0):
    k = measure(weight[0],weight[6])
    if (k != 0):
        print('the number of the odd ball is: 7\n')
    else:
        print('the number of the odd ball is: 8\n')
elif (i == 0 and j == 1):
    k = measure(weight[8],weight[9])
    if (k == 0):
        print('the number of the odd ball is: 11\n')
    elif (k == 1):
        print('the number of the odd ball is: 9\n')
    else:
        print('the number of the odd ball is: 10\n')
elif (i == 0 and j == -1):
    k = measure(weight[8],weight[9])
    if (k == 0):
        print('the number of the odd ball is: 11\n')
    elif (k == 1):
        print('the number of the odd ball is: 10\n')
    else :
        print('the number of the odd ball is: 9\n')
elif (i == 1 and j == 1):
    k = measure(weight[0],weight[1])
    if (k == 0):
        print('the number of the odd ball is: 5\n')
    elif (k == 1):
        print('the number of the odd ball is: 1\n')
    else:
        print('the number of the odd ball is: 2\n')
elif (i == 1 and j == -1):
    k = measure(weight[2],weight[3])
    if (k == 0):
        print('the number of the odd ball is: 6\n')
    elif (k == 1):
        print('the number of the odd ball is: 3\n')
    else:
        print('the number of the odd ball is: 4\n')
elif (i == -1 and j == 1):
    k = measure(weight[2],weight[3])
    if (k == 0):
        print('the number of the odd ball is: 6\n')
    elif (k == 1):
        print('the number of the odd ball is: 4\n')
    else:
        print('the number of the odd ball is: 3\n')
else:
    k = measure(weight[0],weight[1])
    if (k == 0):
        print('the number of the odd ball is: 5\n')
    elif (k == 1):
        print('the number of the odd ball is: 2\n')
    else :
        print('the number of the odd ball is: 1\n')
