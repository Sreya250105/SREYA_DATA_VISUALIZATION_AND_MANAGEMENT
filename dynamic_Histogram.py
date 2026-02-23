import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))
data = []

for i in range(n):
    val = int(input("Enter value: "))
    data.append(val)

plt.hist(data, bins=5)
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()