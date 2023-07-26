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
    def __init__(self, m, x, y, vx, vy, clr='red'):
        self.m, self.x, self.y, self.vx, self.vy, self.clr = m, x, y, vx, vy, clr
        self.img = cnvs.create_oval(x-R, y-R, x+R, y+R)
    def date(self):
        return {'m': self.m, 'x': self.x, 'y': self.y, 'vx': self.vx, 'vy': self.vy, 'clr': self.clr}

    def move(self, cnvs):
        cnvs.move(self.img, self.vx*dt, self.vy*dt)


##############################################################
#########################---input---##########################
##############################################################
Matters = [
    Matter(1, 208, 200, 0, 4, 'green'),
    Matter(10000, 200, 200, 0, 0)
]


##############################################################
#########################---start---##########################
##############################################################
while True:

    time.sleep(dt)
    root.update()
