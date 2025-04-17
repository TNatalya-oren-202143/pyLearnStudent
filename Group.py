import csv


class Group:
    def __init__(self, name, students=[]):
        self.__name = name
        self.__students = students
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self):
        self.__students

    def outconsole(self):
        print(f"name group = {self.__name}\n")
        # print("----------------")
        # print(self.__students)
        # print("----------------")
        for st in self.__students:
            st.outconsole()

    def saveGroup(self):
        with open("1.txt", "w") as fls:
            # print(f"name group = {self.__name}\n", file= "1.txt" )
            fls.write(self.__name)
            fls.write("\n")
            # print("----------------")
            # print(self.__students)
            # print("----------------")
            for st in self.__students:
                fls.write(st.numBooks)
                fls.write("\t")
                fls.write(st.name)
                fls.write("\t")

    def savecsv(self):
        with open("2.txt", "w") as fls:
            writer = csv.writer(fls)
            for st in self.__students:
                writer.writerow(st.name)