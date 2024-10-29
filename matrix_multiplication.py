X = [[3, 1, -2], [0, 1, 2], [-1, 7, 0]]
Y = [[2, 1, 0], [0, -1, 3], [1, 0, 2]]
Z = [[-1], [3], [10]]

def calculate_product(A, B):
    if len(A[0]) != len(B): return "CAN NOT BE MULTIPLIED"
    C = []
    for i in range(0, len(A)):
        c_row = []
        for j in range(0, len(B[0])): 
            sum = 0
            for x in range(0, len(A[0])):
                sum += A[i][x]*B[x][j]
            c_row.append(sum)
        C.append(c_row)
    return C

calculate_product(X, Y)
calculate_product(Z, X)
calculate_product(X, Z)