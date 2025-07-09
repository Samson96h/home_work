from employee import Employee
from manager import Manager


emp1 = Employee("John","Smith" ,22, "programmer")

emp2 = Employee('Lana',"Martinez",30, "driver")

emp3 = Employee('Mher',"Arzumanyan",23,"assistant")

manager1 = Manager("Mark", "Jordan", 45)

manager2 = Manager("Karen", "Voskanyan", 28)


manager1.hire(emp1)
manager1.hire(emp2)
manager1.hire(emp3)

manager2.hire(emp1)

manager1.show_employ()