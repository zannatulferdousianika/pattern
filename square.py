import turtle 
turtle.Screen().bgcolor('cyan')
turtle.setup(800,500)

p = turtle.Turtle()
p.color('white')
p.pensize(4)
p.shape('turtle')


n = 4

for i in range(n):
    p.forward(50)
    p.right(360/n)

turtle.done()