#Project Title: Pong: Redux
#Name: Daniel Shalimov
#Year: Freshman

import turtle
from gtts import gTTS
import playsound


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

player_a_messages = {
     1: "HAHA I won!",
     2: "Why are you so worried? It's not like we're dead or anything.",
     3: "Come on man lighten up. Who needs doing taxes when we have this?"
}
player_b_messages = {
    1: "Dude why are you so invested into this? I don't even know where the heck we are.",
    2: "What is that red thing? And why do you not have a single care in the world?",
    3: "So are you not gonna question that weird turtle thing or am I delusional?"
}


play_until = 5
total_rounds = 3
say = ""
wn = turtle.Screen()
wn.title("Pong:Redux")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Round
round = 1

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Obstacle
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.shapesize(stretch_wid=5, stretch_len=1)
obstacle.penup()
obstacle.goto(0, 0)
obstacle.hideturtle()
obstacle.dy = 5
obstacle.color("red")

#Obstacle 2
obstacle2 = turtle.Turtle()
obstacle2.speed(0)
obstacle2.penup()
obstacle2.goto(0, 0)
obstacle2.shape("turtle")
obstacle2.hideturtle()
obstacle2.dx = -5
obstacle2.dy = -5
obstacle2.color("green")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Comic Sans", 25, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboeard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Loop
while round <= total_rounds: #score_a < play_until and score_b < play_until:
    wn.update()

    #Move the obstacles
    obstacle.sety(obstacle.ycor() + obstacle.dy)
    obstacle2.setx(obstacle2.xcor() - obstacle2.dx)
    obstacle2.sety(obstacle2.ycor() - obstacle2.dy)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if obstacle.ycor() > 290:
        obstacle.sety(290)
        obstacle.dy *= -1

    if obstacle.ycor() < -290:
        obstacle.sety(-290)
        obstacle.dy *= -1

    if obstacle2.ycor() > 290:
        obstacle2.sety(290)
        obstacle2.dy *= -1

    if obstacle2.ycor() < -290:
        obstacle2.sety(-290)
        obstacle2.dy *= -1

    if obstacle2.xcor() > 390:
        obstacle2.setx(390)
        obstacle2.dx *= -1

    if obstacle2.xcor() < -390:
        obstacle2.setx(-390)
        obstacle2.dx *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Round{}: Player 1: {}  Player 2: {}".format(round, score_a, score_b), align="center",
                  font=("Comic Sans", 25, "normal"))
        if score_a == play_until:
            pen.goto(0, 0)
            say = player_a_messages[round]
            speak(say)
            pen.write(f"Player 1: {say}", align="center", font=("Comic Sans", 15, "normal"))
            pen.goto(0, 260)
            round += 1
            score_a = 0
            score_b = 0
            obstacle.showturtle()
            if round > 2:
                obstacle2.showturtle()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Round {}: Player 1: {}  Player 2: {}".format(round, score_a, score_b), align="center",
                  font=("Comic Sans", 25, "normal"))
        if score_b == play_until:
            pen.goto(0, 0)
            say = player_b_messages[round]
            speak(say)
            pen.write(f"Player 2: {say}",
                      align="center", font=("Comic Sans", 15, "normal"))
            pen.goto(0, 260)
            round += 1
            score_a = 0
            score_b = 0
            obstacle.showturtle()
            if round > 2:
                obstacle2.showturtle()
    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #Obstacle and ball collision
    if obstacle.isvisible() and ball.xcor() == 0 and (obstacle.ycor() + 40 > ball.ycor() > obstacle.ycor() -40):
        ball.dx *= -1

    if obstacle2.isvisible() and ball.xcor() == obstacle2.xcor() and obstacle2.ycor() == ball.ycor():
        ball.dx *= -1
        obstacle2.dx *= -1
        ball.dy *= -1
        obstacle2.dy *= -1

    if obstacle2.isvisible() and obstacle2.xcor() == 0 and (obstacle.ycor() + 40 > obstacle2.ycor() > obstacle.ycor() -40):
        obstacle2.dx *= -1
        obstacle2.dy *= -1


turtle.exitonclick()
