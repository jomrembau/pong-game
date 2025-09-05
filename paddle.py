from turtle import Turtle

class Paddle:

    def __init__(self, x_pos,y_pos):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.showturtle()
        self.paddle.goto(x_pos,y_pos)
        self.paddle.shapesize(0.3)
        self.paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.paddle.setheading(90)

    def move_up(self):
        self.paddle.forward(20)

    def move_down(self):
        self.paddle.back(20)
