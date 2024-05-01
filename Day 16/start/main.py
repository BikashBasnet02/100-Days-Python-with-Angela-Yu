import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing Program")
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Define functions for drawing shapes
def draw_circle():
    pen.circle(50)

def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.left(120)

# Function to handle pen movements
def pen_up():
    pen.penup()

def pen_down():
    pen.pendown()

# Function to clear the drawing
def clear_drawing():
    pen.clear()

# Function to exit the program
def exit_program():
    screen.bye()

# Bind functions to keyboard keys
screen.listen()
screen.onkey(draw_circle, "c")
screen.onkey(draw_square, "s")
screen.onkey(draw_triangle, "t")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(clear_drawing, "x")
screen.onkey(exit_program, "q")

# Main loop to keep the window open
screen.mainloop()
