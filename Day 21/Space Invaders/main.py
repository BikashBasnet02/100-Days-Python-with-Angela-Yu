import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Dodge the Ball")
screen.tracer(0)


player = turtle.Turtle()
player.color("white")
player.shape("turtle")
player.penup()
player.setposition(0, -250)
player_speed = 15

ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.penup()
ball.setposition(random.randint(-290, 290), 290)
ball_speed = 5


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

 
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

 
while True:
    screen.update()

    # Move the ball
    y = ball.ycor()
    y -= ball_speed
    ball.sety(y)

    # Check for collision between player and ball
    if player.distance(ball) < 20:
        player.color("red")
        break

    # Reset the ball position if it reaches the bottom
    if ball.ycor() < -290:
        ball.setposition(random.randint(-290, 290), 290)

# Game over message
game_over = turtle.Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.write("Game Over", align="center", font=("Arial", 24, "normal"))

# Keep the window open
turtle.done()
