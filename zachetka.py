class Gradebook:

    def __init__(self, record_book_number, student_name, group):

        self.record_book_number = record_book_number
        self.student_name = student_name
        self.group = group
        self.grades = {}

    def add_grade(self, subject, grade):
        if not isinstance(grade, int):
            raise ValueError("Оценка должна быть целым числом.")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть в диапазоне от 2 до 5.")
        self.grades[subject] = grade

    def get_grade(self, subject):

        return self.grades.get(subject)

    def get_average_grade(self):

        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):

        return (f"Record Book Number: {self.record_book_number}\n"
                f"Student: {self.student_name}\n"
                f"Group: {self.group}\n"
                f"Grades: {self.grades}\n"
                f"Average Grade: {self.get_average_grade()}")


# Example Usage:
student1 = Gradebook("12345", "Ivan Ivanov", "IVT-21")
student1.add_grade("Mathematics", 5)
student1.add_grade("Programming", 4)
student1.add_grade("Physics", 3)

print(student1)


print(f"Grade in Mathematics: {student1.get_grade('Mathematics')}")  # Grade in Mathematics: 5
print(f"Grade in History: {student1.get_grade('History')}")  # Grade in History: None

try:
    student1.add_grade("Chemistry", 6)
except ValueError as e:
    print(f"Error: {e}")

