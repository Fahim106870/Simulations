import random
import matplotlib.pyplot as plt

def func(x):
    return x**3

n = 0
m = 0

print("{:<12} {:<14} {:<10} {:<6} {:<6}".format(
    "Random X", "Random Y", "x^3", "M", "N"))

for i in range(100):
    rx = random.randint(200, 500) / 100  # Random X between 2.00 and 5.00
    ry = random.randint(0, 140)         # Random Y between 0 and 140
    fx = func(rx)
    n += 1
    under_curve = ry <= fx
    if under_curve:
        m += 1
        plt.scatter(rx, ry, color="green")  # Under curve
    else:
        plt.scatter(rx, ry, color="blue")   # Above curve

    print("{:<12.2f} {:<14} {:<10.2f} {:<6} {:<6}".format(
        rx, ry, fx, m, n))

x = []
y = []
i = 2.0
h = 0.1
while i <= 5.0:
    x.append(i)
    y.append(func(i))
    i = round(i + h, 2)

plt.plot(x, y, color='red', label='y = x^3')
plt.title("Monte Carlo Integration of x^3 from 2 to 5")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

area = (m / n) * (3 * 140)
print(f"\nEstimated Area ≈ (M/N) * 420 = ({m}/{n}) * 420 = {area:.4f}")
