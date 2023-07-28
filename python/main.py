from tkinter import *
import time
from settings import *


##############################################################
#########################---Tk---#############################
##############################################################
root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}+200+50')
root.title('stars&planets')
cnvs = Canvas(root, width=WIDTH, height=HEIGHT)
cnvs.pack()

##############################################################
#########################---class---##########################
##############################################################
class Matter:
    def __init__(self, m, x, y, vx, vy, clr='orange'):
        self.m, self.x, self.y, self.vx, self.vy, self.clr = m, x, y, vx, vy, clr
        self.img = cnvs.create_oval(x-R, y-R, x+R, y+R, fill=clr)
    def date(self):
        return {'m': self.m, 'x': self.x, 'y': self.y, 'vx': self.vx, 'vy': self.vy, 'clr': self.clr}

    def move(self, cnvs):
        self.x += self.vx*dt
        self.y += self.vy*dt
        cnvs.move(self.img, self.vx*dt, self.vy*dt)

    def upd(self, vx, vy):
        self.vx += vx
        self.vy += vy


##############################################################
#########################---input---##########################
##############################################################
Matters = [
    Matter(1, 280, 200, 0, 4, 'green'),
    Matter(10000, 200, 200, 0, 0),
    Matter(1, 300, 300, 0, -5, 'red'),
    Matter(1, 200, 240, 5, 0, 'blue')
]


##############################################################
#########################---start---##########################
##############################################################
while True:
    for i in range(len(Matters)):
        for j in range(i):
            a = Matters[i].date()
            b = Matters[j].date()
            sx = a['x'] - b['x']
            sy = a['y'] - b['y']
            s = (sx*sx+sy*sy)**0.5
            F = G * a['m'] * b['m'] / (s * s)
            Fx = sx * F / s
            Fy = sy * F / s
            Matters[i].upd(-Fx * dt / a['m'], -Fy * dt / a['m'])
            Matters[j].upd(Fx * dt / b['m'], Fy * dt / b['m'])
        Matters[i].move(cnvs)

    time.sleep(dt)
    root.update()
