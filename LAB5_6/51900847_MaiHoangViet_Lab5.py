#  51900847_MaiHoangViet_Lab05


import itertools
import math

# Ex1
print('Ex1: ')
print('P = You get good grade in the midterm exam')
print('Q = You understand how to solve all the exercises in the book')
print('a) P <-> Q')
print('b) Q ^ ~P')
print('c) Q -> P')

# Ex2
print('\nEx2: ')
P = 'You get good grade in the midterm exam'
Q = 'You understand how to solve all the exercises in the book'
print('a) ' + P + ' if and only if ' + Q)
print('b) ' + 'If ' + Q + ' then ' + P)
print('c) ' + 'If ' + Q + ' then ' + P)

# Ex3
print('\nEx3: ')
P = 'You get good grade in the midterm exam'
Q = 'You understand how to solve all the exercises in the book'
print('Statements: If Q then P')
print('If you understand how to solve all the exercises in the book, then you get good grade in the midterm exam ')
print('\nNegation: Q ^ ~P')
print('If you understand how to solve all the exercises in the book and you do not get good grade in the midterm exam')
print('\nConverse: P -> Q')
print('If you get good grade in the midterm exam, then you understand how to solve all the exercises in the book')
print('\nContrapositive: ~P -> ~Q')
print('If you do not get good grade in the midterm exam, then you do not understand how to solve all '
      'the exercises in the book')

# Ex4:
print('\nEx4: ')
print('a) ')
print('p = \"Phong has Visa\"')
print('q = \"Phong can fly\"')
print('r = \"Phong can speak English\"')
print('t = \"Phong goes to America\"')
print('S1 = \"If Phong can fly, Phong will go to America\"')
print('S2 = \"If Phong has Visa, Phong will go to America\"')
print('S3 = \"If Phong can speak English, Phong will go to America\"')
print('Conclusion: C = \"Phong goes to America\"')
S1 = 'q -> t'
S2 = 'p -> t'
S3 = 'r -> t'
P = 'p'
C = 't'
print(' %s\n %s\n .%s\n' % (S2, P, C))

print('\nb) ')
print('p = \"An wake up late\"')
print('q = \"the traffic is flowing smooth\"')
print('~q = \"the traffic is heavy\"')
print('r = \"school day\"')
print('s = \"An has go to school\"')
print('v = \"An is late for school\"')
print('S1 = \"The traffic is always heavy on school day\"')
print('S2 = \"If An wake up late, he will be late for school on school day\"')
print('S3 = \"An only have to go to school on school day\"')
print('S4 = \"If An do not have to go to school, An can not be late for school\"')
print('Conclusion: C = \"An is late for school\"')
P = 'p'
Q = 'q'
S1 = '~q -> r'
S2 = 'p -> (v ^ r)'
S3 = 's ^ r'
S4 = '~s -> ~v'
C = 'v'
print(' %s\n %s\n .%s' % (P, S2, 'v ^ r'))
print('\n %s\n .%s' % ('v ^ r', C))

# Ex5
print('\nEx5: ')


def lImplies(p, q):
    if p:
        return q
    return True


S1 = 'q -> t'
S2 = 'p -> t'
S3 = 'r -> t'
P = 'p'
C = 't'
print('a)')
print(' %s\n %s\n .%s\n' % (S2, P, C))
table_1 = list(itertools.product([True, False], repeat=4))
p = [a[0] for a in table_1]
q = [a[1] for a in table_1]
r = [a[2] for a in table_1]
t = [a[3] for a in table_1]
S2 = [lImplies(p[i], t[i]) for i in range(len(table_1))]
print('p\t\t q\t\t r\t\t t\t\t .p->t')
for i in range(len(table_1)):
    print(p[i], '\t', q[i], '\t', r[i], '\t', t[i], '\t', S2[i])

print('\nb)')
P = 'p'
Q = 'q'
S1 = '~q -> r'
S2 = 'p -> (v ^ r)'
S3 = 's ^ r'
S4 = '~s -> ~v'
C = 'v'
print(' %s\n %s\n .%s' % (P, S2, 'v ^ r'))
print('\n %s\n .%s' % ('v ^ r', C))
table_2 = list(itertools.product([True, False], repeat=3))
p = [a[0] for a in table_2]
r = [a[1] for a in table_2]
v = [a[2] for a in table_2]
S2 = [lImplies(p[i], (v[i] and r[i])) for i in range(len(table_2))]
print("\np\t\t r\t\t v\t\tp -> ( v ^ r)")
for i in range(len(table_2)):
    print(p[i], "\t", r[i], "\t", v[i], "\t", S2[i])


# Ex6
def isOdd(a):
    if a % 2 == 0:
        return True
    return False


def isPrime(a):
    for i in range(2, int(math.sqrt(a))):
        if a % i == 0:
            return False
    return True


def isSquare(a):
    if math.sqrt(a).is_integer() and math.sqrt(a) > 0:
        return True
    else:
        return False


def isGreater(a, b):
    if a > b:
        return True
    else:
        return False


def isEqual(a, b):
    if a == b:
        return True
    else:
        return False


def isAbove(a, b):
    if a < b:
        return True
    else:
        return False


def isLeftOf(a, b):
    if a < b:
        return True
    else:
        return False


print("\nEx6:")
A = [[2, 0, 5, 0, 3, 0],
     [3, 0, 0, 0, 0, 0],
     [0, 6, 2, 0, 5, 0],
     [3, 0, 9, 0, 25, 0],
     [0, 0, 2, 4, 5, 0],
     [0, 0, 0, 0, 0, 5]
     ]

print('a : ∃a ∈ A, ¬isOdd(a) ∧ is Prime(a)')
flag = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        if not isOdd(A[i][j]) and isPrime(A[i][j]):
            flag += 1
            break

if flag != 0:
    print(True)
else:
    print(False)

print('b : ∀a ∈ A, isOdd(a) → isSquare(a)')
flag = 1000
for i in range(len(A)):
    for j in range(len(A[i])):
        if lImplies(isOdd(A[i][j]), isSquare(A[i][j])):
            continue
        else:
            flag -= 1

if flag == 1000:
    print(True)
else:
    print(False)

print('c : ∀a ∈ A, isOdd(a) → isGreater(a, 2)')
flag = 1000
for i in range(len(A)):
    for j in range(len(A[0])):
        if lImplies(isOdd(A[i][j]), isGreater(A[i][j], 2)):
            continue
        else:
            flag -= 1

if flag == 1000:
    print(True)
else:
    print(False)

print('d : ∃a ∈ A, isPrime(a) → ¬(isGreater(a, 3) ∨ isEqual(a, 3))')
flag = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        if lImplies(isPrime(A[i][j]), not (isGreater(A[i][j], 3) or isEqual(A[i][j], 3))):
            flag += 1
            break

if flag > 0:
    print(True)
else:
    print(False)

print('e : ∃a ∈ A, ∀b ∈ A, isLeftOf(a, b)')
flag = 1000
for i in range(len(A)):
    for j in range(len(A[0])):
        colA = j
        colB = j + 1
        if colB < len(A[0]) and A[i][colA] > 0 and A[i][colB] > 0:
            if isLeftOf(colA, colB):
                flag -= 1
                break

if flag == 1000:
    print(True)
else:
    print(False)

print('f : ∃a ∈ A, ∀b ∈ A, isGreater(a, b) → ¬isAbove(a, b)')
flag = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        rowA = i
        rowB = i + 1
        if rowB < len(A) and A[rowA][j] > 0 and A[rowB][j] > 0:
            if lImplies(isGreater(A[rowA][j], A[rowB][j]), not isAbove(rowA, rowB)):
                flag += 1
                break

if flag > 0:
    print(True)
else:
    print(False)

print('g : ∀a ∈ A, ∃b ∈ A, isPrime(a) ∧ ¬isOdd(a) ∧ isOdd(b) → isAbove(a, b)')
flag = 1000
for i in range(len(A)):
    for j in range(len(A[0])):
        rowA = i
        rowB = i + 1
        if rowB < len(A) and A[rowA][j] > 0 and A[rowB][j] > 0:
            A1 = isPrime(A[rowA][j]) and not isOdd(A[rowA][j]) and isOdd(A[rowB][j])
            if lImplies(A1, isAbove(rowA, rowB)):
                continue
            else:
                flag -= 1
                break
if flag == 1000:
    print(True)
else:
    print(False)

