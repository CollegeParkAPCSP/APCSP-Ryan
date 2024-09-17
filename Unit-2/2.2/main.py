# README README README README README README README
# click on the 3 bars at the top left and go to fullscreen
import turtle
tima = turtle.Turtle()
tima.shape("turtle")
tima.penup() # we will discuss this command next week
tima.goto(0,125)
# we will discuss this command next week
tima.pendown()
# write code to make a square below these comments
# use forward, back, left, right and goto commands only
# go to next area on the screen
for i in range(4):
    tima.forward(50)
    tima.right(90)
##
tima.penup()
tima.goto(0,0)
tima.pendown()
# write code to make a triangle below these comments
# use forward, back, left, right and goto commands only
# go to next area on the screen
for i in range(3):
    tima.forward(50)
    tima.right(120)
    tima.penup()
    tima.goto(0,-125)
    tima.pendown()
# write code to make a pentagon below these comments
# use forward, back, left, right and goto commands only
for i in range(5):
    tima.forward(50)
    tima.right(72)
    tima.penup()
    tima.goto(-200, 0)
    turtle.done()