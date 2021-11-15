import itertools
import sys
sys.path.insert(0,'..')
import edftools
from testedfs import *

# Copied https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def map(el, m):
    if type(el) is tuple:
        return tuple([x % m for x in el])
    else:
        return el % m
def check_homomorphisms(family, n):
    for m in factors(n):
        image = []
        for s in family:
            image.append([map(g, m) for g in s])
        if not edftools.is_overlapping_edf(image, m):
            print(str(family) + ", mod " + str(m) + " = " + str(image) + "is a counterexample")
            #sys.exit()
            return False
    return True

def find_edfs(n,m,k):
    all_els = list(itertools.combinations(range(0,n), m*k))
    for els in all_els:
        perms = list(itertools.permutations(els))
        for p in perms:
            family = [list(p[i:i+k]) for i in range(0, m*k, k)]
            if edftools.is_edf(family, n):
                #print("found edf!: " + str(family))
                if check_homomorphisms(family, n):
                    pass
                    #print("all homs work")
            if edftools.is_sedf(family, n):
                pass
                #print("found sedf!: " + str(family))
            
for n in range(3, 15):
     family = []
     for m in range(2, n):
        for k in range(1, int(n/m)):
             print("for parameters n = {0}, m = {1}, k = {2}".format( n, m, k))
             find_edfs(n,m,k)

# for sedf in h_7_all_with_mods:
#     print(sedf[0])
#     print(sedf[1])
#     check_homomorphisms(sedf[0], sedf[1])