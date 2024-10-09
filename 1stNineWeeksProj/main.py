import turtle
import math
import random
from time import sleep

screen = turtle.Screen()
screen.reset()
screen.setworldcoordinates(-400, -400, 400, 400) # 800 x 800 (640000) square

tima = turtle.Turtle()
tima.penup()
tima.speed(0)

# ----- START DAY 1 -----
def draw_square(x, y, turtle, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    
def draw_circle(x, y, turtle, radius):
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    
def draw_reg_pentagon(x, y, turtle, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(72)
    turtle.end_fill()
    turtle.penup()
    
def draw_triangle(x, y, turtle, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    
def draw_reg_hexagon(x, y, turtle, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)
    turtle.end_fill()
    turtle.penup()
    
def draw_reg_decagon(x, y, turtle, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(10):
        turtle.forward(size)
        turtle.right(36)
    turtle.end_fill()
    turtle.penup()
    
# ----- END DAY 1 -----

# ----- START DAY 2 -----
def draw_shape(shape, x, y, size):
    if shape == "square":
        draw_square(x, y, tima, size)
    elif shape == "circle":
        draw_circle(x, y, tima, size)
    elif shape == "pentagon":
        draw_reg_pentagon(x, y, tima, size)
    elif shape == "triangle":
        draw_triangle(x, y, tima, size)
    elif shape == "hexagon":
        draw_reg_hexagon(x, y, tima, size)
    elif shape == "decagon":
        draw_reg_decagon(x, y, tima, size)
    else:
        print("Invalid shape")
        return 0
        
    return calc_area(shape, size)
        
def calc_area(shape, size):
    if shape == "square":
        return size ** 2
    elif shape == "circle":
        return math.pi * size ** 2
    elif shape == "pentagon":
        return 1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * size ** 2
    elif shape == "triangle":
        return 1/2 * size ** 2 * math.sqrt(3) / 2
    elif shape == "hexagon":
        return 3/2 * math.sqrt(3) * size ** 2
    elif shape == "decagon":
        return 5/2 * size ** 2 * math.sqrt(5 + 2 * math.sqrt(5))
    else:
        print("Invalid shape")
        return 0
    
shapes_area = 0
shapes = ["square", "circle", "pentagon", "triangle", "hexagon", "decagon"]
for _ in range(3):
    tima.color(random.random(), random.random(), random.random())
    user_shape = turtle.textinput("Shape", "Enter a shape: ")
    while user_shape not in shapes:
        user_shape = turtle.textinput("Shape", "Enter a shape: ")
    user_x = turtle.numinput("X", "Enter an x coordinate: ", 0, -400, 400)
    user_y = turtle.numinput("Y", "Enter a y coordinate: ", 0, -400, 400)
    user_size = turtle.numinput("Size", "Enter a size: ")
    
    shapes_area += draw_shape(user_shape, user_x, user_y, user_size)

# ----- END DAY 2 -----

# ----- START DAY 3 -----
tima.goto(0, 0)
tima.color("black")
tima.write("Total Area: " + str(shapes_area), align="center", font=("Arial", 12, "normal"))

turtle.done()
# ----- END DAY 3 -----