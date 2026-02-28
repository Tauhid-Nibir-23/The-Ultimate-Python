# Cramer's Rule (Same Input Style as Gauss Elimination)

# Function to calculate determinant (recursive)
def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        submatrix = []
        for row in range(1, n):
            temp = []
            for c in range(n):
                if c != col:
                    temp.append(matrix[row][c])
            submatrix.append(temp)

        det += ((-1)**col) * matrix[0][col] * determinant(submatrix)

    return det


# ---- Main Program ----

n = int(input("Enter number of variables: "))

a = []

print("Enter coefficients row-wise including constant term:")
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

# Separate coefficient matrix A and constant vector B
A = []
B = []

for i in range(n):
    A.append(a[i][:n])   # first n elements
    B.append(a[i][n])    # last element

# Main determinant
D = determinant(A)

if D == 0:
    print("No unique solution (Determinant = 0)")
else:
    print("\nSolution:")

    for i in range(n):
        # Copy matrix
        Ai = []
        for row in range(n):
            temp = A[row].copy()
            temp[i] = B[row]
            Ai.append(temp)

        Di = determinant(Ai)
        xi = Di / D

        print("x", i+1, "=", round(xi, 6))