import math

# Ex1
print('Ex1: ')
A1 = [2,
      7, 5,
      2, 6, None, 9,
      None, None, 5, 11, None, None, 4, None]

B1 = [50,
      17, 76,
      9, 23, 54, None,
      None, 14, 19, None, None, 72, None, None,
      None, None, 12, None, None, None, None, None, None, None, 67, None, None, None, None, None]


def printLevel(A):
    for i in range(int(math.sqrt(len(A) + 1))):
        for j in range(int(2 ** i - 1), int(2 ** (i + 1) - 1), 1):
            print(A[j], end=" ")
        print()


printLevel(A1)
print()
printLevel(B1)


# Ex2


class treeNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


A2 = treeNode(2)
A2.left = treeNode(7)
A2.right = treeNode(5)
B2 = A2.left
C2 = A2.right
B2.left = treeNode(2)
B2.right = treeNode(6)
C2.right = treeNode(9)
D2 = B2.left
E2 = B2.right
G2 = C2.right
E2.left = treeNode(5)
E2.right = treeNode(11)
G2.left = treeNode(4)

A3 = treeNode(50)
A3.left = treeNode(17)
A3.right = treeNode(76)
B3 = A3.left
C3 = A3.right
B3.left = treeNode(9)
B3.right = treeNode(23)
C3.left = treeNode(54)
D3 = B3.left
E3 = B3.right
F3 = C3.left
D3.right = treeNode(14)
E3.left = treeNode(19)
F3.right = treeNode(72)
I3 = D3.right
K3 = E3.left
N3 = F3.right
I3.left = treeNode(12)
N3.left = treeNode(67)

# Ex3
print('\nEx3: ')


def NLR(A):
    if A is None:
        return
    else:
        print(A.data, end=" ")
        NLR(A.left)
        NLR(A.right)


def LNR(A):
    if A is None:
        return
    else:
        LNR(A.left)
        print(A.data, end=" ")
        LNR(A.right)


def LRN(A):
    if A is None:
        return
    else:
        LRN(A.left)
        LRN(A.right)
        print(A.data, end=" ")


NLR(A2)
print()
NLR(A3)
print()
LNR(A2)
print()
LNR(A3)
print()
LRN(A2)
print()
LRN(A3)
print()
# Ex4
print('\nEx4: ')


def breadthFirstSearch(A, Data):
    queue = [A]
    print(A.data, end=" ")
    while queue:
        temp = queue.pop(0)
        if temp.left is not None:
            queue.append(temp.left)
            print(temp.left.data, end=" ")
            if temp.left.data == Data:
                return ''
        if temp.right is not None:
            queue.append(temp.right)
            print(temp.right.data, end=" ")
            if temp.right.data == Data:
                return ''


def depthFirstSearch(A, Data):
    stack = []
    print(A.data, end=" ")
    if A.left is not None:
        stack.append(A.left)
    if A.right is not None:
        stack.append(A.right)
    while stack:
        temp = stack.pop()
        print(temp.data, end=" ")
        if temp.data == Data:
            return
        if temp.left is not None:
            stack.append(temp.left)
        if temp.right is not None:
            stack.append(temp.right)


breadthFirstSearch(A2, 11)
print()
breadthFirstSearch(A3, 19)
print()
depthFirstSearch(A2, 11)
print()
depthFirstSearch(A3, 19)
print()


# Ex5


def breadthFirstSearchV(A, Data):
    for i in range(len(A)):
        if A[i] is not None:
            print(A[i], end=" ")
            if A[i] == Data:
                return


print()
breadthFirstSearchV(A1, 11)
print()
breadthFirstSearchV(B1, 19)
print()
