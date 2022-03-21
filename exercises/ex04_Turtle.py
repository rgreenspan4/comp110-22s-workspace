"""This program makes a picture of unconcievable beauty."""

__author__ = 730530918
import turtle as tt
from turtle import Turtle, colormode, done
from random import randint
colormode(255)
GRAPH_WIDTH: float = tt.window_width()
SQUARE_TURN: int = 90
TRIANGLE_TURN: int = 120
CIRCLE_SIZE: int = 50
STARS_IN_SKY: int = 30
STAR_SIZE: int = 3
HORIZON_LINE: int = 0
MAX_SPEED: int = 50


def main() -> None:
    """This calls the entire program!"""
    bob: Turtle = Turtle()
    bob.speed(MAX_SPEED)
    sky(bob, (-GRAPH_WIDTH / 2), HORIZON_LINE)
    stars(bob)
    mountain(bob, (-GRAPH_WIDTH / 3.5), HORIZON_LINE - 5)
    mountain(bob, (GRAPH_WIDTH / 2.5), HORIZON_LINE - 5)
    moon(bob, GRAPH_WIDTH / 4, GRAPH_WIDTH / 4)
    horizon(bob, (-GRAPH_WIDTH / 2), HORIZON_LINE)
    done()


def horizon(bob: Turtle, a: float, b: float) -> None:
    """Doc string for making horizon line."""
    i: int = 0
    x: int = 0
    bob.penup()
    while i < GRAPH_WIDTH / 2 or x < 255:
        y: int = 0
        bob.goto(a, b - x)
        bob.pendown()
        bob.fillcolor(255 - x, 255 - x, 255 - x)
        bob.pencolor((255 - x, 255 - x, 255 - x))
        bob.begin_fill()
        while y < 4:
            bob.forward(GRAPH_WIDTH)
            bob.right(SQUARE_TURN)
            y += 1
        bob.end_fill()
        x += 10
        i += 1


def sky(bob: Turtle, a: float, b: float) -> None:
    """Makes the night sky."""
    i: int = 0
    bob.goto(a, b)
    bob.fillcolor("black")
    bob.pencolor("black")
    bob.begin_fill()
    while i < 4:
        bob.forward(GRAPH_WIDTH)
        bob.left(SQUARE_TURN)
        i += 1
    bob.end_fill()


def mountain(bob: Turtle, a: float, b: float) -> None:
    """This code makes the mountaints."""
    i: int = 0
    bob.goto(a, b)
    bob.fillcolor("grey")
    bob.pencolor("grey")
    bob.begin_fill()
    while i < 3:
        bob.backward(GRAPH_WIDTH / 4)
        bob.right(TRIANGLE_TURN)
        i += 1
    bob.end_fill()


def moon(bob: Turtle, a: float, b: float) -> None:
    """This code makes the moon."""
    i: int = 0
    x: int = 0
    bob.penup()
    while i < 5:
        bob.goto(a, b + x)
        bob.pendown()
        bob.fillcolor(255 - x, 255 - x, 255 - x)
        bob.pencolor((255 - x, 255 - x, 255 - x))
        bob.begin_fill()
        bob.circle(CIRCLE_SIZE - x)
        bob.end_fill()
        x += 5
        i += 1


def stars(bob: Turtle) -> None:
    """This code makes the stars in the sky."""
    i: int = 0
    x: int = 0
    while i < STARS_IN_SKY:
        x = 0
        bob.penup()
        bob.goto(randint((int(-GRAPH_WIDTH / 2)), int((GRAPH_WIDTH / 2))), randint(HORIZON_LINE, int(GRAPH_WIDTH / 2)))
        bob.pendown()
        bob.fillcolor("white")
        bob.pencolor("white")
        bob.begin_fill()
        while x < 4:
            bob.forward(STAR_SIZE)
            bob.left(SQUARE_TURN)
            x += 1
        i += 1
        bob.end_fill()
        bob.penup()


if __name__ == "__main__":
    main()