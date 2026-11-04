# Student Marks Calculator - Numpy Project
# Author: Iram Shehzadi
# Description: Calculates student performance using Numpy

import numpy as np

# Marks of 5 students in 3 subjects (English, Math, Science)
marks = np.array([
    [80, 90, 85],
    [70, 75, 80],
    [90, 95, 92],
    [60, 65, 70],
    [85, 88, 90]
])

print("Student Marks Dataset:\n", marks)

# Calculate average marks for each student
average_per_student = np.mean(marks, axis=1)
print("\nAverage Marks Per Student:", average_per_student)

# Find highest and lowest marks in the class
print("\nHighest Marks in Class:", np.max(marks))
print("Lowest Marks in Class:", np.min(marks))

# Calculate overall class average
print("\nOverall Class Average:", np.mean(marks))