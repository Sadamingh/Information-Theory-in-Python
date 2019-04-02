import random

def encoderep(s):
    t = ''
    for i in range(len(s)):
        t = t + str(s[i])
        t = t + str(s[i])
        t = t + str(s[i])
    return t

def noisegen(f,s):
    n = ''
    for i in range(3*len(s)):
        if (f <= random.random()):
            n += '0'
        else:
            n += '1'
    return n

def store(t,n,s):
    r = ''
    for i in range(3*len(s)):
        if(int(n[i]) == 0):
            r += t[i]
        elif((int(n[i]) == 1) and (int(t[i]) == 1)):
            r += '0'
        else:
            r += '1'
    return r
            
def decoderep(r,s):
    shat = ''
    for i in range(len(s)):
        if(r[(3*i):(3*(i+1))].count('0') >= 2):
            shat += '0'
        else:
            shat += '1'
    return shat

# given the source code    
s = '0010110'
# encode the code to be ready for storage
t = encoderep(s)
# give the probability of a wrong code
f = 0.1
# generate noise randomly
n = noisegen(f,s)
# creat the code to be store
r = store(t,n,s)
# decode the code that has been stored
shat = decoderep(r,s)

print(shat)

# test the error rate
for i in range(1000000):
    s = '0010110'
    t = encoderep(s)
    f = 0.1
    n = noisegen(f,s)
    r = store(t,n,s)
    shat = decoderep(r,s)
    wro = 0
    if (int(s) != int(shat)):
        wro += 1

print(wro)
