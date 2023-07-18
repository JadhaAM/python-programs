import turtle
import time
def draw_square(t):
    for i in range(1,5):
        t.forward(150)
        t.right(90)

def draw_art():
    turtle.bgcolor("black")
    turtle.pencolor("yellow")
    turtle.pensize(4)
    turtle.speed(0)
    for i in range(1,37):
        draw_square(turtle)
        turtle.right(10)

draw_art()
time.sleep(10)