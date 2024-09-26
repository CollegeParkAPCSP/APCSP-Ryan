import turtle
import torch
import random
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from tqdm import tqdm

class Tima(nn.Module):
    def __init__(self):
        super(Tima, self).__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 10)
        self.fc3 = nn.Linear(10, 2)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x
    
tima_model = Tima()

# Training loop
criterion = nn.MSELoss()
optimizer = optim.Adam(tima_model.parameters(), lr=0.001)

for epoch in tqdm(range(500)):
    # Training loop. Inputs are 3,4,5 and outputs are [10, 90], [10, 60], [10, 120]
    for i in range(3, 6):
        optimizer.zero_grad()
        inputs = torch.tensor([i], dtype=torch.float32)
        outputs = tima_model(inputs)
        if i == 3:
            loss = criterion(outputs, torch.tensor([1, 0.25], dtype=torch.float32))
        elif i == 4:
            loss = criterion(outputs, torch.tensor([1, 0.167], dtype=torch.float32))
        elif i == 5:
            loss = criterion(outputs, torch.tensor([1, 0.3], dtype=torch.float32))
        print(f"Epoch: {epoch}, Loss: {loss.item()}")
        loss.backward()
        optimizer.step()

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
        
    with torch.no_grad():
        move_num, rotate_num = tima_model(torch.tensor([4.0]))
        move_num = move_num.item() * 40
        rotate_num = rotate_num.item() * 360
        print(f"Move: {move_num}, Rotate: {rotate_num}")
    
    for i in range(4):
        tima_sqr.pensize(4)
        tima_sqr.forward(move_num)
        tima_sqr.right(rotate_num)
        tima_sqr.color(colors[i])
        tima_sqr.end_fill()
        
def draw_tri():
    move_turtle(tima_tri, 0, 0)
    tima_tri.begin_fill()
    
    with torch.no_grad():
        move_num, rotate_num = tima_model(torch.tensor([3.0]))
        move_num = move_num.item() * 40
        rotate_num = rotate_num.item() * 360
        print(f"Move: {move_num}, Rotate: {rotate_num}")
        
    for _ in range(3):
        tima_tri.pensize(10)
        tima_tri.color((0.5, 0, 0.5))
        tima_tri.forward(move_num)
        tima_tri.right(rotate_num)
        tima_tri.end_fill()
        
def draw_pen():
    move_turtle(tima_pen, 0, -150)
    tima_pen.begin_fill()
    
    with torch.no_grad():
        move_num, rotate_num = tima_model(torch.tensor([5.0]))
        move_num = move_num.item() * 40
        rotate_num = rotate_num.item() * 360
        print(f"Move: {move_num}, Rotate: {rotate_num}")
        
    for i in range(5):
        tima_pen.pensize(1 + i)
        tima_pen.forward(move_num)
        tima_pen.right(rotate_num)
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