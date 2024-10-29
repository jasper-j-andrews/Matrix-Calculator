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
    print(C)
    return C

calculate_product(X, Y)
calculate_product(Z, X)
calculate_product(X, Z)
calculate_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[-1, 0, 0],[0, 2, 0], [0, 0, 5]])
calculate_product([[2, 1, 2], [3, 0, -1], [8, 1, 7]], [[2], [-9], [5]])
calculate_product([[2, 5, 6], [1, 0, -2], [-1, -2, 4]], [[1, 2, 1], [0, -3, -1], [1, 0, 0]])