import matplotlib.pyplot as plt
n = int(input("Enter number of data points: "))

x = []
y = []
for i in range(n):
    x_val = int(input(f"Enter x value {i+1}: "))
    y_val = int(input(f"Enter y value {i+1}: "))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y)
plt.title("Dynamic Line Chart (User Input)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()