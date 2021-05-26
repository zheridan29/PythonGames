import turtle

wn = turtle.Screen()
wn.title("Pong by @zheridan29")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#stops the window from updating
#so we need to manually update the window
#and can speed the game in terms of performance
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation set to max
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #moves the pen up after drawing the shape
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation set to max
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #moves the pen up after drawing the shape
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation set to max
ball.shape("square")
ball.color("white")
ball.penup() #moves the pen up after drawing the shape
ball.goto(0, 0)
#rate of change in movement (delta)
ball.dx = .1
ball.dy = .1

# Function
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

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "5")
wn.onkeypress(paddle_b_down, "2")

#lets try to write comment here

#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor()  + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290);
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290);
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1;
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1;
    

    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1