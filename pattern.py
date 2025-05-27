import turtle 
import random
turtle.Screen().bgcolor('black')
turtle.Screen().setup(800,500)

p = turtle.Turtle()
p.color('white')
p.pensize(2)

s = 0
colors=['pink','orange','red','white','purple']

while True:
    p.color(random.choice(colors))
    for _ in range(4):
        p.forward(s+1)
        p.left(90)
        s = s-5
    s +=1



