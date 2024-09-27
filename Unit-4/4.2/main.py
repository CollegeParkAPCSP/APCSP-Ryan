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
        self.fc3 = nn.Linear(10, 1)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x
    
tima_model = Tima()

# Training loop
criterion = nn.MSELoss()
optimizer = optim.Adam(tima_model.parameters(), lr=0.001)

for epoch in tqdm(range(100)):
    # First pick a random integer
    num = random.randint(1, 100)
    num = torch.tensor([num])
    num = num.float()
    
    # Model forward pass
    rotate_num = tima_model(num)
    
    # Rotation should be 360/n
    target = torch.tensor([360/num])
    
    # normalize the target max = 360
    target = target / 360
    
    # Calculate loss
    loss = criterion(rotate_num, target)
    print(f"Epoch: {epoch}, Loss: {loss.item()}")
    
    # Backward pass
    optimizer.zero_grad()
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
        rotate_num = tima_model(torch.tensor([4.0]))
        
        # denormalize the rotation
        rotate_num = rotate_num.item() * 360
        
        print(f"Rotate: {rotate_num}")
    
    for i in range(4):
        tima_sqr.pensize(4)
        tima_sqr.forward(50)
        tima_sqr.right(rotate_num)
        tima_sqr.color(colors[i])
        tima_sqr.end_fill()
        
def draw_tri():
    move_turtle(tima_tri, 0, 0)
    tima_tri.begin_fill()
    
    with torch.no_grad():
        rotate_num = tima_model(torch.tensor([3.0]))
        
        # denormalize the rotation
        rotate_num = rotate_num.item() * 360
        
        print(f"Rotate: {rotate_num}")
        
    for _ in range(3):
        tima_tri.pensize(10)
        tima_tri.color((0.5, 0, 0.5))
        tima_tri.forward(50)
        tima_tri.right(rotate_num)
        tima_tri.end_fill()
        
def draw_pen():
    move_turtle(tima_pen, 0, -150)
    tima_pen.begin_fill()
    
    with torch.no_grad():
        rotate_num = tima_model(torch.tensor([5.0]))
        
        # denormalize the rotation
        rotate_num = rotate_num.item() * 360
        
        print(f"Rotate: {rotate_num}")
        
    for i in range(5):
        tima_pen.pensize(1 + i)
        tima_pen.forward(50)
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