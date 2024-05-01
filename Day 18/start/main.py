from turtle import Screen, Turtle
import random

def random_colors():
    """
    Generate random RGB colors.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

the_turtle = Turtle()
the_turtle.pensize(5)
the_turtle.speed("fastest")

# Define directions in degrees
directions = [0, 90, 180, 270]

for _ in range(200):
    the_turtle.color(random_colors())
    the_turtle.forward(30)
    the_turtle.setheading(random.choice(directions))

screen.exitonclick()
