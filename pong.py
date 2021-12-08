import turtle as trtl

# Turtle screen start
wn = trtl.Screen()

"""
Background
"""
# Black backround
wn.bgcolor("black")

# border set up
painter = trtl.Turtle()
painter.speed(0)
painter.color("white")
painter.penup()
painter.goto(-300,-300)
painter.pendown()
painter.pensize(3)

# border
for i in range(4):
    painter.forward(600)
    painter.left(90)
painter.hideturtle()

# No lag (effect)
wn.tracer(0)

"""
Players 1 and 2 stuff
"""
# Player 1
p1 = trtl.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-280, 0)

# Player 2
p2 = trtl.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(280, 0)

"""
Ball
"""
# Ball
ball = trtl.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_x = ball.xcor()
ball.dx = 2
ball.dy = 2

"""
Moving Functions
"""
player_speed = 20

# Player 1
def move_up_1():
    y = p1.ycor()
    y += player_speed
    p1.sety(y)
    # Makes it so it wont go out of bounds
    if y > 250:
        y = 250
    p1.sety(y)

def move_down_1():
    y = p1.ycor()
    y -= player_speed
    p1.sety(y)
    # Makes it so it wont go out of bounds
    if y < -250:
        y = -250
    p1.sety(y)

# Player 2
def move_up_2():
    y = p2.ycor()
    y += player_speed
    p2.sety(y)
    # Makes it so it wont go out of bounds
    if y > 250:
        y = 250
    p2.sety(y)

def move_down_2():
    y = p2.ycor()
    y -= player_speed
    p2.sety(y)
    # Makes it so it wont go out of bounds
    if y < -250:
        y = -250
    p2.sety(y)

# Keyboard
wn.listen()
wn.onkey(move_up_1, "w")
wn.onkey(move_down_1, "s")
wn.onkey(move_up_2, "Up")
wn.onkey(move_down_2, "Down")

"""
Score Variable
"""
# Score
p1_score = 0
p2_score = 0

# Score Writer for player 1
score_writer1 = trtl.Turtle()
score_writer1.speed(0)
score_writer1.color("white")
score_writer1.penup()
score_writer1.hideturtle()
score_writer1.goto(-290, 260)
score_writer1.pendown()
font_setup = ("Arial", "15", "normal")
score_writer1.write(str(p1_score) + " points", font = font_setup)

# Score Writer for player 1
score_writer2 = trtl.Turtle()
score_writer2.speed(0)
score_writer2.color("white")
score_writer2.penup()
score_writer2.hideturtle()
score_writer2.goto(220, 260)
score_writer2.pendown()
font_setup = ("Arial", "15", "normal")
score_writer2.write(str(p2_score) + " points", font = font_setup)

# Update score function
def update_score1():
  score_writer1.clear()
  global p1_score
  p1_score += 1
  score_writer1.write(str(p1_score) + " points", font = font_setup)

def update_score2():
  score_writer2.clear()
  global p2_score
  p2_score += 1
  score_writer2.write(str(p2_score) + " points", font = font_setup)

#def collision():

# Gameplay
run = True
while run:
  wn.update()
  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

  # Score for player 1
  if ball_x > 300:
    ball.goto(0, 0)
    ball.dx *= -1
    update_score1
    
  # Score for player 2
  elif ball_x < -300:
    ball.goto(0, 0)
    ball.dx *= -1
    update_score2()

wn.mainloop()
