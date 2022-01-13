import random


def rand(n):
    salary = [27, 61, 52, 69, 88, 85, 99, 90, 77, 145, 41, 83, 140, 74, 143, 131, 34, 59, 46, 108,
              61, 128, 114, 138, 24, 67, 130, 56, 79, 145, 87, 40, 119, 40, 15, 44, 113, 45, 25, 94,
              86, 128, 69, 102, 91, 106, 119, 139, 67, 47, 42, 102, 124, 31, 39, 68, 105, 138, 100, 84,
              76, 66, 128, 146, 41]
    list = []
    temp = []

    for i in range(0, n):
        x = random.randint(1, 65)
        while x in list:
            x = random.randint(1, 65)
        list.append(x)

    for i in range(0, len(list)):
        temp.append(salary[list[i] - 1])
    print('STT: ', list)
    print('Salary: ', temp)


print('S1:')
rand(30)
print('S2:')
rand(15)
