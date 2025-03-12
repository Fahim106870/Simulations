coords = []
n = int(input("How many coordinates? "))

for i in range(n):
    x = int(input(f"Enter x for point {i+1}: "))
    y = int(input(f"Enter y for point {i+1}: "))
    coords.append((x, y))

print("Coordinates:", coords)
