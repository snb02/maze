from numpy import *
#from pylab import plot, show, grid
import matplotlib.pyplot as plt
#from celluloid import Camera

P=array([[1,2,3,4,5],[1,2,3,4,5]])
Q=array([[5, 6, 7, 8],[5, 6, 7, 8]])
plt.plot(P[0,:],P[1,:], 'black')
plt.plot(Q[0,:],Q[1,:], 'black')



plt.show()