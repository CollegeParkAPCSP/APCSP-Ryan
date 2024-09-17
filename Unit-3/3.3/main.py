import turtle

tima = turtle.Turtle()
tima.shape("arrow")
tima.penup()

# First question
def ask_question(question, answer):
    user_inp = input(question)
    tima.write(question + user_inp, move=False, align="center", font=("Arial", 16, "normal"))
    tima.goto(tima.position()[0], tima.position()[1] - 30)
    tima.write(answer, move=False, align="center", font=("Arial", 16, "normal"))

ask_question("What is 2? ", "The correct answer is integer")
tima.goto(0,  -100)
tima.color("red")

ask_question("What is 2.0? ", "The correct answer is float")
tima.goto(0, -200)
tima.color("chartreuse")

ask_question("What is '2'? ", "The correct answer is string")
tima.goto(0, -300)
tima.color("green")

turtle.done()