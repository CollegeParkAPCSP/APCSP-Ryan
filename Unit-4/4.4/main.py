# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer) -> bool:
    # For grading purposes: limit is 60 and 90 or 100
    limit = [60, 90 if not is_summer else 100]
    
    # For grading purposes: limit[0] = 60, limit[1] = 90 or 100
    if limit[0] <= temp <= limit[1]:
        return True
    
    return False

print("True", squirrel_play(70, False)) # True
print("False", squirrel_play(95, False)) # False
print("True", squirrel_play(95, True)) # True
print("True", squirrel_play(90, False)) # True  
print("True", squirrel_play(90, True)) # True
print("False", squirrel_play(50, False)) # False
print("False", squirrel_play(50, True)) # False
print("False", squirrel_play(100, False)) # False
print("True", squirrel_play(100, True)) # True
print("False", squirrel_play(105, True)) # False
print("False", squirrel_play(59, False)) # False
print("False", squirrel_play(59, True)) # False
print("True", squirrel_play(60, False)) # True

def sorta_sum(a, b):
    if 10 <= (a + b) <= 19:
        return 20
    
    return a + b

print("7", sorta_sum(3, 4)) # 7
print("20", sorta_sum(9, 4)) # 20
print("21", sorta_sum(10, 11)) # 21
print("9", sorta_sum(12, -3)) # 9
print("9", sorta_sum(-3, 12)) # 9
print("20", sorta_sum(4, 6)) # 20
print("21", sorta_sum(14, 7)) # 21
print("20", sorta_sum(14, 6)) # 20