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
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #moves the pen up after drawing the shape
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation set to max
paddle_b.shape("square")
paddle_b.color("white")
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

#Main game loop
while True:
    wn.update()

