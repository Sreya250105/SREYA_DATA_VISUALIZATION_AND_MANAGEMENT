import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x_val = int(input("Enter x value: "))
    y_val = int(input("Enter y value: "))
    x.append(x_val)
    y.append(y_val)

plt.scatter(x, y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Dynamic Scatter Plot")
plt.show()