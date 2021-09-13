class A:
    def rpt_func(self):
        print("class A")

class B:
    def rpt_func(self):
        print("class B")

class C(A,B):
    def rpt_func(self):
        print("class C")

class D(C,B):
    pass
    # def rpt_func(self):
    #     print("class D")

d1 = D()
d1.rpt_func()

