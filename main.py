from numpy import *
from matplotlib import pyplot as plt
import matplotlib.animation as an

fig = plt.figure()
board = plt.axes(xlim=(0, 130), ylim=(0, 100))

x1 = 20  # Mittelpunkt des ersten Kreises
y1 = 20
r1 = 25  # Radius

x2 = 100  # Mittelpunkt des zweiten Kreises
y2 = 100
r2 = 20  # Radiuss

a = 'b'

for i in range(50):

    circle1 = plt.Circle((x1, y1), r1, color=a, fill=False)  # konstruiert ersten Kreis

    cp1 = c_[0, x1, y1]  # Werte der Kreise für Kollisionserkennung
    cp2 = c_[0, x2, y2]


    def ZweiKugelKollision(cp1, cp2, r1, r2):  # Kollision zweier Kugeln
        a1 = linalg.norm(cp2 - cp1)  # Abstand zwischen den Mittelpunkten
        if (a1 < r1 + r2):  # Wenn der Abstand kleiner als die addierten Radien findet eine Kollission statt
            return True
        return False  # keine Kollision


    Kollision = ZweiKugelKollision(cp1, cp2, r1, r2)

    if (Kollision == True):  # wenn die Kugeln Kollidieren, soll der erste Kreis seine Farbe zu Rot ändern
        a = 'r'
    if (Kollision == False):  # ist keine Kollision zu erkennen, soll die Farbe blau bleiben
        a = 'b'

    circle1 = plt.Circle((x1, y1), r1, color=a, fill=False)  # erster Kreis
    board.add_patch(circle1)  # Füge Kreis hinzu

    x1 += 5
    y1 += 5

    circle2 = plt.Circle((x2, y2), r2, color='r', fill=False)  # zweiter Kreis wird konstruiert
    board.add_patch(circle2)  # zweiter Kreis wird hinzugefügt

    plt.draw()  # Kreise werden gezeichnet
    plt.pause(0.2)

    circle1.remove()  # entfernt Kreis, um es später zu ersetzen
    circle2.remove()

    x2 -= 5  # ändert die position des zweiten Kreises (diagonal nach unten links)
    y2 -= 5

plt.show()
