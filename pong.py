import turtle as trtl

wn = trtl.Screen()
wn.bgcolor("black")

"""
Players 1 and 2 stuff
"""

# Player 1
p1 = trtl.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)

# Player 2
p2 = trtl.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)

"""
Ball
"""
# Ball
ball = trtl.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
# higher the dx and dy is the fast it gets
ball.dx = 5
ball.dy = 5

"""
Moving Functions
"""
# Player 1
def move_up_1():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def move_down_1():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

# Player 2
def move_up_2():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def move_down_2():
    y = p2.ycor()
    y -= 20
    p2.sety(y)

# Keyboard
wn.listen()
wn.onkeypress(move_up_1, "w")
wn.onkeypress(move_down_1, "s")
wn.onkeypress(move_up_2, "Up")
wn.onkeypress(move_down_2, "Down")
"""
Score Writer
"""
# Player 1 Score
score_writer1 = trtl.Turtle()
score_writer1.speed(0)
score_writer1.color("white")
score_writer1.penup()
score_writer1.hideturtle()
score_writer1.goto(-370,270)
score_writer1.pendown()

# Player 2 Score
score_writer2 = trtl.Turtle()
score_writer2.speed(0)
score_writer2.color("white")
score_writer2.penup()
score_writer2.hideturtle()
score_writer2.goto(250,270)
score_writer2.pendown()

p1_score = 0
p2_score = 0
font_setup = ("Arial", "24", "normal")
score_writer1.write(str(p1_score) + " points", font = font_setup)
score_writer2.write(str(p1_score) + " points", font = font_setup)
"""
While True
"""
while True:
    wn.update()

    # Moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and Wall Collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Score
    if ball.xcor() > 350:
        p1_score += 1
        score_writer1.clear()
        score_writer1.write(str(p1_score) + " points", font = font_setup)
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        p2_score += 1
        score_writer2.clear()
        score_writer2.write(str(p1_score) + " points", font = font_setup)
        ball.goto(0, 0)
        ball.dx *= -1

    # Collision for players and ball
    if ball.xcor() < -340 and ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50:
        ball.dx *= -1

wn.mainloop()
