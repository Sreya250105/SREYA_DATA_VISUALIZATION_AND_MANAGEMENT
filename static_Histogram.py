import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 40, 40, 40, 50]

plt.hist(data, bins=5)
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Static Histogram")
plt.show()