import turtle 
turtle.Screen().bgcolor('cyan')
turtle.Screen().setup(800,500)

p = turtle.Turtle()
p.color('white')
p.pensize(5)
p.shape('turtle')


n = 8

for i in range(n):
    p.forward(50)
    p.right(360/n)

turtle.done()