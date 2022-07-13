import matplotlib.pyplot as plt
import matplotlib.patches as pl

figure, axes = plt.subplots()

circlebody = pl.Ellipse((0.5, 0.5), 0.8, 0.6, color='orange')
circleearleft = pl.Ellipse((0.61, 0.7), 0.12, 0.09, color='white')
circleearinleft = pl.Ellipse((0.63, 0.7), 0.09, 0.07, color='pink')
circleearright = pl.Ellipse((0.61, 0.3), 0.12,0.09, color='white')
circleearinright = pl.Ellipse((0.63, 0.3), 0.09, 0.07, color='pink')
circleeyeleft = plt.Circle((0.8, 0.6), 0.04, color='lightblue')
circleeyepupilleft = plt.Circle((0.81, 0.6), 0.03, color='black')
circleeyeright = plt.Circle((0.8, 0.4), 0.04, color='lightblue')
circleeyepupilright = plt.Circle((0.81, 0.4), 0.03, color='black')
circlenose = plt.Circle((0.87, 0.5), 0.05, color='pink')
circletail = plt.Circle((0.09, 0.5), 0.05, color='orange')
circlereflectionright = pl.Ellipse((0.8, 0.61), 0.01, 0.01, color='white')
circlereflectionleft = pl.Ellipse((0.8, 0.41), 0.01, 0.01, color='white')

axes.set_aspect(1)
axes.add_artist(circlenose)
axes.add_artist(circlebody)
axes.add_artist(circleearleft)
axes.add_artist(circleearright)
axes.add_artist(circleeyeleft)
axes.add_artist(circleeyeright)
axes.add_artist(circleeyepupilleft)
axes.add_artist(circleeyepupilright)
axes.add_artist(circletail)
axes.add_artist(circleearinleft)
axes.add_artist(circleearinright)
axes.add_artist(circlereflectionright)
axes.add_artist(circlereflectionleft)




plt.title('Hamster')
plt.show()