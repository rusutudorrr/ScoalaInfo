import turtle

t = turtle.Pen()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(180):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(90)