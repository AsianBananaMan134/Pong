import turtle as trtl

wn = trtl.Screen()
wn.bgcolor("black")
wn.tracer(0)
"""
Border
"""
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
p1.goto(-275, 0)

# Player 2
p2 = trtl.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(275, 0)

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
ball.dx = 0.5
ball.dy = 0.5

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
wn.onkey(move_up_1, "w")
wn.onkey(move_down_1, "s")
wn.onkey(move_up_2, "Up")
wn.onkey(move_down_2, "Down")

"""
Score Writer
"""
# Player 1 Score
score_writer1 = trtl.Turtle()
score_writer1.speed(0)
score_writer1.color("white")
score_writer1.penup()
score_writer1.hideturtle()
score_writer1.goto(-285,270)
score_writer1.pendown()

# Player 2 Score
score_writer2 = trtl.Turtle()
score_writer2.speed(0)
score_writer2.color("white")
score_writer2.penup()
score_writer2.hideturtle()
score_writer2.goto(215,270)
score_writer2.pendown()

p1_score = 0
p2_score = 0
font_setup = ("Arial", "15", "normal")
score_writer1.write(str(p1_score) + " points", font = font_setup)
score_writer2.write(str(p1_score) + " points", font = font_setup)

"""
Timer
"""
#-----make a rectangle box for the score-----
t = trtl.Turtle()
counter =  trtl.Turtle() 
counter.speed(0)
t.penup()
t.goto(-30,220)
t.pendown()

#-----countdown variables-----
timer = 180
counter_interval = 1000   #1000 represents 1 second
timer_up = False

def make_timer():
  t.color("white")
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.hideturtle()
  
def make_big_rectangle():
  counter.color("white")
  counter.forward(150)
  counter.left(90)
  counter.forward(50)
  counter.left(90)
  counter.forward(150)
  counter.left(90)
  counter.forward(50)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    p1.hideturtle()
    p2.hideturtle()
    ball.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# -----make the timer box-----
t.penup() 
t.pendown()
make_timer()
counter.penup()
counter.goto(-25,240)
counter.pendown()
make_big_rectangle()
t.hideturtle()
counter.hideturtle()
countdown()

"""
While True
"""
while True:
    wn.update()

    # Moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and Wall Collision
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    
    elif ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # Score
    if ball.xcor() > 290:
        p1_score += 1
        score_writer1.clear()
        score_writer1.write(str(p1_score) + " points", font = font_setup)
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -290:
        p2_score += 1
        score_writer2.clear()
        score_writer2.write(str(p2_score) + " points", font = font_setup)
        ball.goto(0, 0)
        ball.dx *= -1

    # Collision for players and ball
    if ball.xcor() < -260 and ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 260 and ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50:
        ball.dx *= -1

wn.mainloop()
wn.ontimer(countdown, counter_interval)
