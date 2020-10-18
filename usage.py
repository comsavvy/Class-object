import itertools as it
import functools as ft
from operator import add

__all__ = ['Usage']


class Usage:
    def __init__(self, first: int = 0, second: int = 0):
        self.__slot__ = ['first', 'second']
        self.first = first
        self.second = second
        self.__all__ = ['add']

    @staticmethod
    def sum(self: object, *others: object) -> object:
        result = Usage()
        if isinstance(self, (list, tuple)):
            for i in self:
                result += i
        else:
            result = self
        if isinstance(others, Usage):
            return result + others
        else:
            for i in others:
                if isinstance(i, (list, tuple)):
                    for j in i:
                        result += j
                else:
                    result += i
        return result

    def add(self, *other):
        current = Usage(self.first, self.second)
        return self.sum(current, other)

    def __add__(self, other):
        # Different ways of addition
        # added = add(self.first, other.first), add(self.second, other.second)
        # added = (add(a, b) for a, b in [(self.first, other.first), (self.second, other.second)])
        # added = (sum(i) for i in zip([self.first, self.second], [other.first, other.second]))

        added = self.first + other.first, self.second + other.second
        return Usage(*added)

    def __mul__(self, other):
        if isinstance(other, Usage):
            m = self.first * other.first, self.second * other.second
        elif isinstance(other, (int, float)):
            m = self.first * other, self.second * other
        elif isinstance(other, (tuple, set)):
            if len(other) > 2:
                raise TypeError(f'{type(other)} must be two dimension')
            m = self.first * other[0], self.second * other[1]
        else:
            raise ValueError(f'Operation on {type(other)} cannot be done!')
        return Usage(*m)

    def __lt__(self, other):
        return (self.first + self.second) < (other.first + other.second)

    def __gt__(self, other):
        return (self.first + self.second) > (other.first + other.second)

    def __le__(self, other):
        return (self.first + self.second) <= (other.first + other.second)

    def __ge__(self, other):
        return (self.first + self.second) >= (other.first + other.second)

    def __ne__(self, other):
        return (self.first + self.second) != (other.first + other.second)

    def __eq__(self, other):
        return (self.first + self.second) == (other.first + other.second)

    def __str__(self):
        form = f'{self.__class__.__name__}(first={self.first}, second={self.second})'
        return form

    def __repr__(self):
        form = f'{self.__class__.__name__}(first={self.first}, second={self.second})'
        return form


if __name__ == '__main__':
    a = Usage(89, 90)
    b = Usage(21, 102)
    print(a,  b)
    d = [Usage(i, j) for i, j in enumerate(range(1, 21), start=1)]
    print(Usage.sum(d))
    print(Usage.sum(d, b, a, b))
    print(Usage.sum(a, b, b))
    print(Usage.sum([a, b], b))
    print(a + b)
    print(a.add(b))
