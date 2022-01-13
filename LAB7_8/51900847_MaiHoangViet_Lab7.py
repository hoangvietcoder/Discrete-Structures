import math
import random
from collections import Counter

# Ex1
print('Ex1: ')
list = [1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]
print(set(list))

# Ex2
print('\nEx2: ')


def Diff(list_1, set_1):
    a = []
    for i in set_1:
        a.append(i)

    li_dif = [i for i in list_1 + a if i not in list_1 or i not in a]
    return li_dif


users = ['tom', 'pam', 'sasha', 'jj', 'que', 'jeff']
bad = set(['jeff', 'sasha'])
print(Diff(users, bad))

# Ex3
print('\nEx3: ')
count = 0
n = 1000000
for i in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == 2 or die2 == 5 or die1 == 5 or die2 == 2:
        count += 1
print(count / n)

# Ex4:
print('\nEx4: ')
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
numbers = ['1', '2', '3', '4', '5', '6', '7']
tmp = []
for item in zip(days, numbers):
    tmp.append(item)

n = (input('Please enter your number or day of week: '))
if n in days:
    for i in tmp:
        if n in i:
            print('{} -> {}'.format(n, i[1]))

if n in numbers:
    for i in tmp:
        if n in i:
            print('{} -> {}'.format(n, i[0]))

# Ex5:
print('\nEx5: ')
list = ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog',
        'dog', 'pear', 'pencil', 'pear', 'pear']
print(dict(Counter(list)))

# Ex6:
print('\nEx6: ')
temp = dict(Counter(list))
sort_dict = sorted(temp.items(), key=lambda x: x[1], reverse=True)
for i in sort_dict[:2]:
    print(i[0], i[1])

# Ex7:
print('\nEx7: ')


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sumList(list):
    arr = []
    for num in list:
        if num < 0:
            num = -num
        arr += [item for item in range(1, num + 1) if (num % item == 0 and isPrime(item) and item not in arr)]
    temp_arr = []
    for item in sorted(arr):
        temp = 0
        for num in list:
            if num % item == 0:
                temp += num
        temp_arr.append([item, temp])
    return temp_arr


a = [12, 15]
b = [15, 21, 24, 30, -45]
print(sumList(a))
print(sumList(b))
