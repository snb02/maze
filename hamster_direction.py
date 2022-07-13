import matplotlib.pyplot as plt
import matplotlib.patches as pl

import maze


class Hamster:

    def __init__(self):
        self.fig = plt.figure()
        self.axes = plt.axes(xlim=(-1, 20), ylim=(-2, 11))
        self.px = 0
        self.py = 0

    def maze_1(self):
        # I thought of introducing at least 3 mazes
        # and for that I got a random maze generator,
        # and then I converted ("manually") the mazes into polygons

        n = 0
        for repetition in range(0, 11):
            step = 0
            for i in maze.rows[repetition]:
                if i == 0:
                    box = plt.Rectangle((0 + step, 9 + n), 1, 1, color='black')
                    self.axes.add_artist(box)
                    plt.draw()
                    plt.pause(0.2)
                    step += 1
                elif i == 1:
                    box = plt.Rectangle((0 + step, 9 + n), 1, 1, color='red')
                    self.axes.add_artist(box)
                    plt.draw()
                    plt.pause(0.2)
                    step += 1
                elif i == 2:
                    box = plt.Rectangle((0 + step, 9 + n), 1, 1, color='white')
                    self.axes.add_artist(box)
                    plt.draw()
                    plt.pause(0.2)
                    step += 1
                elif i == 3:
                    box = plt.Rectangle((0 + step, 9 + n), 1, 1, color='green')
                    self.axes.add_artist(box)
                    plt.draw()
                    plt.pause(0.2)
                    step += 1
                elif i == 4:
                    box = plt.Rectangle((0 + step, 9 + n), 1, 1, color='blue')
                    self.axes.add_artist(box)
                    plt.draw()
                    plt.pause(0.2)
                    step += 1
            n -= 1

    def hamsterRight(self):
        # self.px += 1  # step

        # sensors
        x = 0.5 + self.px
        y = 1.5 + self.py
        x1 = 1.5 + self.px
        y1 = 0.5 + self.py

        left_sensor = plt.Circle((x, y), 0.2, color='red')  # sensor on the left
        s2 = plt.Circle((x1, y1), 0.2, color='green')  # sensor on the front

        # hamster body
        circlebody = pl.Ellipse((0.5 + self.px, 0.5 + self.py), 0.8, 0.6, color='orange')

        # ears
        circleearleft = pl.Ellipse((0.61 + self.px, 0.7 + self.py), 0.12, 0.09, color='white')
        circleearinleft = pl.Ellipse((0.63 + self.px, 0.7 + self.py), 0.09, 0.07, color='pink')
        circleearright = pl.Ellipse((0.61 + self.px, 0.3 + self.py), 0.12, 0.09, color='white')
        circleearinright = pl.Ellipse((0.63 + self.px, 0.3 + self.py), 0.09, 0.07, color='pink')

        # eyes
        circleeyeleft = plt.Circle((0.8 + self.px, 0.6 + self.py), 0.04, color='lightblue')
        circleeyepupilleft = plt.Circle((0.81 + self.px, 0.6 + self.py), 0.03, color='black')
        circleeyeright = plt.Circle((0.8 + self.px, 0.4 + self.py), 0.04, color='lightblue')
        circleeyepupilright = plt.Circle((0.81 + self.px, 0.4 + self.py), 0.03, color='black')
        circlereflectionright = pl.Ellipse((0.8 + self.px, 0.61 + self.py), 0.01, 0.01, color='white')
        circlereflectionleft = pl.Ellipse((0.8 + self.px, 0.41 + self.py), 0.01, 0.01, color='white')

        # nose
        circlenose = plt.Circle((0.87 + self.px, 0.5 + self.py), 0.05, color='pink')

        # tail
        circletail = plt.Circle((0.09 + self.px, 0.5 + self.py), 0.05, color='orange')

        # def CollisionMazeSensor(#mazetiles, x, y):

        # hamster added to graph
        self.axes.set_aspect(1)
        self.axes.add_artist(circlenose)
        self.axes.add_artist(circlebody)
        self.axes.add_artist(circleearleft)
        self.axes.add_artist(circleearright)
        self.axes.add_artist(circleeyeleft)
        self.axes.add_artist(circleeyeright)
        self.axes.add_artist(circleeyepupilleft)
        self.axes.add_artist(circleeyepupilright)
        self.axes.add_artist(circletail)
        self.axes.add_artist(circleearinleft)
        self.axes.add_artist(circleearinright)
        self.axes.add_artist(circlereflectionright)
        self.axes.add_artist(circlereflectionleft)
        self.axes.add_artist(left_sensor)
        self.axes.add_artist(s2)

        plt.draw()
        plt.pause(10)

        circlebody.remove()
        circleearleft.remove()
        circleearinleft.remove()
        circleearright.remove()
        circleearinright.remove()
        circleeyeleft.remove()
        circleeyepupilleft.remove()
        circleeyeright.remove()
        circleeyepupilright.remove()
        circlenose.remove()
        circletail.remove()
        circlereflectionright.remove()
        circlereflectionleft.remove()
        left_sensor.remove()
        s2.remove()

    def hamsterUp(self):
        # self.py += 1  # step

        # sensors
        x = -0.5 + self.px
        y = 0.5 + self.py
        x1 = 0.5 + self.px
        y1 = 1.5 + self.py

        left_sensor = plt.Circle((x, y), 0.2, color='red')  # sensor on the left
        s2 = plt.Circle((x1, y1), 0.2, color='green')  # sensor on the front

        a = 90
        # hamster body
        circlebody = pl.Ellipse((0.5 + self.px, 0.5 + self.py), 0.8, 0.6, a, color='orange')

        # ears
        circleearleft = pl.Ellipse((0.7 + self.px, 0.61 + self.py), 0.12, 0.09, a, color='white')
        circleearinleft = pl.Ellipse((0.7 + self.px, 0.63 + self.py), 0.09, 0.07, a, color='pink')
        circleearright = pl.Ellipse((0.3 + self.px, 0.61 + self.py), 0.12, 0.09, a, color='white')
        circleearinright = pl.Ellipse((0.3 + self.px, 0.61 + self.py), 0.09, 0.07, a, color='pink')

        # eyes
        circleeyeleft = plt.Circle((0.6 + self.px, 0.8 + self.py), 0.04, color='lightblue')
        circleeyepupilleft = plt.Circle((0.6 + self.px, 0.81 + self.py), 0.03, color='black')
        circleeyeright = plt.Circle((0.4 + self.px, 0.8 + self.py), 0.04, color='lightblue')
        circleeyepupilright = plt.Circle((0.4 + self.px, 0.81 + self.py), 0.03, color='black')
        circlereflectionright = pl.Ellipse((0.61 + self.px, 0.8 + self.py), 0.01, 0.01, a, color='white')
        circlereflectionleft = pl.Ellipse((0.41 + self.px, 0.8 + self.py), 0.01, 0.01, a, color='white')

        # nose
        circlenose = plt.Circle((0.5 + self.px, 0.87 + self.py), 0.05, color='pink')

        # tail
        circletail = plt.Circle((0.5 + self.px, 0.09 + self.py), 0.05, color='orange')

        # def CollisionMazeSensor(#mazetiles, x, y):

        # hamster added to graph
        self.axes.set_aspect(1)
        self.axes.add_artist(circlenose)
        self.axes.add_artist(circlebody)
        self.axes.add_artist(circleearleft)
        self.axes.add_artist(circleearright)
        self.axes.add_artist(circleeyeleft)
        self.axes.add_artist(circleeyeright)
        self.axes.add_artist(circleeyepupilleft)
        self.axes.add_artist(circleeyepupilright)
        self.axes.add_artist(circletail)
        self.axes.add_artist(circleearinleft)
        self.axes.add_artist(circleearinright)
        self.axes.add_artist(circlereflectionright)
        self.axes.add_artist(circlereflectionleft)
        self.axes.add_artist(left_sensor)
        self.axes.add_artist(s2)

        plt.draw()
        plt.pause(10)

        circlebody.remove()
        circleearleft.remove()
        circleearinleft.remove()
        circleearright.remove()
        circleearinright.remove()
        circleeyeleft.remove()
        circleeyepupilleft.remove()
        circleeyeright.remove()
        circleeyepupilright.remove()
        circlenose.remove()
        circletail.remove()
        circlereflectionright.remove()
        circlereflectionleft.remove()
        left_sensor.remove()
        s2.remove()

    def hamsterDown(self):
        # self.py -= 1  # step

        # sensors
        x = 1.5 + self.px
        y = 0.5 + self.py
        x1 = 0.5 + self.px
        y1 = -0.5 + self.py

        s1 = plt.Circle((x, y), 0.2, color='red')  # sensor on the left
        s2 = plt.Circle((x1, y1), 0.2, color='green')  # sensor on the front

        a = 90
        # hamster body
        circlebody = pl.Ellipse((0.5 + self.px, 0.5 + self.py), 0.8, 0.6, a, color='orange')

        # ears
        circleearleft = pl.Ellipse((0.7 + self.px, 1 - 0.61 + self.py), 0.12, 0.09, a, color='white')
        circleearinleft = pl.Ellipse((0.7 + self.px, 1 - 0.63 + self.py), 0.09, 0.07, a, color='pink')
        circleearright = pl.Ellipse((0.3 + self.px, 1 - 0.61 + self.py), 0.12, 0.09, a, color='white')
        circleearinright = pl.Ellipse((0.3 + self.px, 1 - 0.61 + self.py), 0.09, 0.07, a, color='pink')

        # eyes
        circleeyeleft = plt.Circle((0.6 + self.px, 1 - 0.8 + self.py), 0.04, color='lightblue')
        circleeyepupilleft = plt.Circle((0.6 + self.px, 1 - 0.81 + self.py), 0.03, color='black')
        circleeyeright = plt.Circle((0.4 + self.px, 1 - 0.8 + self.py), 0.04, color='lightblue')
        circleeyepupilright = plt.Circle((0.4 + self.px, 1 - 0.81 + self.py), 0.03, color='black')
        circlereflectionright = pl.Ellipse((0.61 + self.px, 1 - 0.8 + self.py), 0.01, 0.01, a, color='white')
        circlereflectionleft = pl.Ellipse((0.41 + self.px, 1 - 0.8 + self.py), 0.01, 0.01, a, color='white')

        # nose
        circlenose = plt.Circle((0.5 + self.px, 1 - 0.87 + self.py), 0.05, color='pink')

        # tail
        circletail = plt.Circle((0.5 + self.px, 1 - 0.09 + self.py), 0.05, color='orange')

        # def CollisionMazeSensor(#mazetiles, x, y):

        # hamster added to graph
        self.axes.set_aspect(1)
        self.axes.add_artist(circlenose)
        self.axes.add_artist(circlebody)
        self.axes.add_artist(circleearleft)
        self.axes.add_artist(circleearright)
        self.axes.add_artist(circleeyeleft)
        self.axes.add_artist(circleeyeright)
        self.axes.add_artist(circleeyepupilleft)
        self.axes.add_artist(circleeyepupilright)
        self.axes.add_artist(circletail)
        self.axes.add_artist(circleearinleft)
        self.axes.add_artist(circleearinright)
        self.axes.add_artist(circlereflectionright)
        self.axes.add_artist(circlereflectionleft)
        self.axes.add_artist(s1)
        self.axes.add_artist(s2)

        plt.draw()
        plt.pause(10)

        circlebody.remove()
        circleearleft.remove()
        circleearinleft.remove()
        circleearright.remove()
        circleearinright.remove()
        circleeyeleft.remove()
        circleeyepupilleft.remove()
        circleeyeright.remove()
        circleeyepupilright.remove()
        circlenose.remove()
        circletail.remove()
        circlereflectionright.remove()
        circlereflectionleft.remove()
        s1.remove()
        s2.remove()

    def hamsterLeft(self):
        # self.px -= 1  # step

        # sensors
        x = 0.5 + self.px
        y = -0.5 + self.py
        x1 = -0.5 + self.px
        y1 = 0.5 + self.py

        s1 = plt.Circle((x, y), 0.2, color='red')  # sensor on the left
        s2 = plt.Circle((x1, y1), 0.2, color='green')  # sensor on the front

        # hamster body
        circlebody = pl.Ellipse((0.5 + self.px, 0.5 + self.py), 0.8, 0.6, color='orange')

        # ears
        circleearleft = pl.Ellipse((1 - 0.61 + self.px, 0.7 + self.py), 0.12, 0.09, color='white')
        circleearinleft = pl.Ellipse((1 - 0.63 + self.px, 0.7 + self.py), 0.09, 0.07, color='pink')
        circleearright = pl.Ellipse((1 - 0.61 + self.px, 0.3 + self.py), 0.12, 0.09, color='white')
        circleearinright = pl.Ellipse((1 - 0.63 + self.px, 0.3 + self.py), 0.09, 0.07, color='pink')

        # eyes
        circleeyeleft = plt.Circle((1 - 0.8 + self.px, 0.6 + self.py), 0.04, color='lightblue')
        circleeyepupilleft = plt.Circle((1 - 0.81 + self.px, 0.6 + self.py), 0.03, color='black')
        circleeyeright = plt.Circle((1 - 0.8 + self.px, 0.4 + self.py), 0.04, color='lightblue')
        circleeyepupilright = plt.Circle((1 - 0.81 + self.px, 0.4 + self.py), 0.03, color='black')
        circlereflectionright = pl.Ellipse((1 - 0.8 + self.px, 0.61 + self.py), 0.01, 0.01, color='white')
        circlereflectionleft = pl.Ellipse((1 - 0.8 + self.px, 0.41 + self.py), 0.01, 0.01, color='white')

        # nose
        circlenose = plt.Circle((1 - 0.87 + self.px, 0.5 + self.py), 0.05, color='pink')

        # tail
        circletail = plt.Circle((1 - 0.09 + self.px, 0.5 + self.py), 0.05, color='orange')

        # def CollisionMazeSensor(#mazetiles, x, y):

        # hamster added to graph
        self.axes.set_aspect(1)
        self.axes.add_artist(circlenose)
        self.axes.add_artist(circlebody)
        self.axes.add_artist(circleearleft)
        self.axes.add_artist(circleearright)
        self.axes.add_artist(circleeyeleft)
        self.axes.add_artist(circleeyeright)
        self.axes.add_artist(circleeyepupilleft)
        self.axes.add_artist(circleeyepupilright)
        self.axes.add_artist(circletail)
        self.axes.add_artist(circleearinleft)
        self.axes.add_artist(circleearinright)
        self.axes.add_artist(circlereflectionright)
        self.axes.add_artist(circlereflectionleft)
        self.axes.add_artist(s1)
        self.axes.add_artist(s2)

        plt.draw()
        plt.pause(10)

        circlebody.remove()
        circleearleft.remove()
        circleearinleft.remove()
        circleearright.remove()
        circleearinright.remove()
        circleeyeleft.remove()
        circleeyepupilleft.remove()
        circleeyeright.remove()
        circleeyepupilright.remove()
        circlenose.remove()
        circletail.remove()
        circlereflectionright.remove()
        circlereflectionleft.remove()
        s1.remove()
        s2.remove()
