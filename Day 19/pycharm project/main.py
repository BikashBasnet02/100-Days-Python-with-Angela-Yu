import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

for _ in range(100):
    for turtle in turtles:
        turtle.forward(random.randint(1, 5))
        time.sleep(0)

winner = random.choice(turtles)

while winner.xcor() < screen.window_width():
    winner.forward(5)
    time.sleep(0.1)

screen.exitonclick()
