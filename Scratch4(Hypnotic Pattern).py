import turtle
import time
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
distance=0

for i in range(100):
    turtle.forward(distance)
    turtle.left(90)
    turtle.pencolor("yellow")
    distance+= 5
time.sleep(100)