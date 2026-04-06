import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**3 - x - 2

# Bisection Method Function
def bisection(a, b, tol=0.0001, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return

    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    print("-"*60)

    for i in range(max_iter):
        c = (a + b) / 2
        print(f"{i+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")

        if abs(f(c)) < tol:
            print("\nRoot found:", c)
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Initial values
a = 1
b = 2

root = bisection(a, b)

# Graphical Representation
x = np.linspace(0, 3, 400)
y = f(x)

plt.axhline(0)
plt.plot(x, y, label="f(x) = x^3 - x - 2")
plt.scatter(root, f(root), color='red', label="Root")
plt.title("Bisection Method Graph")
plt.legend()
plt.grid()
plt.show()