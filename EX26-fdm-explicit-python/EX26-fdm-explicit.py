import math
import numpy as np
import matplotlib.pylab as plt
#data structures
##physical parameter
alpha = 1.0
##numerical parameters (discretization)
nx = 100
x = np.zeros(nx+1)
dx = 1./nx
t = [0.01]
nt = 500 #wieviele Zeitschritte bis zum stationären Zustand
dt = 0.505 * dx*dx / alpha
Ne = alpha * dt / (dx*dx)
##field function
u = np.zeros(nx+1)
uo = np.zeros(nx+1)
#initial condition
u_ic = 0.
for i in range(nx+1):
	x[i] = 0
	u[i] = 0
	uo[i] = 0
#boundary conditions
u_bc_l = 3.
u_bc_r = -1.
u[0] = uo[0] = u_bc_l
u[nx] = uo[nx] = u_bc_r
#initial state
for i in range(0,nx+1):
    x[i] = (float(i)/float(nx))
plt.plot(x,u,color='blue')
#fdm-explicit
for n in range(1,nt):
	for i in range(1,nx):
		u[i] = uo[i] + Ne *(uo[i-1] - 2*uo[i] + uo[i+1])
	if(n % 10 == 0): 
	    plt.plot(x,u,color='blue')
	for i in range(1,nx):
		uo[i] = u[i]
#plots
plt.title('EX08: explizite Finite-Differenzen-Methode')
plt.xlabel('x')
plt.ylabel('u')
plt.axis('tight')
plt.grid()
plt.savefig("fdm-explicit.png")
plt.show()
