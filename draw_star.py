import turtle 
turtle.Screen().bgcolor('cornflowerblue')
turtle.Screen().setup(800,500)

p = turtle.Turtle()
p.color('white')
p.pensize(5)
p.shape('turtle')


p.penup()
p.goto(0,100)
p.pendown()

for _ in range(5):
    p.forward(100)
    p.right(144)

p.penup()
p.goto(150,100)
p.pendown()

for _ in range(5):
    p.forward(100)
    p.right(144)

p.penup()
p.goto(-150,100)
p.pendown()

for _ in range(5):
    p.forward(100)
    p.right(144)

turtle.done()