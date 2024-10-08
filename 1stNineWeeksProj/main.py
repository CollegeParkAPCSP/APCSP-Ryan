import turtle
import math
import random

screen = turtle.Screen()
screen.reset()
screen.setworldcoordinates(-100, -100, 100, 100) # 200 x 200 (40000) square

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
draw_square(-60, 60, tima, 30)

draw_circle(0, 60, tima, 15)

draw_triangle(60, 60, tima, 10)

draw_reg_pentagon(-60, -60, tima, 20)

draw_reg_hexagon(0, -60, tima, 15)

draw_reg_decagon(60, -60, tima, 8)

