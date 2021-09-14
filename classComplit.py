class Employee:
    pay_rising = 0.1
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail=first+'.'+last+'@aa.com'
        __init__ = 10
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def pay_inc (self):
        self.pay += int (self.pay * self.pay_rising)            
    #overriding
    def __add__(self,other):
        return self.pay + other.pay
    def __sub__(self,other):
        return self.pay - other.pay
    def __len__(self):
        return len(self.fullname())
    def __repr__(self):
        return __class__.__name__+ "('{}','{}',{} )".format(self.first,self.last,self.pay)                    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.mail)        

class Developer (Employee):
    def __init__(self, first,last,pay,prog_lag):
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lag

class Manager(Employee):            
    def __init__(self, first,last,pay,empoees = None):
        Employee.__init__(self,first,last,pay)
        if empoees is None:
            self.empoees = []
        else:
            self.empoees = empoees 
    def add_emp (self,emp):
        if emp not in self.empoees:
            self.empoees.append(emp)  
    def remove_emp(self,emp):
        if emp in self.empoees:
            self.empoees.remove(emp) 
    def print_emp(self):
        for empcount in self.empoees:
            print("--",empcount.fullname())

dev1 = Developer ("reza","asghari",1000,"java")
dev2 = Developer ("mehdi","ghomi",1000,"java")
dev3 = Developer ("hassan","omidi",1000,"go")
emp1 = Employee("reza","asghari",1000)
emp2 = Employee("reza","asghari",5000)
mng1 = Manager ("mm","ashjaei", 9000, [dev1])
# print(mng1.mail)
# mng1.add_emp(dev2)
# mng1.add_emp(dev3)
# mng1.print_emp()
 #overriding
print(dev1+dev2)
print(len(dev1))
print(emp1)
print(repr(dev1))



        
