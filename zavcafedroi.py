from Teacher import Teacher
class Zavcafedroi(Teacher):
    def __init__(self, name, fam, post, cafedra = None):
        Teacher.__init__(self, name, fam, post)
        self.__cafedra = cafedra

    @property
    def cafedra(self):
        return self.__cafedra
    def outconsole(self):
        super().outconsole()
        print(f"post={self.cafedra}")


if __name__ == '__main__':
    teacher1 = Zavcafedroi("Ivan", "Ivaniw", "Assistent")
    teacher1.outconsole()
    print(teacher1.post)