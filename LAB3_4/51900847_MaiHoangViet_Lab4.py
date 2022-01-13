# Ex1
import random
import math

print('Ex1: ')
P = "Phong has Visa"
S1 = "If Phong can fly, Phong will go to America"
S2 = "If Phong has Visa, Phong will go to America"
S3 = "If Phong can speak English, Phong will go to America"
C = "Phong goes to America"
print("a)")
print("P -> C")
print("P:", P)
print("C:", C)

P = "It's hot yesterday"
S1 = "If it's hot, it will rain the next day"
S2 = "If and only if it's not rain, Nam goes outside"
S3 = "If it's not hot, Nam will go outside"
C = "Nam goes outside"
print("\nb)")
print("S2 and S3 -> C")
print("S2:", S2)
print("S3:", S3)
print("C:", C)

Q = "An wake up late"
R = "The traffic is flowing smooth"
S1 = "The traffic is always heavy on school day"
S2 = "If An wake up late, he will be late for school on school day"
S3 = "An only have to go to school on school day"
S4 = "If An don't have to go to school, An can't be late for school"
C = "An is late for school"
print("\nc)")
print("S1 and S2 -> C")
print("S1:", S1)
print("S2:", S2)
print("C:", C)

P = "Ex, y in R, (x+y)^2 <= x^2 + y^2"
Q = "Vx, y in Z+, x + y >= x + y"
R = "Vx, y in Z+, x + y + 2sqrt(x+y) >= x + y"
T = "Vx, y in Z+, sqrt(x+y) >= 0"
S1 = "Vx, y in Z+, x^2 >= y^2 -> x >= y"
S2 = "Vx, y in Z+, x >= y -> x^2 >= y^2"
S3 = "Vx, y in R+, x >= y -> x^2 >= y^2"
S4 = "Vx, y in R+, x^2 >= y^2 -> x >= y"
C = "Vx, y in Z+, sqrt(x) + sqrt(y) >= sqrt(x+y)"
print("\nd)")
print("R -> C")
print("R:", R)
print("C:", C)

# Ex2
print('\nEx2: ')
checkError = False
for x in range(101):
    if x ** 2 == 15 ** 2 + 16 ** 2:
        checkError = True
        print("a. The given statement is correct when x equal to", x)
        break
if not checkError:
    print("a. The given statement is incorrect for all values x within the given domain.")

checkError = False
for x in range(101):
    if x ** 2 == 12 ** 2 + 16 ** 2:
        checkError = True
        print("b. The given statement is correct when x equal to", x)
        break
if not checkError:
    print("b. The given statement is incorrect for all values x within the given domain.")

checkError = False
for x in range(-50, 51):
    if x ** 2 >= 99 * x:
        checkError = True
        print("c. The given statement is correct when x equal to", x)
        break
if not checkError:
    print("c. The given statement is incorrect for all values x within the given domain.")

checkError = False
for x in range(50, 101):
    if x * (x + 1) * (x + 2) % 6 != 0:
        checkError = True
        print("d. The given statement is correct when x equal to", x)
        break
if not checkError:
    print("d. The given statement is incorrect for all values x within the given domain.")

checkError = False
y = random.randint(0, 101)
for x in range(101):
    if math.sqrt(x + y) == math.sqrt(x) + math.sqrt(y):
        checkError = True
        print("e. The given statement is correct when x equal to", x)
        break
if not checkError:
    print("e. The given statement is incorrect for all values x within the given domain.")

# Ex3
print('\nEx3: ')
print('a)')
print("Negative: Vx in Z, 0 <= x <= 100, x^3 < x")
checkError = False
for x in range(101):
    if x ** 3 < x:
        checkError = True
        print("The given statement is correct when x equal to ", x)
        break
if not checkError:
    print("The given statement is incorrect for all values x within the given domain.")

print('\nb)')
print("Negative: Vx in Z, 0 <= x <= 100, and x is even, x * 3 + 1 is not a prime number")
checkError = False
for x in range(0, 101, 2):
    temp = x * 3 + 1
    for i in range(2, int(math.sqrt(temp)) + 1):
        if temp % i == 0:
            checkError = True
            print("The given statement is correct when x equal to", x)
            break
        if checkError:
            break
if not checkError:
    print("The given statement is incorrect for all values x within the given domain.")

print('\nc)')
print("Negative: Vx in Z, 1 <= x, y <= 100, and x is even, x*5+3 is not a prime number")
checkError = False
for x in range(0, 101, 2):
    temp = x * 5 + 3
    for i in range(2, int(math.sqrt(temp)) + 1):
        if temp % i == 0:
            checkError = True
            print("The given statement is correct when x equal to", x)
            break
        if checkError:
            break
if not checkError:
    print("The given statement is incorrect for all values x within the given domain.")

print('\nd)')
print("Negative: Vc in Z, 0 < c <= 100, c%4 = 0, Ea, b in Z, c^2 != a^2 + b^2")
checkError = False
a = random.randint(0, 101)
b = random.randint(0, 101)
for c in range(4, 101, 4):
    if c * c != a * a + b * b:
        checkError = True
        print("The given statement is correct when c equal to ", c, ", a equal to ", a, ", b equal to ", b)
        break
if not checkError:
    print("The given statement is incorrect for all values x within the given domain.")

print('\ne)')
print("Negative: Vc in Z, 0 < c <= 100, c^2 > c")
checkError = False
for c in range(1, 101):
    if c ** 2 > c:
        checkError = True
        print("The given statement is correct when c equal to", c)
        break
if not checkError:
    print("The given statement is incorrect for all values x within the given domain.")

# Ex4:
print('\nEx4: ')
print('a)', end=" ")
sum_Left = 0
sum_Right = 0
for x in range(11):
    for y in range(11):
        sum_Left += (x + y) ** 2
        sum_Right += (x + 2 * y) ** 2
if sum_Left > sum_Right:
    print('True')
else:
    print('False')

print('b)', end=" ")
left = 1
right = 0
for i in range(2, 21):
    left *= i
for j in range(11):
    factorial = 1
    for k in range(2, j + 1):
        factorial *= k
    right += factorial
if left < right:
    print('True')
else:
    print('False')

print('c)', end=" ")
left = 0
right = 10 ** 3
for x in range(11):
    left += 3 * x ** 2

if left >= right:
    print('True')
else:
    print('False')

print('d)', end=" ")
left = 0
right = 10 ** 4 + 2 * 10 ** 3 + 10 ** 2 - 5 ** 4 - 2 * 5 ** 3 - 5 ** 2
for x in range(5, 11):
    left += 4 * (x ** 3) + 6 * (x ** 2) + 2 * x

if left > right:
    print('True')
else:
    print('False')


# Ex5:
print('a) ')
G1 = 'p -> r'
G2 = '~p -> q'
G3 = 'q -> s'
G4 = 'G2 + G3 => G4 = ~p -> s, Transitivity'
G5 = 'G4 = ~s -> p, Contrapositive'
G6 = 'G1 + G5 => G6 = ~s -> r, Transitivity '
C = 'G5 => C = ~r -> s, Contrapositive'
print('G1 = ', G1)
print('G2 = ', G2)
print('G3 = ', G3)
print('G4 = ', G4)
print('G5 = ', G5)
print('G6 = ', G6)
print('C = ', C)

print('\nb) ')
G1 = 'p -> (q -> r)'
G2 = 'p v s'
G3 = 't -> q'
G4 = '~s'
G5 = 'G2 + G4 => G5 = p, Elimination'
G6 = 'G1 + G5 => G6 = q -> r, Modus Ponens'
G7 = 'G3 + G6 => G7 = t -> r, Transitivity'
C = 'G7 => C = ~r -> ~t, Contrapositive'
print('G1 = ', G1)
print('G2 = ', G2)
print('G3 = ', G3)
print('G4 = ', G4)
print('G5 = ', G5)
print('G6 = ', G6)
print('G7 = ', G7)
print('C = ', C)

print('\nc) ')
G1 = 'p -> q'
G2 = '~r v s'
G3 = 'p v r'
G4 = 'G2 => G4 = r -> s, If – then law'
G5 = 'G3 => G5 = ~p -> r, If – then law'
G6 = 'G4 + G5 => G6 = ~p -> s, Transitivity'
G7 = 'G6 => G7 = ~s -> p, Contrapositive'
G8 = 'G1 + G7 => G8 = ~s -> q, Transitivity'
C = 'G9 => C = ~q -> s, Contrapositive'
print('G1 = ', G1)
print('G2 = ', G2)
print('G3 = ', G3)
print('G4 = ', G4)
print('G5 = ', G5)
print('G6 = ', G6)
print('G7 = ', G7)
print('G8 = ', G8)
print('C = ', C)

print('\nd) ')
G1 = 'p'
G2 = 'p -> r'
G3 = 'p -> (q v ~r)'
G4 = '~q v ~s'
G5 = 'G1 + G2 => G5 = r, Modus Ponens'
G6 = 'G1 + G3 => G6 = q v ~r, Modus Ponens'
G7 = 'G5 + G6 => G7 = q, Elimination'
C = 'G4 + G7 => C = ~s, Elimination'
print('G1 = ', G1)
print('G2 = ', G2)
print('G3 = ', G3)
print('G4 = ', G4)
print('G5 = ', G5)
print('G6 = ', G6)
print('G7 = ', G7)
print('C = ', C)
