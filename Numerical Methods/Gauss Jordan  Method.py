# Gauss-Jordan Method

n = int(input("Enter number of variables: "))

# Taking augmented matrix input
a = []
print("Enter coefficients row-wise including constant term:")

for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

# Gauss-Jordan elimination
for i in range(n):
    
    # Make pivot element 1
    pivot = a[i][i]
    if pivot == 0:
        print("Mathematical Error (Zero Pivot)")
        break
    
    for j in range(n + 1):
        a[i][j] = a[i][j] / pivot

    # Make other elements in column zero
    for k in range(n):
        if k != i:
            factor = a[k][i]
            for j in range(n + 1):
                a[k][j] = a[k][j] - factor * a[i][j]

# Display Solution
print("\nSolution:")
for i in range(n):
    print("x", i+1, "=", round(a[i][n], 6))