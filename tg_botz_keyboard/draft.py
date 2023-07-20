import turtle
import tkinter as tk
from turtle import RawTurtle, TurtleScreen, pensize
from tkinter import colorchooser


class App:
    def __int__(self):


root = tk.Tk()
root.title("Sierpinsky'""s Triangle.")
root.configure(background="black")
canvas1 = tk.Canvas(root, width=400, height=600, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Sierpinsky Triangle', font=('Lobster', 14), background='black', foreground='white')
label1.pack()

label2 = tk.Label(root, text='Enter Width:', font=('Lobster', 10), background='black', foreground='white')
label2.pack()

Length = tk.Entry(root, background='black', foreground='#FBFBF8')
Length.pack()

label3 = tk.Label(root, text='Enter depth of recusion:', font=('Lobster', 10), background='black', foreground='white')
label3.pack()

Depth = tk.Entry(root, background='black', foreground='white')
Depth.pack()

canvas2 = tk.Canvas(canvas1, width=400, height=300)
canvas2.pack()


def draw_sierpinski():
    length = int(Length.get())
    level = int(Depth.get())
    turtle.speed(0)
    sierpinski(length, level)


def sierpinski(length, level):
    if level == 0:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        sierpinski(length / 2, level - 1)
        turtle.forward(length / 2)
        sierpinski(length / 2, level - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierpinski(length / 2, level - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)


def stop():
    turtle.clear()
    turtle.setposition(0, 0)


def keypress(event):
    global xx, canvas, t, speed
    ev = event.keysym
    if ev == 'Left':
        xx += speed
    else:
        xx -= speed

    canvas.place(x=xx)
    t.setposition((-canvas.winfo_width() / 4) - (xx + 250), 0)
    return None


draw_button = tk.Button(root, text='Draw.', command=draw_sierpinski, background='black', foreground='white')
draw_button.pack()

example_button = tk.Button(root, text='Example(Length).', comman=lambda: Length.insert(0, '100'), background='black',
                           foreground='white')
example_button.pack()
example2_button = tk.Button(root, text='Example(Depth).', comman=lambda: Depth.insert(0, '3'), background='black',
                            foreground='white')
example2_button.pack()

stop_button = tk.Button(root,
                        text="Redraw(Click on it when previous drawing is done, otherwise there will be graphic errors).",
                        command=stop, background='black', foreground='white')
stop_button.pack()
screen = TurtleScreen(canvas2)
screen.bgcolor('#FBFBF8')
turtle = RawTurtle(screen)
root.mainloop()

button.grid(row=,
            column=,
            columnspan=)
