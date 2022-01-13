import random

# Ex1:
print('Ex1: ')
print('a)')


def goToRoma(A):
    if A > 3000:
        print('Please enter number less than 3000')
        return
    elif A < 1:
        print('Please enter a number greater than 1')
    result = ''
    value = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    while A != 0:
        for i, j in value.items():
            if A >= j:
                temp = int(A / j)
                A %= j
                result += temp * i
    return result


A = int(input('Please enter your integer number: '))
print(goToRoma(A))

print('\nb): ')


def returnFromRoma(R):
    value = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    prev = None
    for i in R:
        if prev and value[i] > value[prev]:
            result += value[i] - 2 * value[prev]
        else:
            result += value[i]
        prev = i
    return result


R = input('Please enter your roma number: ').upper()
print(returnFromRoma(R))

# Ex2
print('\nEx2: ')


def s(a, b):
    return [a + b for (a, b) in zip(a, b)]


def p(a, b):
    return [a * b for (a, b) in zip(a, b)]


def d(a, b):
    return [a - b for (a, b) in zip(a, b)]


Cal = {'s': '+', 'p': '*', 'd': '-'}
a = [1, 0, 1, 0, 1, 1, 1, 1]
b = [1, 1, 0, 0, 1, 1, 0, 0]

print('b)')
print([a + b for a, b in zip(a, b) if Cal['s']])
print([a * b for a, b in zip(a, b) if Cal['p']])
print([a - b for a, b in zip(a, b) if Cal['d']])

print('\nc)')


def calList(a, b):
    sumList = ([a[i] + b[i] for i in range(len(a))])
    productList = ([a[i] * b[i] for i in range(len(a))])
    diffList = ([a[i] - b[i] for i in range(len(a))])
    print('Sum two list is:', sumList)
    print('Direct product two list is:', productList)
    print('Difference two list is:', diffList)


a = [1, 0, 1, 0, 1, 1, 1, 1]
b = [1, 1, 0, 0, 1, 1, 0, 0]
calList(a, b)

print('\nd)')
a = [random.randint(0, 1) for i in range(5)]
print('The random the first list is:', a)
b = [random.randint(0, 1) for i in range(5)]
print('The random the second list is:', b)

calList(a, b)

print('\ne)')
a = []
n = int(input('Enter number of elements in the first list : '))
for i in range(0, n):
    print('Enter element {}: '.format(i + 1))
    element = int(input())
    a.append(element)
print('The entered the first list is:', a)

b = []
n = int(input('\nEnter number of elements in the second list : '))

for i in range(0, n):
    print('Enter element {}: '.format(i + 1))
    element = int(input())
    b.append(element)
print('The entered the second list is:', b)
print()
calList(a, b)

# Ex3
print('\nEx3:')
print('a)')


def conList(A, B):
    new_List = list()
    A = list(A)
    temp_1 = [A[0][i] for i in range(len(A[0]))]
    temp_1.append(B[0])

    temp_2 = [A[1][i] for i in range(len(A[0]))]
    temp_2.append(B[1])

    new_List.append(tuple(temp_1))
    new_List.append(tuple(temp_2))

    return new_List


A = [(1, 2, 3), (6, 7, 8)]
B = [4, 9]
C = conList(A, B)
print(C)

print('\nb)')


def conList(A, B):
    new_List = list()
    A = list(A)
    temp_1 = [A[0][i] for i in range(len(A[0]))]
    temp_1.append(B[0])

    temp_2 = [A[1][i] for i in range(len(A[0]))]
    temp_2.append(B[1])

    new_List.append(temp_1)
    new_List.append(temp_2)

    return new_List


A = [(1, 2, 3), (6, 7, 8)]
B = [4, 9]
C = conList(A, B)
print(C)
# Ex4
print('\nEx4: ')
print('a)')


def dateCount(seconds):
    years = seconds // (24 * 3600 * 365)
    days = (seconds - (years * (24 * 3600 * 365))) // (3600 * 24)
    hours = (seconds - (years * (24 * 3600 * 365)) - (days * (3600 * 24))) // (60 * 60)
    minutes = (seconds - (years * (24 * 3600 * 365)) - (days * (3600 * 24)) - (hours * (60 * 60))) // 60
    seconds = (seconds - (years * (24 * 3600 * 365)) - (days * (3600 * 24)) - (hours * (60 * 60)) - (minutes * 60))
    return '[%d, %d, %d, %d, %d]' % (years, days, hours, minutes, seconds)


print(dateCount(3600))
print(dateCount(3662))
print(dateCount(31629720))
print(dateCount(873458243))

print('\nb)')


def printDate(Date):
    years = Date // (24 * 3600 * 365)
    days = (Date - (years * (24 * 3600 * 365))) // (3600 * 24)
    hours = (Date - (years * (24 * 3600 * 365)) - (days * (3600 * 24))) // (60 * 60)
    minutes = (Date - (years * (24 * 3600 * 365)) - (days * (3600 * 24)) - (hours * (60 * 60))) // 60
    seconds = (Date - (years * (24 * 3600 * 365)) - (days * (3600 * 24)) - (hours * (60 * 60)) - (minutes * 60))

    years_text = 'year{}'.format('s' if years != 1 else '')
    days_text = 'day{}'.format('s' if days != 1 else '')
    hours_text = 'hour{}'.format('s' if hours != 1 else '')
    minutes_text = 'minute{}'.format('s' if minutes != 1 else '')
    seconds_text = 'second{}'.format('s' if seconds != 1 else '')

    result = ', '.join(filter(lambda x: bool(x), [
        '{0} {1}'.format(years, years_text) if years else '',
        '{0} {1}'.format(days, days_text) if days else '',
        '{0} {1}'.format(hours, hours_text) if hours else '',
        '{0} {1}'.format(minutes, minutes_text) if minutes else '',
        '{0} {1}'.format(seconds, seconds_text) if seconds else ''
    ]))
    return result


print(printDate(3600))
print(printDate(3662))
print(printDate(31629720))
