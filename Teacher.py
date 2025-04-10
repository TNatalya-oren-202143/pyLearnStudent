from Human import Human
class Teacher(Human):
    def __init__(self, name, fam, post):
        Human.__init__(self, name, fam)
        self.__post = post

    @property
    def post(self):
        return self.__post
    def outconsole(self):
        super().outconsole()
        print(f"post={self.post}")

if __name__ == '__main__':
    teacher1 = Teacher("Ivan", "Ivaniw", "Assistent")
    teacher1.outconsole()
    print(teacher1.post)