
#
# short_names = [name.upper() for name in names if len(name) > 5]
#
# print(short_names)
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student:random.randint(1, 100) for student in names}


passed_students = {student for student in student_scores if student_scores[student] >= 60}

print(student_scores)

print(passed_students)