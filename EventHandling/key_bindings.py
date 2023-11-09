### Add some new key bindings

import turtle

turtle.setup(400,500) # Determine the window size
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling keypresses!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle() # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye() # Close down the turtle window

def turn_red():
    tess.color("red")

def turn_green():
    tess.color("green")

def turn_blue():
    tess.color("blue")

pen_size = 1

def increase_size():
    global pen_size
    if pen_size < 20:
        pen_size += 1
        tess.pensize(pen_size)

def decrease_size():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
        tess.pensize(pen_size)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(turn_red, "r")
wn.onkey(turn_green, "g")
wn.onkey(turn_blue, "b")
wn.onkey(increase_size, "+")
wn.onkey(decrease_size, "-")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

