from turtle import Screen
from ball import Ball
from score import Score
from paddle import Paddle
import time

game_on = True
win = Screen()
ball = Ball()
player1_score = Score(-150,150)
player2_score = Score(150,150)
paddle1 = Paddle(-250,0)
paddle2 = Paddle(250,0)

win.title("Pong Game")
win.bgcolor("black")
win.setup(600,400)
win.tracer(0)

win.listen()
win.onkey(paddle2.move_up, "Up")
win.onkey(paddle2.move_down, "Down")
win.onkey(paddle1.move_up, "w")
win.onkey(paddle1.move_down, "s")

while game_on:
    ball.move_ball()
    time.sleep(0.1)
    win.update()

    if (paddle1.paddle.xcor() -10 < ball.ball.xcor() < paddle1.paddle.xcor() +10 and
        paddle1.paddle.ycor() -50 < ball.ball.ycor() < paddle1.paddle.ycor()+50):
        ball_x = ball.ball.xcor()
        heading = ball.ball.heading()
        ball.ball.setheading(180 - heading)

    if (paddle2.paddle.xcor() - 10 < ball.ball.xcor() < paddle2.paddle.xcor() + 10 and
        paddle2.paddle.ycor() - 50 < ball.ball.ycor() < paddle2.paddle.ycor() + 50):
        ball_x = ball.ball.xcor()
        heading = ball.ball.heading()
        ball.ball.setheading(180 - heading)

    if ball.ball.xcor() >= 300:
        ball.reset_ball()
        player1_score.current_score += 1
        player1_score.update_score()


    if ball.ball.xcor() <= -300:
        ball.reset_ball()
        player2_score.current_score += 1
        player2_score.update_score()

    if player1_score.current_score == 11 or player2_score.current_score == 11:
        game_on = False
        ball.game_over()


win.exitonclick()

