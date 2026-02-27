# Gauss Elimination Method

n = int(input("Enter number of variables: "))

# Create augmented matrix
a = []

print("Enter coefficients row-wise including constant term:")
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

# Forward Elimination
for i in range(n):
    if a[i][i] == 0.0:
        print("Mathematical Error (Division by zero)")
        break
        
    for j in range(i+1, n):
        ratio = a[j][i] / a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x = [0 for i in range(n)]

x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j] * x[j]
        
    x[i] = x[i] / a[i][i]

# Display solution
print("\nSolution:")
for i in range(n):
    print("x", i+1, "=", round(x[i], 6))