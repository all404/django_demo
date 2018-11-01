class O1(object):
    def foo(self):
        print('到了O1')


class O2(object):
    def foo(self):
        print('到了O2')


class Fu1(O1):
    def foo(self):
        print('到了Fu1')
        super().foo()


class Fu2(O2):
    def foo(self):
        print('到了Fu2')
        super().foo()


class Demo(Fu1, Fu2):
    def foo(self):
        print('到了Demo')
        super().foo()


if __name__ == '__main__':
    demo = Demo()
    demo.foo()
    print(Demo.__mro__)
