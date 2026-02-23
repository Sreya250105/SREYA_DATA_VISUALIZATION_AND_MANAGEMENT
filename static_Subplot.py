import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.subplot(1, 2, 1)   
plt.plot(x, [1, 4, 9, 16])
plt.xlabel("Input Data")
plt.ylabel("Squared Value")
plt.title("SQUARE")

plt.subplot(1, 2, 2)   
plt.plot(x, [1, 8, 27, 64])
plt.title("CUBE")
plt.xlabel("Input Data")
plt.ylabel("Cubic Value")
plt.show()