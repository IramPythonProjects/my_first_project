# Student Grade System
# Author: Iram Shehzadi
# Description: Calculates grades based on student marks

def calculate_grade(marks):
    if marks >= 90:
        return "A+ Grade"
    elif marks >= 80:
        return "A Grade"
    elif marks >= 70:
        return "B Grade"
    elif marks >= 60:
        return "C Grade"
    elif marks >= 50:
        return "D Grade"
    else:
        return "Fail"

# Example Students
students = {
    "Ali": 88,
    "Sara": 92,
    "Ahmed": 65,
    "Iram": 95,
    "Zain": 45
}

print("--- Student Grade Report ---\n")
for name, marks in students.items():
    grade = calculate_grade(marks)
    print(f"Student: {name} | Marks: {marks} | Result: {grade}")