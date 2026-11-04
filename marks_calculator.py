#My First Numpy Project_ students marks calculator 
#Created by Iram Shehzadi 
import numpy as np

# 5 students ke marks (English, Math, Science)
marks = np.array([
    [80, 90, 85],
    [70, 75, 80],
    [90, 95, 92],
    [60, 65, 70],
    [85, 88, 90]
])

print("Marks:\n", marks)

# Har student ka average
average = np.mean(marks, axis=1)
print("\nHar student ka average:", average)

# Sab se zyada aur kam marks
print("\nSab se zyada marks:", np.max(marks))
print("Sab se kam marks:", np.min(marks))

# Class ka overall average
print("\nClass ka average:", np.mean(marks))