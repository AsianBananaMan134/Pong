import turtle as trtl

wn = trtl.Screen()
wn.bgcolor("black")

# No lag
wn.tracer(0)

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
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

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
While True
"""
while True:
    wn.update()

wn.mainloop()