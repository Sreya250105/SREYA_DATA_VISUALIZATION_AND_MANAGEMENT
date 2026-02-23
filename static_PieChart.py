import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [40, 35, 25, 50]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Static Pie Chart")
plt.show()