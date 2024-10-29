test_matrix = [[1, 0, 1], 
               [2, -1, -3], 
               [0, 2, 7]]

not_square = [[2, 3], [1,9], [0,0]]
ut = [[1, 0, 0, 0], [3, -1, 0, 0], [2, 0, 7, 0], [1, -1, 1, 2]]

two_by_two = [[3, 5], [-1, -2]]

one_val = [[9]]

null_matrix = []

def calculate_determinant(matrix):
    # If matrix does not have a determinant, return INVALID MATRIX
    if len(matrix) == 0 or (len(matrix) != len(matrix[0])): return 'INVALID MATRIX'
    if len(matrix) == 1: return matrix[0][0] # The determinant of a 1x1 matrix is itself.
    if len(matrix) == 2: return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
      
    # Perform a cofactor expansion.
    determinant = 0;
    for col in range(0,len(matrix)):
        # get minor of matrix
        minor = [
            [matrix[i][j] for j in range(len(matrix)) if j!= col] for i in range(1, len(matrix))
        ]
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(minor)
    
    return determinant
print(calculate_determinant(ut))
