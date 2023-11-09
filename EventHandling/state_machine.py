### We’re going to build a program that uses a turtle to simulate the traffic lights.

### There are three lessons here:
###     The first shows off some different ways to use our turtles. 
###     The second demonstrates how we would program a state machine in Python, by using a variable 
###         to keep track of the current state, and a number of different if statements to inspect the 
###         current state, and take the actions as we change to a different state. 
###     The third lesson is to use events from the keyboard to trigger the state changes.

import turtle # Tess becomes a traffic light.

turtle.setup(700,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

def draw_housing(t):
    """ Draw a nice housing to hold the traffic lights """
    t.pensize(3)
    t.color("black", "darkgrey")
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()

### Original code from example

# tess = turtle.Turtle()
# draw_housing(tess)

# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
# state_num = 0

# def advance_state_machine():
#     global state_num
#     if state_num == 0: # Transition from state 0 to state 1
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1: # Transition from state 1 to state 2
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else: # Transition from state 2 to state 0
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0

# Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")

# def update_state():
#     advance_state_machine()
#     wn.ontimer(update_state,2000)

# update_state()
# wn.listen() # Listen for events

### Exercise

# Add to your program above as follows: draw a second housing for another set of traffic lights. 
# Create three separate turtles to represent each of the green, orange and red lights, and position 
# them appropriately within your new housing. As your state changes occur, just make one of the three 
# turtles visible at any time.

# Change the traffic light program so that changes occur automatically, driven by a timer.

# If we watch traffic lights, they turn on and off – but when they’re off they are still there, perhaps 
# just a darker color. Modify the program now so that the lights don’t disappear: they are either on, or off. 
# But when they’re off, they’re still visible.

# They want four states in their state machine: Green, then Green and Orange together, then Orange only, 
# and then Red. Additionally, they want different times spent in each state. The machine should spend 3 
# seconds in the Green state, followed by one second in the Green+Orange state, then one second in the 
# Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.

def place_turtle(t):
    # Position turtle onto the place where the green light should be
    t.forward(40)
    t.left(90)
    t.forward(50)
    # Turn tess into a big circle
    t.shape("circle")
    t.shapesize(3)

alex1 = turtle.Turtle()
alex2 = turtle.Turtle()
alex3 = turtle.Turtle()
alex1.penup()
alex1.forward(100)
alex1.pendown()
draw_housing(alex1)

alex1.penup()
place_turtle(alex1)
alex1.fillcolor("green")

alex2.penup()
alex2.forward(100)
place_turtle(alex2)
alex2.forward(70)
alex2.fillcolor("dark orange")
# alex2.hideturtle()

alex3.penup()
alex3.forward(100)
place_turtle(alex3)
alex3.forward(140)
alex3.fillcolor("dark red")
# alex3.hideturtle()

# This variable holds the current state of the machine
state_num2 = 0

def advance_state_machine2():
    global state_num2
    if state_num2 == 0: # Transition from state 0 to state 1
        # Green and Orange
        alex1.fillcolor("green")
        alex2.fillcolor("orange")
        state_num2 = 1
        wn.ontimer(advance_state_machine2, 1000)
    elif state_num2 == 1: # Transition from state 1 to state 2
        # Orange only
        alex1.fillcolor("dark green")
        state_num2 = 2
        wn.ontimer(advance_state_machine2, 1000)
    elif state_num2 == 2: # Transition from state 2 to state 3
        # Red only
        alex2.fillcolor("dark orange")
        alex3.fillcolor("red")
        state_num2 = 3
        wn.ontimer(advance_state_machine2, 2000)
    else: # Transition from state 3 to state 0
        # Green only
        alex3.fillcolor("dark red")
        alex1.fillcolor("green")
        state_num2 = 0
        wn.ontimer(advance_state_machine2, 3000)

advance_state_machine2()

wn.mainloop()
