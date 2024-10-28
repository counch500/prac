from itertools import count

def fun():
        sum = 0
        for n in count(1):
                sum += 1/(n**2)
                yield sum
