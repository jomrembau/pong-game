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
        self.ball_speed = 15

    def move_ball(self):

        ball_y = self.ball.ycor()

        if abs(ball_y) >= 190:
            heading = self.ball.heading()
            self.ball.setheading( - heading)
        self.ball.fd(self.ball_speed)


    def reset_ball(self):
        heading = self.ball.heading()
        self.ball.goto(0,0)
        self.ball_speed += 1
        self.ball.fd(self.ball_speed)
        self.ball.setheading(180- heading)

    def game_over(self):
        self.ball.goto(0, 0)
        self.ball.write("G A M E  O V E R", font=("Arial", 12, ""), align="center")
