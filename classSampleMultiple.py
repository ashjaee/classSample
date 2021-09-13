class A:
    def rpt_func(self,no1):
        print("class A")

class B:
    def rpt_func(self,no1,no2):
        print("class B")

class C(A,B):
    def rpt_func(self,no1,no2,no3):
        print("class C")

c = C()
c.rpt_func(20,20,20)
print(help(c))