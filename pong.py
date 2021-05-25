import turtle

wn = turtle.Screen()
wn.title("Pong by @zheridan29")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#stops the window from updating
#so we need to manually update the window
#and can speed the game in terms of performance
wn.tracer(0)

#Main game loop
while True:
    wn.update()

