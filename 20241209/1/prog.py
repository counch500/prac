class dump(type):
    def __new__(cls, name, bases, attrs):
        def wrapper(func):
            @functools.wraps(func) # Важно для сохранения имени функции
            def wrapped(self, *args, **kwargs):
                print(f"{func.__name__}: {args}, {kwargs}")
                return func(self, *args, **kwargs)
            return wrapped

        new_attrs = {}
        for name, attr in attrs.items():
            if callable(attr):
                new_attrs[name] = wrapper(attr)
            else:
                new_attrs[name] = attr
        return super().__new__(cls, name, bases, new_attrs)

import functools

class C(metaclass=dump):
    def __init__(self, val):
        self.val = val
    def add(self, other, another=None):
        return self.val + other + (another or self.val)
import sys
exec(sys.stdin.read())

