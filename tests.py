from unittest import TestCase
from code import TestClass
import pytest
import allure
from allure.constants import Severity


#: mixins
class FooTestCaseMixin(object):
    @allure.story('check foo')
    def test_foo(self):
        self.assertEqual(bool(self.foo), True)


@allure.feature('Call')
class TestCall(FooTestCaseMixin, TestCase):
    foo = ''

    def setUp(self):
        self.instance = TestClass(10)

    @allure.story('foo')
    @allure.severity(Severity.NORMAL)
    def test_my_foo(self):
        allure.attach('foo', 'my foo')
        with allure.step('step one'):
            self.assertEqual(self.instance.foo, 10)
        with allure.step('step two'):
            self.assertEqual(self.instance.foo2(), self.instance.foo)

    @allure.story('foo foo')
    @allure.step('one')
    def test_foo_foo(self):
        self.assertEqual(True, True)

    @allure.step('one')
    @allure.story('failed test')
    def test_fail(self):
        self.assertEqual(False, True)


@allure.feature('Another Call')
class TestAnotherCall(FooTestCaseMixin, TestCase):
    foo = 'something'

    @allure.story('the foo')
    def test_the_foo(self):
        self.assertEqual(self.foo, 'something')


@allure.feature('Finall Call')
class TestFinallCall(FooTestCaseMixin, TestCase):
    foo = True


class ApplyMixinsMeta(type):
    """
    Metaclass that cuts test_* methods from given mixins and bind them towards
    main class directly. It helps to make BDD tests for each feature unique by
    each test case class
    """
    def __new__(mcs, name, bases, cls_dict):
        new_cls = type.__new__(mcs, name, bases, cls_dict)
        if hasattr(new_cls, 'Meta'):
            new_cls._meta = {
                'mixins': (
                    hasattr(new_cls.Meta, 'mixins')
                    and getattr(new_cls.Meta, 'mixins') or []
                )
            }

            #: copy existent mixins
            mixins = []
            for mixin in new_cls._meta['mixins']:
                new_mixin = type.__new__(
                    mixin.__class__, mixin.__name__ + '_%s' % name,
                    mixin.__bases__, dict(mixin.__dict__)
                )
                mixins.append(new_mixin)
            new_cls._meta['mixins'] = mixins

            for mixin in new_cls._meta['mixins']:
                tests = filter(
                    lambda x: callable(getattr(mixin, x)) and 'test_' in x,
                    dir(mixin)
                )
                for test in tests:
                    unbound_method = getattr(mixin, test).im_func
                    setattr(new_cls, test, unbound_method)
                    delattr(mixin, test)
            new_cls.__bases__ = (new_cls.__base__, ) + tuple(
                new_cls._meta['mixins']
            )
        return new_cls


class TestCaseExtended(TestCase):
    __metaclass__ = ApplyMixinsMeta


@allure.feature('Call Extended')
class TestCallExtended(TestCaseExtended):
    foo = True

    class Meta:
        mixins = (FooTestCaseMixin, )

    @allure.story('check extended')
    def test_extended(self):
        self.assertTrue(isinstance(self, TestCaseExtended))


@allure.feature("Another extended")
class AnotherTestCallExtended(TestCaseExtended):
    foo = 'not false'

    class Meta:
        mixins = (FooTestCaseMixin, )


@allure.feature("Failed extended")
class TestCallFailedExtended(TestCaseExtended):
    foo = False

    class Meta:
        mixins = (FooTestCaseMixin, )
