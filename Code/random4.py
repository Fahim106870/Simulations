import random
import matplotlib.pyplot as plt

for asa in range(1):
    step = 0
    x = 0
    y = 0
    dotx = []
    doty = []
    direction = []
    F_L_R = [0.5, 0.3, 0.2]
    F_L_R = [int(10 * i) for i in F_L_R]  # Convert to range scale (0-9)

    while step <= 20:

        rn = random.randint(0, 9)

        if rn in range(F_L_R[0]):       # Forward (North)
            direction.append('F')
            y += 1
            dotx.append(x)
            doty.append(y)
        elif rn in range(F_L_R[0], F_L_R[0] + F_L_R[1]):  # Left (West)
            direction.append('L')
            x -= 1
            dotx.append(x)
            doty.append(y)
        else:                           # Right (East)
            direction.append('R')
            x += 1
            dotx.append(x)
            doty.append(y)
        step += 1

    # Plot the path
    plt.plot(dotx, doty, marker='o', linestyle='-', color='b')

plt.title("Random Walk with Forward, Left, and Right Movements")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
