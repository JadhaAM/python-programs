import turtle
def draw_square(t):
    for i in range(1,5):
        t.forward(150)
        t.right(90)

def draw_art():
    turtle.bgcolor("yellow")
    turtle.pencolor("blue")
    turtle.speed(0)
    for i in range(300):
        draw_square(turtle)
        turtle.right(17)

draw_art()
turtle.done()