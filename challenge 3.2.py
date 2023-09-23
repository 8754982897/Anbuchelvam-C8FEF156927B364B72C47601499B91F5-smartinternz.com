'''Implement a function called sort_students that takes a list of students objects as input and sorts the list based on their CGPA in descending order.Each student object has the following attributes Name(string),roll_number(string),andcgpa(float).Test the function with different input list of students'''
class student:
    def __init__(self,name,roll_number,cgpa):
       self.name=name
       self.roll_number=roll_number
       self.cgpa=cgpa
def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student: student.cgpa, reverse=True)
  return sorted_students
  #Example usage
students=[
  student ("Ajith","UG01",7.8),       student("vijay","UG02",8.9),
  student("Anbu","UG03",9.9),
  student("Selasri","UG04",9.9)
]
sorted_students=sort_students(students)
#print the sorted of students
for student in sorted_students:
    print("Name:{},Roll Number:{},CGPA:{}".format(student.name, student.roll_number,student.cgpa))