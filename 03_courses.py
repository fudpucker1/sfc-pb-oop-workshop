class Course:
   def __int__(self, course_name):
      self.name = course_name
      self.students = []

   def add_student(self, student):
      self.students.append(student)

   def get_average_grade(self):
      return (sum(student.get_grade() for student in self.students)) / len(self.students)

   def get_total_students(self):
      return len(self.students)


class Student:
   def __int__(self, name, grade):
      self.name = name
      self.grade = grade

   def get_grade(self):
      return self.grade