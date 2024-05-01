from turtle import Screen, Turtle
from freegames import vector

class Ball(Turtle):
    """
    A ball that bounces around the screen.
    """
    def __init__(self):
        """
        Create a new ball with default values for position and velocity.
        """
        super().__init__()
        self.position = vector.Vector2(0, 0)
        self.velocity = vector.Vector2(150, -90)

    def draw(self):
        """
        Draw the ball on the screen.
        """

        self.hideturtle()

        self.color("white")

        self.goto(self.position)

    def bounce(self):
        """
        Change the x and y components of the velocity by negating them. This makes the ball
        bounce in all four directions: up, down, left, and right.
        """
        self.velocity = vector.Vector2(-self.velocity.x, self.velocity.y)

    def move(self):
        """
        Move the ball forward by its velocity. If the ball hits the edge of the screen, change the  
        direction of its velocity accordingly.
        """
        self.position += self.velocity


        if not (0 <= self.position.x <= SCREEN_WIDTH):
            self.bounce()

        self.position.y = max(min(self.position.y, SCREEN_HEIGHT), 0)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

def move():
    ball.move()

    screen.ontimer(move, 1000 // 30)  # 30 frames per second

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Bouncing Ball")

ball = Ball()

ball.draw()


move()

screen.mainloop()
