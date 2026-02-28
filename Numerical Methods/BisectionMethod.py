def f(x):
    return x**3 - 4*x - 9   # You can change this equation if needed

# Taking input from user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
tolerance = float(input("Enter tolerance (e.g., 0.0001): "))
max_iterations = int(input("Enter maximum iterations: "))

# Check condition
if f(a) * f(b) >= 0:
    print("Bisection method not applicable.")
else:
    print("\nIter\t a\t\t b\t\t c\t\t f(c)")
    
    for i in range(max_iterations):
        c = (a + b) / 2
        
        print(i+1, "\t", round(a,6), "\t", round(b,6),
              "\t", round(c,6), "\t", round(f(c),6))
        
        if abs(f(c)) < tolerance:
            print("\nRoot found successfully!")
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nApproximate Root =", round(c,6))