class Human:
    # name="Ivan"
    # fam="Ivanow"
    #__slots__ = {self.__name, __fam }

    def __init__(self, name="", fam=""):
        self.__name = name
        self.__fam = fam

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def outconsole(self):
        print(f"name={self.__name}\t fam={self.__fam}")

#__new__
if __name__ == '__main__':
    student1 = Human("Wasya", "Sidorow")
    student1 = Human("Wasya")
    student1 = Human()
    student1.fam = "Petrow"
    student1.name=""
    student1.outconsole()
    print(student1.__dict__)
    student2 = Human("Petya"," Lisan")
    student2.outconsole()
    print(student2.__dict__)
    print(Human.__dict__)

