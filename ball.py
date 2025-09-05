from turtle import Turtle

class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.color("blue")
        self.ball.shape("circle")
        self.ball.shapesize(0.5)
        self.ball.penup()
        self.ball.goto(0,0)
        self.initial_angle = 45
        self.ball.left(self.initial_angle)

    def move_ball(self):

        ball_y = self.ball.ycor()

        if abs(ball_y) >= 190:
            heading = self.ball.heading()
            self.ball.setheading( - heading)
        self.ball.fd(15)


