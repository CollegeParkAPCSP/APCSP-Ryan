user_grade = float(input("Enter your grade: "))

def check_grade(grade: float):
    if grade == 5.0:
        print("Perfect Score!")
    elif 4.0 <= grade < 5.0:
        print("Thats an A!")
    elif 3.0 <= grade < 4.0:
        print("Thats a B!")
    elif 2.0 <= grade < 3.0:
        print("Thats a C!")
    elif 1.0 <= grade < 2.0:
        print("Thats a D!")
    elif 0.0 <= grade < 1.0:
        print("Thats an F! :(")
    else:
        print("Invalid Grade!")
        
check_grade(user_grade)