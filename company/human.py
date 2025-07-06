from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name, lname, age):
        self.__name = name
        self.__last_name = lname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

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