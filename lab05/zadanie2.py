import random

matrix = [[random.randint(1, 10) for j in range(4)] for i in range(4)]
print(matrix)

diagonal = [matrix[i][i] for i in range(4)]
print(diagonal)