from tkinter import *
from random import randint
t = 0
def f():
    global t

    if eval(l['text'][:-1]) == int(e.get()):
        t += 1
        print(t)
        root['bg'] = 'green'
        c['bg'] = 'green'
        t = randint(0, 2)
        txt = ''
        if t == 0:
            txt = f'{randint(0, 54)}+{randint(0, 14)}='
        elif t == 1:
            x = {randint(0, 44)}
            txt = f'{x}-{randint(0, x)}='
        else:
            txt = f'{randint(0, 10)}*{randint(0, 7)}='
        l['text'] = txt
    else:
        root['bg'] = 'red'
        c['bg'] = 'red'


root = Tk()
root.geometry('1600x900')
root['bg'] = '#f58205'
c = Canvas(height=80, bg=root['bg'], width=1650)
c.pack()
l = Label()
l.pack()
l['text'] = '1+1='
l['bg'] = '#f58205'
e = Entry(bg='black', fg='white')
e.pack()
Button(text='дальше', command=f).pack()


root.mainloop()
