class A:
    def rpt_func(self):
        print("class A")

class B:
    def rpt_func(self):
        print("class B")

class C(A,B):
    def rpt_func(self):
        print("class C")

c = C()
print(c.rpt_func())
