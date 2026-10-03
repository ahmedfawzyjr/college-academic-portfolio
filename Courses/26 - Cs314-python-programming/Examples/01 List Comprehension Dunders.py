# 01_list_comprehension_dunders.py

class Student:
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __repr__(self):
        return f"Student({self.name}, GPA={self.gpa})"

students = [
    Student("Ahmed", 3.85),
    Student("Sara", 3.40),
    Student("Omar", 3.92),
    Student("Mona", 2.95)
]

# Filter honor students using list comprehension
honor_students = [s for s in students if s.gpa >= 3.50]
print("Honor Students:", honor_students)
