import numpy as np
import matplotlib.pyplot as plt

length = 1000
height = 600
deviation_x = length / 2
deviation_y = height / 2

def getRNN():
    return np.random.randn()

HIT = 0
N = 0

print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Strike No", "RNN (x)", "x", "RNN (y)", "Result"))

for i in range(1, 21):
    rnn_x = getRNN()
    rnn_y = getRNN()

    x = rnn_x * deviation_x
    y = rnn_y * deviation_y

    if (x <= length / 2 and x >= -length / 2) and (y <= height / 2 and y >= -height / 2):
        HIT += 1
        result = "Hit"
        plt.scatter(x, y, color="green")
    else:
        result = "Miss"
        plt.scatter(x, y, color="blue")

    print("{:<15} {:<10.2f} {:<10.2f} {:<10.2f} {:<10}".format(i, rnn_x, x, rnn_y, result))

    N += 1

area_x = [-500, 500, 500, -500, -500]
area_y = [-300, -300, 300, 300, -300]
plt.plot(area_x, area_y, color="red")

plt.title("Bomb Strike Simulation (Hit or Miss)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

print("\nNumber of strikes: ", N)
print("Number of hits: ", HIT)
print("Accuracy: ", (HIT / N) * 100, "%")
