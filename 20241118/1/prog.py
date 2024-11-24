from collections import UserString

class DivStr(UserString):
    def __init__(self, s = None):
        if s is None:
            super().__init__('')
        else:
            super().__init__(s)

    def __floordiv__(self, n):
        step = len(self) // n
        return (self.__class__(self.data[i:i + step]) for i in range(0, len(self), step))

    def __mod__(self, n):
        return self.__class__(self.data[-(len(self) % n):]) if len(self) % n else self.__class__()

import sys

exec(sys.stdin.read())
