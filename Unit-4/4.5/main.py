# 1
def evaluate_conditions(a: bool, b: bool):
    # true if a is one and b is one and true if either a or b is one
    if a and b or a or b:
        return True
    
    return False

print("True", evaluate_conditions(1, 1)) # True

# 2
def is_teenager(age):
    return 13 <= age <= 19

print("True", is_teenager(13)) # True

# 3
def is_valid_login(username, password):
    if username == "admin" and password == "secret":
        return True
    
    return False

print("True", is_valid_login("admin", "secret")) # True
print("False", is_valid_login("admin", "password")) # False

# 4
def exclusive_or(a, b):
    return a != b # True if a is not equal to b ie: a = true b = false == true

print("True", exclusive_or(1, 0)) # True

# 5
def lights_on(a, b):
    return a or b

print("True", lights_on(True, False)) # True
print("False", lights_on(False, False)) # False

# 6
def is_eligible(age, citizenship):
    return age >= 18 and citizenship == True

print("True", is_eligible(18, True)) # True
print("False", is_eligible(17, True)) # False

# 7
def can_drive(age, has_license):
    return age >= 16 and has_license == True

print("True", can_drive(16, True)) # True
print("False", can_drive(15, True)) # False

# 8
def is_safe_to_cross(traffic_light, pedestrian_light):
    return traffic_light == "green" and pedestrian_light == "walk"

print("True", is_safe_to_cross("green", "walk")) # True
print("False", is_safe_to_cross("red", "walk")) # False

# 9
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print("True", is_leap_year(2000)) # True
print("False", is_leap_year(1900)) # False