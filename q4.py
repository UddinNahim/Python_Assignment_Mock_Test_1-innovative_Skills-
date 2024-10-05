'''
Write a Python function print_student_averages(grades) that takes a 2D list where each inner list represents a student's grades in different subjects. The function should print each student's grades and their average grade. 
'''

def print_student_averages(grades):
    for student in grades:
      name = student[0]
      grades_list = student[1:]
      average_grade = sum(grades_list)/len(grades_list)
      print(f"{name}'s grades: {grades_list}")
      print(f"{name}'s average grade: {average_grade}")
      print()
print_student_averages([["Nahim Uddin", 45, 50, 62], ["Nafis Fuad", 78, 82, 85], ["Watson", 52, 95, 88]])

