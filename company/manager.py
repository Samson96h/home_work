from human import Human

class Manager(Human):
    def __init__(self, name, lname, age):
        super().__init__(name, lname, age)
        self.__emp = []

    @property
    def emp(self):
        return self.__emp

    def hire(self, emp):
        if emp in self.emp:
            print(f"{emp.name} is already hired")
        if emp.isbusy == False and emp.age >= 18:
            if len(self.__emp) < 10:
                self.__emp.append(emp)
                emp.isbusy = True
                print(f'{emp.name} successfully hired')
            else:
                print("Cannot hire more than 10 employees")
        else:
            print(f"{emp.name} is busy")

    def fire(self, emp):
        if emp in self.emp:
            self.__emp.remove(emp)
            emp.isbusy = False
            print(f'{emp.name} successfully fired')

    def show_employ(self):
        for emp in self.__emp:
            print(emp)

    def __str__(self):
        return f"My name is {self.name}, {self.last_name},i am {self.age} years old"