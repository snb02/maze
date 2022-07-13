# from numpy import *
# #from pylab import plot, show, grid
# import matplotlib.pyplot as plt
# #from celluloid import Camera
#
# P=array([[1,2,3,4,5],[1,2,3,4,5]])
# Q=array([[5, 6, 7, 8],[5, 6, 7, 8]])
# plt.plot(P[0,:],P[1,:], 'black')
# plt.plot(Q[0,:],Q[1,:], 'black')
import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as pl

plt.axes()

A = plt.Rectangle((-1, 1), 1, 9, fc='black' ,ec="black")
B = plt.Rectangle((-1,10), 21, 1, fc='black',ec="black")
C = plt.Rectangle((19,0), 1,9, fc='black',ec="black")
D = plt.Rectangle((-1,-1), 21, 1, fc='black',ec="black")
E = plt.Rectangle((1, 6), 1, 4, fc='black' ,ec="black")
F = plt.Rectangle((2, 6), 3, 1, fc='black' ,ec="black")
G = plt.Rectangle((3, 8), 3, 1, fc='black' ,ec="black")
H = plt.Rectangle((6, 6), 1, 4, fc='black' ,ec="black")
I = plt.Rectangle((8, 8), 1, 2, fc='black' ,ec="black")
J = plt.Rectangle((9, 8), 3, 1, fc='black' ,ec="black")
K = plt.Rectangle((13, 8), 1, 2, fc='black' ,ec="black")
L = plt.Rectangle((15, 7), 1, 2, fc='black' ,ec="black")
M = plt.Rectangle((17, 8), 1, 2, fc='black' ,ec="black")
N = plt.Rectangle((8, 6), 1, 1, fc='black' ,ec="black")
O = plt.Rectangle((9,5), 1, 2, fc='black',ec="black")
P = plt.Rectangle((11,6), 8, 1, fc='black',ec="black")
Q = plt.Rectangle((0,4), 5, 1, fc='black',ec="black")
R = plt.Rectangle((5,1), 1, 4, fc='black',ec="black")
S = plt.Rectangle((7,4), 3, 1, fc='black',ec="black")
T = plt.Rectangle((11,0), 1, 5, fc='black',ec="black")
U = plt.Rectangle((13,3), 1, 2, fc='black',ec="black")
V = plt.Rectangle((14,4), 4, 1, fc='black',ec="black")
W = plt.Rectangle((1,0), 1, 3, fc='black',ec="black")
X = plt.Rectangle((2,2), 2, 1, fc='black',ec="black")
Y = plt.Rectangle((3,1), 1, 1, fc='black',ec="black")
Z = plt.Rectangle((7,1), 1, 3, fc='black',ec="black")
A1 = plt.Rectangle((8,1), 2, 1, fc='black',ec="black")
B1 = plt.Rectangle((9,2), 1, 1, fc='black',ec="black")
C1 = plt.Rectangle((12,2), 2, 1, fc='black',ec="black")
D1 = plt.Rectangle((15,2), 1, 1, fc='black',ec="black")
E1 = plt.Rectangle((17,1), 1, 3, fc='black',ec="black")
F1 = plt.Rectangle((15,1), 2, 1, fc='black',ec="black")
G1 = plt.Rectangle((13,0), 1, 1, fc='black',ec="black")


plt.gca().add_patch(A)
plt.gca().add_patch(B)
plt.gca().add_patch(C)
plt.gca().add_patch(D)
plt.gca().add_patch(E)
plt.gca().add_patch(F)
plt.gca().add_patch(G)
plt.gca().add_patch(H)
plt.gca().add_patch(I)
plt.gca().add_patch(J)
plt.gca().add_patch(K)
plt.gca().add_patch(L)
plt.gca().add_patch(M)
plt.gca().add_patch(N)
plt.gca().add_patch(O)
plt.gca().add_patch(P)
plt.gca().add_patch(Q)
plt.gca().add_patch(R)
plt.gca().add_patch(S)
plt.gca().add_patch(T)
plt.gca().add_patch(U)
plt.gca().add_patch(V)
plt.gca().add_patch(W)
plt.gca().add_patch(X)
plt.gca().add_patch(Y)
plt.gca().add_patch(Z)
plt.gca().add_patch(A1)
plt.gca().add_patch(B1)
plt.gca().add_patch(C1)
plt.gca().add_patch(D1)
plt.gca().add_patch(E1)
plt.gca().add_patch(F1)
plt.gca().add_patch(G1)



#figure, axes = plt.subplots()

circlebody = pl.Ellipse((0.5, 0.5), 0.8, 0.6, color='orange')
circleearleft = pl.Ellipse((0.61, 0.7), 0.12, 0.09, color='white')
circleearinleft = pl.Ellipse((0.63, 0.7), 0.09, 0.07, color='pink')
circleearright = pl.Ellipse((0.61, 0.3), 0.12, 0.09, color='white')
circleearinright = pl.Ellipse((0.63, 0.3), 0.09, 0.07, color='pink')
circleeyeleft = plt.Circle((0.8, 0.6), 0.04, color='lightblue')
circleeyepupilleft = plt.Circle((0.81, 0.6), 0.03, color='black')
circleeyeright = plt.Circle((0.8, 0.4), 0.04, color='lightblue')
circleeyepupilright = plt.Circle((0.81, 0.4), 0.03, color='black')
circlenose = plt.Circle((0.87, 0.5), 0.05, color='pink')
circletail = plt.Circle((0.09, 0.5), 0.05, color='orange')
circlereflectionright = pl.Ellipse((0.8, 0.61), 0.01, 0.01, color='white')
circlereflectionleft = pl.Ellipse((0.8, 0.41), 0.01, 0.01, color='white')

#axes.set_aspect(1)
plt.gca().add_patch(circlenose)
plt.gca().add_patch(circlebody)
plt.gca().add_patch(circleearleft)
plt.gca().add_patch(circleearright)
plt.gca().add_patch(circleeyeleft)
plt.gca().add_patch(circleeyeright)
plt.gca().add_patch(circleeyepupilleft)
plt.gca().add_patch(circleeyepupilright)
plt.gca().add_patch(circletail)
plt.gca().add_patch(circleearinleft)
plt.gca().add_patch(circleearinright)
plt.gca().add_patch(circlereflectionright)
plt.gca().add_patch(circlereflectionleft)



plt.axis('scaled')

plt.title('Hamster')
plt.show()

#HAMSTER DIRECTION

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.patches as pl
from matplotlib.pyplot import figure, plot, axis, show
from celluloid import Camera

from hamster_direction import Hamster

devil = Hamster()

devil.maze_1()

devil.hamsterRight()
