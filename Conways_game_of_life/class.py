class Employee: 
    # pass - dersom klassen er helt tom
    num_of_emps=0 
    raise_amount=1.04 # klasse variabel

    def __init__(self, first, last, pay): # konstruktør
        self.first=first
        self.last=last
        self.pay=pay
        self.mail=first + "_" + last + "@email.com"
        Employee.num_of_emps+=1


    # def full_name(self): # klasse funksjon
    #     return "{} {}".format(self.first, self.last)

    @property
    def email(self): # klasse funksjon
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def full_name(self): # klasse funksjon
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last=name.split("")
        self.first=first
        self.last=last

    @full_name.deleter
    def full_name(self):
        self.first=None
        self.last=None
        print("Deleted name")

    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amount) # kan også bruke self.raise_amount
   
    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount=amt

    def __repr__(self): # object representation, debuger or loging, used by developers 
        # should have this if we use __str__ 
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    # def __str__(self): # readable representation of an object for the user
    #     return "{} - {}".format(self.full_name(), self.mail)
    
    # def __add__(self, other):
    #     return self.pay+other.pay

    # def __len__(self):
    #     return len(self.full_name())



# emp_1=Employee()
# emp_1.first="John"
# emp_1.last="Smith"
# emp_1.mail="John_smith@email.com"
# emp_1.pay=50000

# print(emp_1.first)


emp_1=Employee("John", "Smith", 50000)
# print(emp_1.mail)

# print(emp_1.full_name())



# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)



# Employee.raise_amount=1.05
# emp_1.raise_amount=1.05
# print(emp_1.__dict__)
# print(Employee.__dict__)


# print(Employee.num_of_emps)


# class methods - 
    # @classmethod
    # def set_raise_amt(cls, amt):
        # cls.raise_amount=amt

# static methods - 
    # @staticmethod
    # def is_workday(day):
    #     if day=weekday:
    #         return 0
    #     else:
    #         return 1

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)

class Developer(Employee): # klassen Developer arvet fra Employee
    raise_amount=1.10 

    def __init__(self, first, last, pay, prog_lang): 
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang

        # Employee.__init__(self, first, last, pay)

emp_2=Developer("John", "Smith", 50000, "Python")

# print(emp_2.prog_lang)


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): 
        super().__init__(first, last, pay)

        if employees==None:
            self.employees=[]
        else:
            self.employees=employees

    
    def add_emp(self, employee): 
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee): 
        if employee  in self.employees:
            self.employees.remove(employee)

    def print_emps(self):
        for emp in self.employees:
            print("-->" + emp.full_name())


mng=Manager("John F.", "Kennedy", 100000, [emp_1, emp_2])
# mng.print_emps()
# print(mng.mail)

# print(isinstance(mng, Manager))
# print(issubclass(Developer,Employee))


# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1+emp_2)
# print(len(emp_2))