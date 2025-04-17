


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
        print("----------------")
        print(self.__students)
        print("----------------")
        for st in self.__students:
            st.outconsole()

