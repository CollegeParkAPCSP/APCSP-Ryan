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
def move_turtle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_sqr():
    move_turtle(tima_sqr, 0, 150)
    tima_sqr.begin_fill()
    for i in range(4):
        tima_sqr.pensize(4)
        tima_sqr.forward(50)
        tima_sqr.right(90)
        tima_sqr.color(colors[i])
        tima_sqr.end_fill()
        
def draw_tri():
    move_turtle(tima_tri, 0, 0)
    tima_tri.begin_fill()
    for _ in range(3):
        tima_tri.pensize(10)
        tima_tri.color((0.5, 0, 0.5))
        tima_tri.forward(50)
        tima_tri.right(120)
        tima_tri.end_fill()
        
def draw_pen():
    move_turtle(tima_pen, 0, -150)
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
    move_turtle(tima, -200, 0)
    
tima_sqr.hideturtle()
tima_tri.hideturtle()
tima_pen.pendown()
tima_pen.circle(15)
turtle.done()