import unittest

exam = 80
presentation = 60
grade = ""

# Function to check the grade
def check_grade(exam, presentation) -> str:
    if (exam > 90) and (presentation > 80): # above 90 in exam and above 80 in presentation
        grade = "A"
        
    elif (exam > 80) or (presentation > 75): # above 80 in exam or above 75 in presentation
        grade = "B"
        
    elif (exam > 70) or (presentation > 60): # above 70 in exam or above 60 in presentation
        grade = "C"
        
    elif (exam > 60): # above 60 in exam
        grade = "D"
        
    else: # below 60 in exam
        grade = "F"
        
    return grade

print(check_grade(exam, presentation))