import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

length = 1000
height = 1000
deviation_x = length / 2
deviation_y = length / 2

def getRNN():
    return np.random.randn()

poin_x = []
poin_y = []
HIT = 0
N = 0

print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Strike No", "RNN (x)", "x", "RNN (y)", "Result"))

for i in range(1, 11):
    rnn_x = getRNN()
    rnn_y = getRNN()

    x = rnn_x * deviation_x
    y = rnn_y * deviation_y

    if (x**2 + y**2) <= (500*500):
        HIT += 1
        result = "Hit"
        plt.scatter(x, y, color="green")
    else:
        result = "Miss"
        plt.scatter(x, y, color="blue")

    print("{:<15} {:<10.2f} {:<10.2f} {:<10.2f} {:<10}".format(i, rnn_x, x, rnn_y, result))

    poin_x.append(x)
    poin_y.append(y)
    N += 1

fig = plt.figure()
ax = fig.add_subplot()
circle1 = patches.Circle((0, 0), radius=500, color='red')
ax.add_patch(circle1)
ax.axis('equal')

plt.scatter(poin_x, poin_y)
plt.show()

print("\nNumber of strikes: ", N)
print("Number of hits: ", HIT)
print("Accuracy: ", (HIT / N) * 100, "%")
