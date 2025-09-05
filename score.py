from turtle import Turtle

class Score:

    def __init__(self, x_pos,y_pos, current_score):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color("white")
        self.score.goto(x_pos,y_pos)
        self.score.write("")
        self.current_score = current_score
        self.score.write(current_score, font=("Arial", 12, ""), align="center")
