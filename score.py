from turtle import Turtle

class Score:

    def __init__(self, x_pos,y_pos):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color("white")
        self.score.goto(x_pos,y_pos)
        self.score.write("")
        self.current_score = 0
        self.score.write(self.current_score, font=("Arial", 12, ""), align="center")

    def update_score(self):
        self.score.clear()
        self.score.write(self.current_score, font=("Arial", 12, ""), align="center")
