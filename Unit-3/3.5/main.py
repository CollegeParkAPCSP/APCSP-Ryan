import math
import random

user_input1: float = input("Write a float number: ")
user_input2: int = input("Write an integer number: ")

user_input1 = float(user_input1)
user_input2 = int(user_input2)

print("##### SQRT #####")
print(f"{user_input1} -> {math.sqrt(user_input1)}")
print(f"{user_input2} -> {math.sqrt(user_input2)}")
print("\n")

print("##### FLOAT-ABS #####")
print(f"{user_input1} -> {math.fabs(user_input1)}")
print(f"{user_input2} -> {math.fabs(user_input2)}")
print("\n")

print("##### E^X #####")
print(f"{user_input1} -> {math.exp(user_input1)}")
print(f"{user_input2} -> {math.exp(user_input2)}")
print("\n")

print("##### Ceiling #####")
print(f"{user_input1} -> {math.ceil(user_input1)}")
print("\n")

print("##### Floor #####")
print(f"{user_input1} -> {math.floor(user_input1)}")
print("\n")

print("##### Log Base 10 #####")
print(f"{user_input1} -> {math.log10(user_input1)}")
print(f"{user_input2} -> {math.log10(user_input2)}")
print("\n")

print("##### Power #####")
print(f"{user_input1}^{user_input2} -> {user_input1**user_input2}")
print(f"{user_input2}^{user_input1} -> {user_input2**user_input1}")
print("\n")

print("##### Randint #####")
try: 
    print(f"{user_input1}-{user_input2} -> {random.randint(int(user_input1), user_input2)}")
except:
    print(f"{user_input2}-{user_input1} -> {random.randint(user_input2, int(user_input1))}")
print("\n")

print("##### Randrange #####")
try: 
    print(f"{user_input1}-{user_input2} -> {random.randrange(int(user_input1), user_input2)}")
except:
    print(f"{user_input2}-{user_input1} -> {random.randrange(user_input2, int(user_input1))}")
print("\n")

print("##### Random #####")
rand1 = random.random()
rand2 = random.random()
print(f"{user_input1}*{rand1} -> {user_input1 * rand1}")
print(f"{user_input2}*{rand2} -> {user_input2 * rand2}")
print("\n")