class A(object):
    def __init__(self, a, b=10, *arg):
        self.a = a
        self.b = b

        if len(arg) > 2:
            self.arg = list(arg)
        else:
            self.arg = arg

a = A(3, 7, 3, 5, "Hello")
aa = A(3, 7, 3, 5)
print a.a
print a.b
print type(aa.arg)
print type(a.arg)
