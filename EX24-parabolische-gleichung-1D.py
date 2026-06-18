import math
import matplotlib.pylab as plt
PI = 3.14159265358979323846
numPoints = 100
alpha = 1.0
t = [0.01,0.1,0.2,0.5,1.0,1.5,2.0]
x = []
y = []
for n in t:
    for i in range(0,numPoints+1):
        x.append(float(i)/float(numPoints))
        #y.append(math.sin(PI*x[i]) * math.exp(-alpha*n*n))
        y.append(math.sin(math.pi*x[i]) * math.exp(-alpha*n*n))
    plt.plot(x,y,color='blue')
    x = []
    y = []
plt.xlabel('x')
plt.ylabel('u')
plt.axis('tight')
plt.savefig("diffusion-equation.png")
plt.show()