class Human:
    def __init__(self, name: str, surname: str, age: int, career: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__career = career

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @surname.deleter
    def surname(self):
        del self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @property
    def career(self):
        return self.__career

    @career.setter
    def career(self, career):
        self.__career = career

    @career.deleter
    def career(self):
        del self.__career