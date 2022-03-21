"""This is practice for the tutrle assignment."""

from turtle import Turtle, done
leo: Turtle = Turtle()
i: int = 0
while i < 3:
    leo.forward(50)
    leo.right(120)
    i += 1
leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()

bob: Turtle = Turtle()
bob.color("blue")
