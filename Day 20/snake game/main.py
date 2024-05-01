from turtle import Screen, Turtle
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0.5)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)
    segment.penup()
    segments.append(segment)

food = Turtle("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

score = 0
score_display = Turtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 16, "normal"))

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

head = segments[0]

def move():
    if head.heading() != DOWN:
        head.setheading(UP)

def move_down():
    if head.heading() != UP:
        head.setheading(DOWN)

def move_left():
    if head.heading() != RIGHT:
        head.setheading(LEFT)

def move_right():
    if head.heading() != LEFT:
        head.setheading(RIGHT)

screen.listen()
screen.onkey(move, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

def check_collision_with_wall():
    x = head.xcor()
    y = head.ycor()
    if x > 290:
        head.goto(-290, y)
    elif x < -290:
        head.goto(290, y)
    elif y > 290:
        head.goto(x, -290)
    elif y < -290:
        head.goto(x, 290)

def move_snake():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20) 

def grow_snake():
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    segments.append(new_segment)

def check_collision_with_food():
    global score
    if segments[0].distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        grow_snake()
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 16, "normal"))


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    check_collision_with_wall()
    check_collision_with_food()
    move_snake()


screen.exitonclick()
