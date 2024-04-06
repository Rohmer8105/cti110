import turtle
t = turtle.Turtle()

side_length = 100
angle = 90
sides = 4

t.penup()
t.goto(-50, 50)
t.pendown()

count = 0
while count < sides:
    t.forward(side_length)
    t.right(angle)
    count += 1

t.penup()
t.goto(100, 100)
t.pendown()

side_length = 100
angle = 120
sides = 3

count = 0
while count < sides:
    t.forward(side_length)
    t.left(angle)
    count += 1

turtle.done()
