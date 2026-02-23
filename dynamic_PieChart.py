import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

labels = []
sizes = []

for i in range(n):
    label = input("Enter label: ")
    size = int(input("Enter value: "))
    labels.append(label)
    sizes.append(size)

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Dynamic Pie Chart")
plt.show()