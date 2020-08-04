class A():
    rate=4
    @classmethod
    def set_variable(cls):
        cls.rate=5

a=A()
print(a.rate)
b=A()
b.set_variable()
print(b.rate)
c=A()
print(b.rate)
