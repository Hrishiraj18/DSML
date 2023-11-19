import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
labels = ['A', 'B', 'C', 'D', 'E']

colors = ['red', 'blue', 'green', 'orange', 'purple']
markers = ['o', 's', '^', 'D', 'v']

for i in range(len(x)):
    plt.scatter(x[i], y[i], label=labels[i], color=colors[i], marker=markers[i])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Labeled Data Points')
plt.legend()

plt.show()