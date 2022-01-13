# Ex1
print('Ex1:')
# (a) For all fishes, they need water to survive.
print('a)')
print("D is \'fishes\'")
print("P is \'need water to survive\'")
print("Formal form: For all x in D, P(x)")
# (b) Exist a person, who is left handed
print('\nb)')
print("D is \'person\'")
print("P is \'is left handed\'")
print("Formal form: Exist x in D such that P(x)")
# (c) Exist an employee in the company, who is late to work everyday.
print('\nc)')
print("D is \'employee in company\'")
print("P is \'is late to work everyone\'")
print("Formal form: Exist x in D such that P(x)")
# (d) For all fishes in this pond, they are Koi fish.
print('\nd)')
print("D is \'fishes in this pond\'")
print("P is \'are Koi fish\'")
print("Formal form: For all x in D, P(x)")
# (e) There is at least one creature in the ocean, it can live on land
print('\ne)')
print("D is \'at least one creature in the ocean\'")
print("P is \'can live in land\'")
print("Formal form: There is x in D such that P(x)")
# (f) Every students in class A did not pass the test
print('\nf)')
print("D is \'students in class A\'")
print("P is \'did not pass the test\'")
print("Formal form: Every x in D, P(x)")

# Ex2
print('\nEx2: ')


def formalConvert(S):
    list = S.split(',')
    left = list[0].split(' ')
    right = list[1].split(' ')
    temp = []
    D = []
    for item in left:
        if item == 'For' or item == 'all' or item == 'Exist' or item == 'There' or item == 'is' or item == 'Every':
            temp.append(item)
        else:
            D.append(item)
    P = [right[i] for i in range(2, len(right))]
    F = [temp[i] for i in range(len(temp))]
    if temp == ['Exist'] or temp == ['There', 'is']:
        F.append('x in D such that P(x)')
    else:
        F.append('x in D, P(x)')
    return [D, P, F]


def printAll(D, P, F):
    print("D is \'", end="")
    for item in D:
        print(item, end=" ")
    print("\'")

    print("P is \'", end="")
    for item in P:
        print(item, end=" ")
    print("\'")

    print("Formal form: ", end="")
    for item in F:
        print(item, end=" ")
    print()


D, P, F = formalConvert('For all fishes, they need water to survive')
print('a)')
printAll(D, P, F)

D, P, F = formalConvert('Exist a person, who is left handed')
print('\nb)')
printAll(D, P, F)

D, P, F = formalConvert('Exist an employee in the company, who is late to work everyday')
print('\nc)')
printAll(D, P, F)

D, P, F = formalConvert('For all fishes in this pond, they are Koi fish')
print('\nd)')
printAll(D, P, F)

D, P, F = formalConvert('There is at least one creature in the ocean, it can live on land')
print('\ne)')
printAll(D, P, F)

# Ex3:
print('\nEx3:')
# (a) For all people, if they are blond then they are westerners.
print('a)')
print("D is \"people\"")
print("P is \"are blond\"")
print("Q is \"are westerners\"")
print("Formal form: For all x in D, P(x) then Q(x)")
# (b) Exist a person, whose hair is black but is a westerner.
print('\nb)')
print("D is \"person\"")
print("P is \"is black\"")
print("Q is \"is a westerner\"")
print("Formal form: Exist x in D such that P(x) and Q(x)")
# (c) For all students, if they study correctly then they have high score.
print('\nc)')
print("D is \"students\"")
print("P is \"study correctly\"")
print("Q is \"have high score\"")
print("Formal form: For all x in D, P(x) then Q(x)")
# (d) For every mammal, if they live in the sea, they are either dolphins or whales.
print('\nd)')
print("D is \"mammal\"")
print("P is \"live in the sea\"")
print("Q is \"either dolphins or whales\"")
print("Formal form: For every x in D, P(x) then Q(x)")
# (e) For every bird, if they don’t have wings and can swim then they are penguins.
print('\ne)')
print("D is \"bird\"")
print("P is \"don't have wings and can swim\"")
print("Q is \"are penguins\"")
print("Formal form: For every x in D, P(x) then Q(x)")
# (f) Exist a bird, who have wing but can’t fly.
print('\nf)')
print("D is \"a bird\"")
print("P is \"have wing\"")
print("Q is \"can't fly\"")
print("Formal form: Exist x in D, P(x) and Q(x)")

# Ex4
print('\nEx4: ')


def formalConvertPQ(S):
    list = S.split(',')
    left = list[0].split(' ')
    right = list[1].split(' ')
    temp = []
    D = []
    for item in left:
        if item == 'For' or item == 'all' or item == 'Exist' or item == 'every':
            temp.append(item)
        else:
            D.append(item)
    if 'then' in right:
        P = [right[i] for i in range(3, right.index('then'))]
        Q = [right[i] for i in range(right.index('then') + 2, len(right))]
    elif 'but' in right:
        P = [right[i] for i in range(3, right.index('but'))]
        Q = [right[i] for i in range(right.index('but') + 1, len(right))]
    else:
        temp_Right = right.split(', ')
        temp_Right_Left = temp_Right[0].split(' ')
        temp_Right_Right = temp_Right[1].split(' ')
        P = [temp_Right_Left[i] for i in range(3, len(temp_Right_Left))]
        Q = [temp_Right_Right[i] for i in range(2, len(temp_Right_Right))]
    F = [temp[i] for i in range(len(temp))]
    if temp == ['For', 'all'] or temp == ['For', 'every']:
        F.append('x in D, if P(x) then Q(x)')
    else:
        F.append('x in D such that P(x) and Q(x)')
    return [D, P, Q, F]


def printAll(D, P, Q, F):
    print("D is \"", end="")
    for item in D:
        print(item, end=" ")
    print("\"")

    print("P is \"", end="")
    for item in P:
        print(item, end=" ")
    print("\"")

    print("Q is \"", end="")
    for item in Q:
        print(item, end=" ")
    print("\"")

    print("Formal form: ", end="")
    for item in F:
        print(item, end=" ")
    print()


D, P, Q, F = formalConvertPQ("For all people, if they are blond then they are westerners")
print('a)')
printAll(D, P, Q, F)

D, P, Q, F = formalConvertPQ("Exist a person, whose hair is black but is a westerner")
print('\nb)')
printAll(D, P, Q, F)

D, P, Q, F = formalConvertPQ("For all students, if they study correctly then they have high score")
print('\nc)')
printAll(D, P, Q, F)

D, P, Q, F = formalConvertPQ("For every bird, if they don’t have wings and can swim then they are penguins")
print('\ne)')
printAll(D, P, Q, F)

D, P, Q, F = formalConvertPQ("Exist a bird, who have wing but can’t fly")
print('\nf)')
printAll(D, P, Q, F)

# Ex5
print('\nEx5: ')


def nega(A):
    list = A.split(',')
    left = list[0].split(" ")
    right = list[1].split(" ")
    D = []
    N = []
    temp = []
    for item in left:
        if item == 'For' or item == 'all' or item == 'Exist' or item == 'Every' or item == 'There' or item == 'is':
            temp.append(item)
        else:
            D.append(item)
    P = [right[i] for i in range(2, len(right))]
    if temp == ['For', 'all']:
        N.append('Exist')
        for item in D:
            N.append(item)
        N.append(',')
        N.append(right[1])
        N.append("not")
        for item in P:
            N.append(item)
    else:
        N = ['For', 'all']
        for item in D:
            N.append(item)
        N.append(",")
        N.append(right[1])
        N.append("not")
        for item in P:
            N.append(item)
    return N


def printNega(N):
    for item in N:
        print(item, end=" ")
    print()


N = nega("For all fishes, they need water to survive.")
print("a)")
printNega(N)

N = nega("Exist a person, who is left handed")
print('\nb)')
printNega(N)

N = nega("Exist an employee in the company, who is late to work everyday.")
print('\nc)')
printNega(N)

N = nega("For all fishes in this pond, they are Koi fish.")
print('\nd)')
printNega(N)

N = nega("There is at least one creature in the ocean, it can live on land")
print('\ne)')
printNega(N)

# Ex6
print('\nEx6: ')
print("a)")
print(" Negation: Exist a person, he/she is blond but he/she is not westerners.")
print(" Contrapositive: For all people, if they are not westerners then they are not blond")
print(" Converse: For all people, if they are westerners then they are blond")
print(" Inverse: For all people, if they are not blond then they are not westerners")
print("\nb)")
print(" Negation: For all people, if their hair is black then they are not westerner")
print(" Contrapositive: Exist a person, whose is not a westerner but hair is not black")
print(" Converse: Exist a person, whose is a westerner but hair is black")
print(" Inverse: Exist a person, whose hair is not black but is not a westerner")
print("\nc)")
print(" Negation: Exist a student, he/she studies correctly but he/she has not high score")
print(" Contrapositive: For all students, if they have not high score then they are not study correctly")
print(" Converse: For all students, if they have high score then they study correctly")
print(" Inverse: For all students, if they are not study correctly then they have not high score")
print("\nd)")
print(" Negation: Exist a mammal, it lives in the sea but it not either dolphin or whale")
print(" Contrapositive: For all mammal, if they are not dolphins or whales then they are not live in the sea")
print(" Converse: For all mammal, if they are either dolphins or whales then they are live in the sea")
print(" Inverse: For all mammal, if they are not live in the sea then they are not either dolphins or whales")
print("\ne)")
print(" Negation: Exist a bird, it doesn't have wings and can not swim but it is not penguin")
print(" Contrapositive: For all birds, if they are not penguins then they have wings and can not swim")
print(" Converse: For all birds, if they are penguins then they don't have wings and can swim")
print(" Inverse: For all birds, if they have wings and can not swim then they are not penguins")
print("\nf)")
print(" Negation: For all birds, if they have wings then they can fly")
print(" Contrapositive: Exist a bird, who can fly but have not wing")
print(" Converse: Exist a bird, who can't fly but have wing")
print(" Inverse: Exist a bird, who have not wing but can fly")
