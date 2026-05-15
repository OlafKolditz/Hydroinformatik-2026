import math
import matplotlib.pylab as plt

PI = 3.14159265358979323846
numPoints = 100
alpha = 1.0
t = [0.001, 0.1, 0.5, 0.7, 1.0, 2.0]

# Precompute x coordinates (same for all curves)
x = [float(i) / numPoints for i in range(numPoints + 1)]

for n in t:
    y = [math.sin(PI * xi) * math.exp(-alpha * n * n) for xi in x]
    plt.plot(x, y, label=f't = {n}')   # Add label

plt.xlabel('x')
plt.ylabel('u')
plt.legend()            # Show the labels
plt.axis('tight')
plt.savefig("ex08c-function.png")
plt.show()