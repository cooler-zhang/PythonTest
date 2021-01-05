import turtle

turtle.pen()

colors=["red","yellow","blue","green"]

for x in range(1000):
    turtle.pencolor(colors[x%4])
    turtle.forward(x)
    turtle.left(91)