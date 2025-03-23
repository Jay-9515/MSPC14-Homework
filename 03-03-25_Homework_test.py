# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:46:13 2025

@author: JAY
"""

students = [
    {'name': 'Alice', 'grades': [90, 85, 92]},
    {'name': 'Bob', 'grades': [70, 88, 80]},
    {'name': 'Charlie', 'grades': [95, 93, 97]}
]

[
    {'name': 'Alice', 'grades': [85, 90, 92], 'average': 89.0},
    {'name': 'Bob', 'grades': [70, 80, 88], 'average': 79.33},
    {'name': 'Charlie', 'grades': [97, 95, 93], 'average': 95.0}
]

def name_list(students):
    for value in students:
        value['grades'].sort()
        value['average'] = round(sum(value['grades']) / len(value['grades']),2)
    return students

students = [
    {'name': 'Alice', 'grades': [90, 85, 92]},
    {'name': 'Bob', 'grades': [70, 88, 80]},
    {'name': 'Charlie', 'grades': [95, 93, 97]}
]

result = name_list(students)
print(result)