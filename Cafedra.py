class Cafedra:
    def __init__(self, name, __zavcafedroi = None):
        self.__name = name
        self.__zavcafedroi = __zavcafedroi


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def zavcafedroi(self):
        return self.__zavcafedroi

    @zavcafedroi.setter
    def zavcafedroi(self):
        self.__zavcafedroi

    def outconsole(self):
        print(f"name cafedri = {self.__name}\n")
        print("----------------")
        self.__zavcafedroi.outconsole()
        print("----------------")