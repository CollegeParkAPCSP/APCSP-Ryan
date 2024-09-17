import math
import random
user_input1: float = input("Write a float number: ")
user_input2: int = input("Write an integer number: ")
user_input1 = float(user_input1)
user_input2 = int(user_input2)
print("##### SQRT #####")
print(str(user_input1) + " -> " + str(math.sqrt(user_input1)))
print(str(user_input2) + " -> " + str(math.sqrt(user_input2)))
print("\n")
print("##### FLOAT-ABS #####")
print(str(user_input1) + " -> " + str(math.fabs(user_input1)))
print(str(user_input2) + " -> " + str(math.fabs(user_input2)))
print("\n")
print("##### E^X #####")
print(str(user_input2) + " -> " + str(math.exp(user_input2)))
print(str(user_input1) + " -> " + str(math.exp(user_input1)))
print("\n")
print("##### Ceiling #####")
print(str(user_input1) + " -> " + str(math.ceil(user_input1)))
print("\n")
print("##### Floor #####")
print(str(user_input1) + " -> " + str(math.floor(user_input1)))
print("\n")
print("##### Log Base 10 #####")
print(str(user_input1) + " -> " + str(math.log10(user_input1)))
print(str(user_input2) + " -> " + str(math.log10(user_input2)))
print("\n")
print("##### Power #####")
print(str(user_input1) + "^" + str(user_input2) + "->" +
str(user_input1**user_input2))
print(str(user_input2) + "^" + str(user_input1) + "->" +
str(user_input2**user_input1))
print("\n")
print("##### Randint #####")
print(str(user_input1) + "-" + str(user_input2) + "->" +
str(random.randint(int(user_input1), user_input2)))
print("\n")
print("##### Randrange #####")
print(str(user_input1) + "-" + str(user_input2) + "->" +
str(random.randint(int(user_input1), user_input2)))
print("\n")
print("##### Random #####")
rand1 = random.random()
rand2 = random.random()
print(str(user_input1) + "*" + str(rand1) + "->" + str(user_input1 * rand1))
print(str(user_input2) + "*" + str(rand2) + "->" + str(user_input2 * rand2))