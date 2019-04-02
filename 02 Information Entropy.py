from math import *

P = {'A':.1,'B':.3,'C':.4,'D':.2}

def entropy(P,L):
    ent = log((1/(P[L])),2)
    return ent

print(entropy(P,input('please enter a letter for checking the entropy of each answer of a multiple choice (A - D):')))

sument = 0

for letter in ['A','B','C','D']:
    ent = P[letter]*log((1/(P[letter])),2)
    sument = sument + ent

print('\nThe expected entropy of the ensemble is:',sument)
