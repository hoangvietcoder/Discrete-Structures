import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Ex1
print('Ex1: ')


# a. Write function mPlus(A,B) to calculate the sum of two matrix 𝐴, 𝐵 knowing that 𝐴 +
# 𝐵 = 𝐶 where 𝐶𝑖,𝑗 = 𝐴𝑖,𝑗 + 𝐵𝑖,𝑗
def mPlus(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        return None
    else:
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j] + B[i][j])
            result.append(temp)
        return result


# b. Write function mMinus(A,B) to calculate the difference of two matrix 𝐴, 𝐵 knowing
# that 𝐴 − 𝐵 = 𝐶 where 𝐶𝑖,𝑗 = 𝐴𝑖,𝑗 − 𝐵𝑖,𝑗
def mMinus(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        return None
    else:
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j] - B[i][j])
            result.append(temp)
        return result


# c. Write function mMultiply(A,B) to calculate the difference of two matrix 𝐴, 𝐵 knowing
# that 𝐴 ∗ 𝐵 = 𝐶 where 𝐶𝑖,𝑗 = ∑ 𝐴𝑖,𝑘 ∗ 𝐵𝑘,𝑗 (remember that python count from 0 not 1)
def mMultiply(A, B):
    if len(A[0]) != len(B):
        return None
    else:
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                temp = 0
                for k in range(len(A[0])):
                    temp += A[i][k] * B[k][j]
                result[i][j] = temp
        return result


# d. Write function mTranspose(A) to calculate the transpose matrix of 𝐴 where 𝐴𝑖,𝑗 = 𝐴𝑗,𝑖
def mTranspose(A):
    result = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            result[i][j] = A[j][i]
    return result


# e. Test your functions with A is the blue matrix and B is the yellow matrix
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(mPlus(A, B))
print(mMinus(A, B))
print(mMultiply(A, B))
print(mMultiply(B, A))
print(mTranspose(A))
print(mTranspose(B))

print()

A = [[1, 4, 6, 10], [2, 7, 5, 3]]
B = [[1, 4, 6], [2, 7, 5], [9, 0, 11], [3, 1, 0]]
print(mMultiply(A, B))
print(mTranspose(A))
print(mTranspose(B))

# Ex2:
print('\nEx2: ')
A1 = np.array([[0, 0, 3, 0, 1],
               [0, 0, 5, 3, 0],
               [3, 5, 0, 1, 0],
               [0, 3, 1, 0, 2],
               [1, 0, 0, 2, 0]])

G1 = nx.from_numpy_matrix(A1)
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a: b for
                                                        a, b in enumerate('abcde')})
edge_labels = nx.draw_networkx_edge_labels(G1, font_size=6,
                                           pos=pos, label_pos=0.5)
plt.axis('equal')
plt.show()

#
A1 = np.array([[0, 0, 0, 0, 1, 1],
               [0, 0, 5, 3, 0, 0],
               [0, 5, 0, 1, 5, 0],
               [0, 3, 1, 2, 3, 0],
               [1, 0, 5, 2, 0, 6],
               [1, 0, 0, 3, 6, 0]])

G1 = nx.from_numpy_matrix(A1)
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a: b for
                                                        a, b in enumerate('abcdef')})
edge_labels = nx.draw_networkx_edge_labels(G1, font_size=6,
                                           pos=pos, label_pos=0.5)
plt.axis('equal')
plt.show()

# Ex3
print('\nEx3:')
A1 = np.array([[0, 0, 5, 3, 0, 0],
               [0, 0, 3, 2, 0, 0],
               [5, 3, 0, 1, 3, 0],
               [3, 2, 1, 0, 1, 3],
               [0, 0, 3, 1, 4, 0],
               [0, 0, 0, 3, 4, 0]])
G1 = nx.from_numpy_matrix(A1)
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a: b for
                                                        a, b in enumerate('abcdef')})
edge_labels = nx.draw_networkx_edge_labels(G1, font_size=6,
                                           pos=pos, label_pos=0.5)
plt.axis('equal')
plt.show()


A1 = np.array([[0, 0, 2, 3, 3, 0],
               [0, 0, 3, 2, 0, 0],
               [2, 3, 0, 2, 8, 6],
               [3, 2, 2, 0, 0, 5],
               [3, 0, 8, 0, 0, 3],
               [0, 0, 6, 5, 3, 0]])
G1 = nx.from_numpy_matrix(A1)
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a: b for
                                                        a, b in enumerate('abcdef')})
edge_labels = nx.draw_networkx_edge_labels(G1, font_size=6,
                                           pos=pos, label_pos=0.5)
plt.axis('equal')
plt.show()

# Ex4
print('\nEx4: ')

# Ex 5
print('\nEx5: ')
A = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

G1 = nx.from_numpy_matrix(A)
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos=pos, with_labels=True, labels={a: b for
                                                        a, b in enumerate(
            ["Primates", "Rodents", "Mammals", "Reptiles", "Animals", "Plant", "Mushrooms", "Molds", "Multicellular",
             "Yeasts", "Unicellular"])})
plt.figure(figsize=(60, 60))
plt.show()
