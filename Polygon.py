from numpy import *
from pylab import plot, show, grid
import matplotlib.pyplot as plt
from celluloid import Camera

# Startwerte (x = x-Achse, y = y-Achse, p = erste Box, q = zweite Box)

px0 = 3
px1 = 5
py0 = 2
py1 = 3
qx0 = 6
qx1 = 7
qy0 = 1
qy1 = 2

n=100
# Intervall
dt=.01

fig=plt.figure()
camera=Camera(fig)
a='b'
for i in range (0,n):

    px0+=dt
    px1+=dt
    py0-=dt/2
    py1-=dt/2
    qx0-=dt
    qx1-=dt
    qy0+=dt
    qy1+=dt

    P=array([[px0,px1,px1,px0,px0],[py0,py0,py1,py1,py0]])
    Q=array([[qx0,qx1,qx1,qx0,qx0],[qy0,qy0,qy1,qy1,qy0]])


    def ZweiBoxKollision (P, Q): # Kollision zweier Kugeln

        if(qx0 > px1): # Wenn der Abstand kleiner als die addierten Radien findet eine Kollission statt
            return True
        elif(py0 == qy0): # Wenn der Abstand kleiner als die addierten Radien findet eine Kollission statt
            return True
        return False # keine Kollision

    Kollision = ZweiBoxKollision(P, Q)

    if(Kollision == True): #wenn die Boxen Kollidieren, soll die erste Box seine Farbe in Rot Ã¤ndern
        a = 'r'
    if(Kollision == False):
        a = 'b'


    plt.plot(P[0,:],P[1,:],a)
    plt.plot(Q[0,:],Q[1,:],a)



    camera.snap()

anim = camera.animate()
plt.show()