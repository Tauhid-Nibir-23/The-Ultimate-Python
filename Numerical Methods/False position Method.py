# False Position Method (User-defined equation)

# Take equation input
equation = input("Enter equation in terms of x (example: x**3 - 4*x - 9): ")

# Define function using eval
def f(x):
    return eval(equation)

# Taking interval input
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter maximum iterations: "))

# Check sign condition
if f(a) * f(b) >= 0:
    print("Method not applicable (No sign change).")
else:
    print("\nIter\t a\t\t b\t\t c\t\t f(c)")

    for i in range(max_iterations):

        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

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