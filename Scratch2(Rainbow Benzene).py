import turtle
turtle.bgcolor("black")
colors=['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.speed(0)
for i in range(288):
    turtle.pencolor(colors[i%6])
    turtle.pensize(i/80+1)
    turtle.forward(i)
    turtle.left(59)
turtle.done()
