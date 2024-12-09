class Doubleton(type):
    _instances = []
    _idx = -1
    def __call__(cls, *args, **kw):
        if len(cls._instances) < 2:
             cls._instances.append(super().__call__(*args, **kw))
        cls._idx += 1
        return cls._instances[cls._idx % 2]
class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")
