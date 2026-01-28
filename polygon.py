import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(400,670)
polygon = turtle.Turtle()
numbr_sides = 6
side_length = 60
angle = 360/ numbr_sides
for i in range(numbr_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()