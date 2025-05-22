# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import hello
from Cafedra import Cafedra
from Group import Group
from Student import Student
from hello import print_hi as print
from zavcafedroi import Zavcafedroi

#студент(зачетка,группа)
#преподаватель(должность,кафедра)
#зав. кафедрой(научное направления,кафедра)
#человек(имя, фамилия,отчество, год. рождения)


#кафедра
#группа
# Добавить зачетка - часть студента
#Добавить дисциплина -  часть группы
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
    student2 = Student("Petr", "Petrow", "A18279")
    student3 = Student("Nikola", "Petrow", "A18279")

    groupe = Group("22Ping")
    groupe.students.append(student1)
    groupe.students.append(student2)
    groupe.students.append(student3)
    groupe.outconsole()
    zavcafedroi1 = Zavcafedroi("Ivan", "Ivaniw", "Assistent")
    zavcafedroi1.outconsole()
    cafedra1 = Cafedra("POVTAS", zavcafedroi1)
    cafedra1.outconsole()
    groupe.saveGroup()
    groupe.savecsv()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
