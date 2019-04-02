from math import *

P = {'A':.1,'B':.3,'C':.4,'D':.2}
Q = {'A':.25,'B':.25,'C':.25,'D':.25}

def entropy(P,Q,L):
    ent = log(P[L],2)-log(Q[L],2)
    return ent

print(entropy(P,Q,input('please enter a letter for checking the relative entropy of each answer of a multiple choice (A - D):')))

sument = 0

for letter in ['A','B','C','D']:
    ent = P[letter]*(log(P[letter],2)-log(Q[letter],2))
    sument = sument + ent

print('\nThe K-L divergence between P and Q is:',sument)
