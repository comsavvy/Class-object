from operator import add

__all__ = ['Usage', 'sum']


def sum(*iterable):
    total = Usage()
    for i in iter(iterable):
        total += i
    return total


class Usage:
    def __init__(self, first: int = 0, second: int = 0):
        self.__slot__ = ['first', 'second']
        self.first = first
        self.second = second
        self.__all__ = ['add', 'sum']

    @staticmethod
    def sum(self: object, *others: object) -> object:
        result = Usage()
        if isinstance(self, (list, tuple)):
            if isinstance(self[0], (int, float)):
                result += self
            else:
                for i in self:
                    result += i
        else:
            result = self
        for i in others:
            if isinstance(i, Usage):
                result += i
            elif isinstance(i, (tuple, list)):
                if isinstance(i[0], Usage):
                    for j in i:
                        result += j
                else:
                    result += i
        return result

    def add(self, *other):
        current = Usage(self.first, self.second)
        return self.sum(current, *other)

    def _test(self, other, one=None):
        if one is None:
            if len(other) > 2 or len(other) < 2:
                raise TypeError(f'{type(other)} must be two dimension')
        else:
            raise ValueError(f'Operation on {type(other)} cannot be done!')

    def __add__(self, other):
        # Different ways of addition
        # added = add(self.first, other.first), add(self.second, other.second)
        # added = (add(a, b) for a, b in [(self.first, other.first), (self.second, other.second)])
        # added = (sum(i) for i in zip([self.first, self.second], [other.first, other.second]))
        if isinstance(other, Usage):
            added = self.first + other.first, self.second + other.second
        elif isinstance(other, (tuple, list)):
            self._test(other)
            added = self.first + other[0], self.second + other[1]
        else:
            self._test(other, one=bool)
        return Usage(*added)

    def __sub__(self, other):
        """
        Making the instance of Usage accept subtraction
        """
        if isinstance(other, Usage):
            added = self.first - other.first, self.second - other.second
        elif isinstance(other, (tuple, list)):
            self._test(other)
            added = self.first - other[0], self.second - other[1]
        else:
            self._test(other, one=bool)
        return Usage(*added)

    def __round__(self, n=None):
        return Usage(round(self.first, n), round(self.second, n))

    def __mul__(self, other):
        if isinstance(other, Usage):
            m = self.first * other.first, self.second * other.second
        elif isinstance(other, (int, float)):
            m = self.first * other, self.second * other
        elif isinstance(other, (tuple, list)):
            self._test(other)
            m = self.first * other[0], self.second * other[1]
        else:
            self._test(other, one=bool)
        return Usage(*m)

    def __truediv__(self, other):
        if isinstance(other, Usage):
            added = self.first / other.first, self.second / other.second
        elif isinstance(other, (tuple, list)):
            self._test(other)
            added = self.first / other[0], self.second / other[1]
        else:
            self._test(other, one=bool)
        return Usage(*added)

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

    def __iter__(self):
        """
        This will allow class Usage to be iterable
        """
        return iter([self.first, self.second])

    def __str__(self):
        form = f'{self.__class__.__name__}(first={self.first}, second={self.second})'
        return form

    def __repr__(self):
        form = f'{self.__class__.__name__}(first={self.first}, second={self.second})'
        return form
