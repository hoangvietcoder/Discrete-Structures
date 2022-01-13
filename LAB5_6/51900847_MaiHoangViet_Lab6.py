import math
import random

# Ex1: Write a python function print2Prime(a,b) to print all the pair of primes
# numbers p,q such that a<p*q<b.
print('Ex1: ')


def print2Prime(a, b):
    temp_1 = []
    temp_2 = []
    temp_3 = []
    for i in range(a + 1, b + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                temp_1.append(i)
    for i in temp_1:
        for j in temp_1:
            if i != j:
                c = i * j
                if a < c < b:
                    temp_2.append([i, j])
    for i in temp_2:
        if len(temp_3) < 1:
            temp_3.append(i)
        else:
            if i not in temp_3:
                temp_3.append(i)
            for j in temp_3:
                if i[0] == j[1] and i[1] == j[0]:
                    temp_3.remove(i)
    return temp_3


print(print2Prime(0, 50))

# Ex2: Write a python function printCoprime(a,n) to print all the coprime
# numbers of a in [2,n]
print('\nEx2: ')


def printPrime(a, b):
    temp = []
    for i in range(a + 1, b + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                temp.append(i)
    return temp


def printCoprime(a, n):
    temp_1 = printPrime(0, n)
    temp_2 = []
    for item in temp_1:
        if math.gcd(item, a) == 1:
            temp_2.append(item)
    return temp_2


print(printCoprime(2, 100))

# Ex3: Write a python function printHidkey(fn,e) to print all the numbers d that
# satisfy: d*e%fn=1 and 2<d<fn
print('\nEx3: ')


def printHidkey(fn, e):
    e = int(e)
    temp = []
    for i in range(2, fn):
        if (i * e) % fn == 1 and 2 < i < fn:
            temp.append(i)
    return temp


p = random.randrange(0, 100, 2)
q = random.randrange(0, 100, 2)
e = 2.7
h = printHidkey((p-1)*(q-1), e)
d = random.sample(h, 1)[0]
print(d)
