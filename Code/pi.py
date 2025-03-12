import math
import random
import matplotlib.pyplot as plt

def func(x):
    return math.sqrt(1 - x**2)

m = 0
n = 0

print("{:<6} {:<6} {:<16} {:<6}".format("R1", "R2", "sqrt(1 - R1^2)", "In/Out"))

for i in range(40):
    rx = random.randint(0, 1000) / 1000   # Random X between 0 and 1
    ry = random.randint(0, 1000) / 1000   # Random Y between 0 and 1
    fx = func(rx)
    n += 1
    if ry <= fx:
        m += 1
        plt.scatter(rx, ry, color="green")  #  inside
        status = "In"
    else:
        plt.scatter(rx, ry, color="blue")   # outside
        status = "Out"

    print("{:<6.2f} {:<6.2f} {:<16.4f} {:<6}".format(rx, ry, fx, status))

x = []
y = []
i = 0
h = 0.01
while i <= 1:
    x.append(i)
    y.append(func(i))
    i = round(i + h, 2)

plt.plot(x, y, color="red", label="y = √(1 - x²)")
plt.title("Monte Carlo Simulation: Area under Quarter Circle")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

area = (m / n) * 4
error = abs(math.pi - area) * 100 / math.pi
print("\nTotal Points In (M):", m)
print("Total Points (N):", n)
print(f"Estimated = {area:.5f}")
print(f"Error: {error:.4f}%")
