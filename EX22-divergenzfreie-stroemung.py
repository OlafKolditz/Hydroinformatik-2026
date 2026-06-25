import numpy as np
import matplotlib.pyplot as plt
#matplotlib notebook
# set up a normalized grid:
dim= 20
xarray= np.arange(-dim,dim)
yarray= np.arange(-dim,dim)

# (fluid) flow from a source at L to a sink at -L:
L = dim/4
x,y = np.meshgrid(xarray,yarray)
vx = (x-L)/((x-L)**2+y**2) - (x+L)/((x+L)**2 +y**2)
vy = y/((x-L)**2+y**2) - y/((x+L)**2 +y**2)

# Masking the singularities at the poles:
threshold = 0.8
Mx = np.abs(vx) > threshold
My = np.abs(vy) > threshold
vx = np.ma.masked_array(vx, mask=Mx)
vy = np.ma.masked_array(vy, mask=My)

# plot the flow lines:
plt.figure()
plt.quiver(x,y, vx, vy, pivot='mid')
plt.xlabel("$x$-axis")
plt.ylabel("$y$-axis")
plt.axis('equal')
plt.show()


