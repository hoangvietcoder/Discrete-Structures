# Câu 1
a = 15 * 2 + 7 * 8
print(a)

b = 20 - 15 + 15 * 2
print(b)

c = 20 + 30 - 3 * 15 + 5 * 5 ** 2
print(c)

d = (4 / 6 + 2 / 6) / (5 / 2 + 1 / 2)
print(d)

e = 14 / 2 + 7
print(e)

f = (5 * 2) / (5 - 20 * 3 ** 2 + 30)
print(f)

# Câu 2
print("15*2+7*8 =", a)


# Câu 3
def sumN(n):
    sum = 0
    if n > 0:
        for i in range(0, n + 1):
            sum += i
    else:
        for i in range(n, 0):
            sum += i
    return sum


n = int(input('Enter n: '))
print("Sum: " + format(sumN(n)))

# Câu 4
A = str(input('Enter your string: '))
B = A.split()
C = " ".join(B)
D = "_".join(B)
print(C)
print(D)

# Câu 5
str_input = input('Enter the calculation(a+b): ')
first_number = ''
operator = ['+', '-', '*', '/', '%', '^']
second_number = ''
tmp = ''
t = ''

for i in range(0, len(str_input)):
    if str_input[i] in operator:
        tmp = str_input[i]
        first_number = t
        t = ''
    else:
        t += str_input[i]

second_number = t
n1 = int(first_number)
n2 = int(second_number)

if tmp == '+':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 + n2))
elif tmp == '-':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 - n2))
elif tmp == '*':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 * n2))
elif tmp == '/':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 / n2))
elif tmp == '%':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 % n2))
elif tmp == '^':
    print('{} {} {} = {}'.format(first_number, tmp, second_number, n1 ** n2))

# Câu 6
dictionary = {'+': n1 + n2, '-': n1 - n2, '*': n1 * n2, '/': n1 / n2, '%': n1 % n2, '^': n1 ** n2}
print('{} {} {} = {}'.format(first_number, tmp, second_number, dictionary[tmp]))


# Câu 7


def mSum(A, B):
    if len(A) != len(B):
        return []
    else:
        for i in range(len(A)):
            if len(A[i]) != len(B[i]):
                return []
        result = A
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] + B[i][j]
        return result


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = mSum(A, B)

if C == []:
    print("Matrix dimension error")
else:
    for item in C:
        print(item)

# Câu 8:
A = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

B = [[1, 2, 3, 4],
     [4, 5, 6, 7],
     [7, 8, 9, 10]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for item in result:
    print(item)


# Câu 9
def ithCombine(p, q):
    return "if " + p + ", then " + q


def panqCombine(p, q):
    temp = q.split()
    return p + " and " + temp[0] + " not " + temp[1] + " " + temp[2]


def npoqCombine(p, q):
    temp = p.split()
    return temp[0] + " not " + temp[1] + ", or " + q


p = "it sunny"
q = "I go camping"
print(ithCombine(p, q))
print(panqCombine(p, q))
print(npoqCombine(p, q))
