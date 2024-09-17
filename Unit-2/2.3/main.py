# README README README README README README README
# click on the 3 bars at the top left and go to fullscreen
import turtle
tima = turtle.Turtle()
tima.speed(0)
tima.shape("turtle")
tima.penup() # we will discuss this command next week
tima.goto(0,0)
# we will discuss this command next week
tima.pendown()
# Draw text
tima.write("Let's Draw!", font=("Arial", 24, "normal"))
colors = ["red", "blue", "green", "yellow"]
# Draw square
for i in range(4):
    tima.pensize(4)
    tima.forward(50)
    tima.right(90)
    tima.color(colors[i])
tima.penup()
tima.goto(0, -100)
# Triangle
tima.pendown()
for i in range(3):
    tima.pensize(10)
    tima.color((0.5, 0, 0.5))
    tima.forward(50)
    tima.right(120)
# Pentagon
tima.penup()
tima.goto(0, -250)
tima.pendown()
tima.color("black")
for i in range(5):
    tima.pensize(1 + i)
    tima.forward(50)
    tima.right(72)
tima.penup()
tima.goto(-100, -100)
tima.pendown()
tima.write("Look at all those shapes!", font=("Arial", 24, "normal"))
turtle.done()
