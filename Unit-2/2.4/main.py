# README README README README README README README
# click on the 3 bars at the top left and go to fullscreen
import turtle
tima_sqr = turtle.Turtle()
tima_tri = turtle.Turtle()
tima_pen = turtle.Turtle()
timas = [tima_sqr, tima_tri, tima_pen]
######## SETUP ########
for tima in timas:
    tima.speed(6)
    tima.shape("arrow")
    tima.penup()
    tima.goto(0, 40)
    tima.pendown()
    tima.write("Let's Draw!", font=("Arial", 24, "normal"))
colors = ["red", "blue", "green", "yellow"]
######## FUNCTIONS ########
def draw_sqr():
    tima_sqr.penup()
    tima_sqr.goto(0, 150)
    tima_sqr.pendown()
    tima_sqr.begin_fill()
    for i in range(4):
        tima_sqr.pensize(4)
        tima_sqr.forward(50)
        tima_sqr.right(90)
        tima_sqr.color(colors[i])
        tima_sqr.end_fill()
def draw_tri():
    tima_tri.penup()
    tima_tri.goto(0, 0)
    tima_tri.pendown()
    tima_tri.begin_fill()
    for _ in range(3):
        tima_tri.pensize(10)
        tima_tri.color((0.5, 0, 0.5))
        tima_tri.forward(50)
        tima_tri.right(120)
        tima_tri.end_fill()
def draw_pen():
    tima_pen.penup()
    tima_pen.goto(0, -150)
    tima_pen.pendown()
    tima_pen.begin_fill()
    for i in range(5):
        tima_pen.pensize(1 + i)
        tima_pen.forward(50)
        tima_pen.right(72)
        tima_pen.end_fill()
######## MAIN CODE ########
draw_sqr()
draw_tri()
draw_pen()
for tima in timas:
    tima.penup()
    tima.goto(-200, 0)
tima_sqr.hideturtle()
tima_tri.hideturtle()
tima_pen.pendown()
tima_pen.circle(15)
turtle.done()