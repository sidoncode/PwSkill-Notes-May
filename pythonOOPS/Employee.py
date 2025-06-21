class Employee:
    def __init__(self,name,salary):
        #public Variable
        self.name = name

        #private Variable
        self.__salary = salary

        #protected Variable
        self._department = "IT"

    def get_salary(self):
        return self.__salary

    def setter_salary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid Salary")

emp1 = Employee("Alice",5000) # creating a object of Employee class
print(emp1.name) # name is pub -> working... (accessable from anywhere!)
# print(emp1.__salary) #not working.. -> Private (accessble only from self Class)
emp1.setter_salary(5001)
print(emp1.get_salary())
print(emp1._department)# working.. -> procted( access from objects)

# how to access Private Varible??
# >> getters and setter
# >> getters will get the value from the private Variable
# >> setter will set the value to the private Variable  
