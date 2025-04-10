from Human import Human
class Student(Human):
    def __init__(self, name, fam, numBooks):
        Human.__init__(self, name, fam)
        self.__numBooks = numBooks

    @property
    def numBooks(self):
        return self.__numBooks


    def outconsole(self):
        super().outconsole()
        print(f"numBooks={self.numBooks}")

if __name__ == '__main__':
    student1 = Student("Ivan", "Ivaniw", "A18279")
    student1.outconsole()
