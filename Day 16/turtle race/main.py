import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.setup(width=800, height=600)

# List of colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Number of turtles in the race
num_turtles = 6

# Create turtles for the race
turtles = []
for i in range(num_turtles):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-380, 250 - i * 100)
    turtles.append(new_turtle)

# Function to move turtles forward
def move_turtles():
    for turtle in turtles:
        distance = random.randint(1, 20)
        turtle.forward(distance)

# Function to check for winner
def check_winner():
    winner = None
    for turtle in turtles:
        if turtle.xcor() >= 380:
            winner = turtle.color()
            break
    return winner

# Function to play the game
def play_game():
    while True:
        move_turtles()
        winner = check_winner()
        if winner:
            print(f"The {winner[0]} turtle wins!")
            break

# Start the game
play_game()

# Keep the window open until it's manually closed
screen.mainloop()
