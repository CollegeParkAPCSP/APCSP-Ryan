# TASK ONE
# create 5 variables that hold the following information
# a students first name, last name, score, grade, date of birth
# pick the data type that makes the most sense to you
# print this information out to the user in a clear way

stu_first_name: str = "John"
stu_last_name: str = "Doe"
stu_score: int = 95
stu_grade: str = "A"
stu_dob: str = "01/01/2000"

stu = [stu_first_name, stu_last_name, stu_score, stu_grade, stu_dob]

print("TASK ONE OUTPUT")
for i in range(5):
    print(stu[i])
# TASK TWO
# change the identifier to a more clear description
# The first should be a temperature
# the second is the name of a customer
# the third is a status indicator of a printer
# finally, print this information out to the user in a clear way
print("")
print("TASK TWO OUTPUT")
temp = 86
customer_name = "Bob"
status = False

vars = [temp, customer_name, status]

for i in range(3):
    print(vars[i])
# TASK THREE
# change the identifier / data of each variable such that
# you do not get an error when you run the program
# they will be commented to not effect tasks one and two
# uncomment them before you turn it in and have fixed the issues
# finally, print this information out to the user in a clear way
print("")
print("TASK THREE OUTPUT")
print("")
score = 3
GamePoints = 89
myString = "This is my string"
temperatureAsFloat = 99
not_a_bool = False

vars = [score, GamePoints, myString, temperatureAsFloat, not_a_bool]

for i in range(5):
    print(vars[i])