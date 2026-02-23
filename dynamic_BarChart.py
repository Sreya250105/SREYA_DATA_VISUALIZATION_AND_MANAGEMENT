import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

categories = []
values = []

for i in range(n):
    cat = input("Enter category name: ")
    val = int(input("Enter value: "))
    categories.append(cat)
    values.append(val)

plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Dynamic Bar Chart")
plt.show()