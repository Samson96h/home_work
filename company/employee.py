from human import Human

class Employee(Human):
    def __init__(self, name, lname, age, prof, busy=False):
        super().__init__(name, lname, age)
        self.__profession = prof
        self.__busy = busy

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    @property
    def busy(self):
        return self.__busy

    @busy.setter
    def busy(self, busy):
        self.__busy = busy

    def __str__(self):
        return f"My name is {self.name} {self.last_name} i am {self.age} years old"
