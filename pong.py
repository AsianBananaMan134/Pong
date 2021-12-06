import turtle as trtl
import threading

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
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-280, 0)

# Player 2
p2 = trtl.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(280, 0)

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
    if y < -280:
        y = -280
    p1.sety(y)


def move_down_1():
    y = p1.ycor()
    y -= 20
    p1.sety(y)
    if y > 280:
        y = 280
    p1.sety(y)

# Player 2
def move_up_2():
    y = p2.ycor()
    y += 20
    p2.sety(y)
    if y < -280:
        y = -280
    p2.sety(y)

def move_down_2():
    y = p2.ycor()
    y -= 20
    p2.sety(y)
    if y > 280:
        y = 280
    p2.sety(y)

# Make it so they can both 
if __name__ == "__main__":
    p1u = threading.Thread(name="mu1", target=move_up_1())
    p1u.start()
    p1d = threading.Thread(name="md1", target=move_down_1())
    p1d.start()
    p2u = threading.Thread(name="mu2", target=move_up_2())
    p2u.start()
    p2d = threading.Thread(name="md2", target=move_down_2())
    p2d.start()
    p1u.join()
    p1d.join()
    p2u.join()
    p2d.join()
    exit(0)




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
