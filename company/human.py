from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name, lname, age):
        if type(name) == str:
            self.name = name
        else:
            self.name = "Jack"
        if type(lname) == str:
            self.last_name = lname
        else:
            self.last_name = "Smith"
        if type(age) == int:
            self.age = age
        else:
            self.age = 18

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
        else:
            self.__name = "Jack"

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if type(value) == str:
            self.__last_name = value
        else:
            self.__last_name = "Smith"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            self.__age = 16
        else:
            self.__age = age


    @abstractmethod
    def __str__(self):
        return