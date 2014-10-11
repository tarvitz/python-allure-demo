# coding: utf-8


class TestClass(object):
    """class for test cases on allure test framework"""

    def __init__(self, foo):
        self.foo = foo

    def foo(self, foo):
        print(foo)
        return foo

    def foo2(self):
        print("foo: ", self.foo)
        return self.foo

    def __repr__(self):
        return "<TestClass instance>"


if __name__ == '__main__':
    pass
