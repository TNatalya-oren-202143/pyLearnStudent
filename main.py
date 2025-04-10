# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import hello
from Group import Group
from Student import Student
from hello import print_hi as print
#студент(зачетка,группа)
#преподаватель(должность,кафедра)
#зав. кафедрой(научное направления,кафедра)
#человек(имя, фамилия,отчество, год. рождения)


#кафедра
#группа
#зачетка
#дисциплина
#ведомость
#------------***
#студент-часть группы
#зачетка-часть студента
#дисциплина - часть группы
#группа- часть кафедры
#препод-часть кафедры
#зав.каф -часть кафедры

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    student1 = Student("Ivan", "Ivaniw", "A18279")
    student1.outconsole()
    student2 = Student("Petr", "Petrow", "A18279")
    student2.outconsole()
    student3 = Student("Nikolay", "Petrow", "A18279")
    student3.outconsole()

    groupe = Group("22Ping")
    groupe.students.append(student1)
    groupe.students.append(student2)
    groupe.students.append(student3)
    groupe.outconsole()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
