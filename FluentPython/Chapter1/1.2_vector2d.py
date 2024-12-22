"""
Vector class 를 생성해 곱하기, 복소수 크기, 더하기 를 수행

# add
v1 = Vector(2, 4)
v2 = Vector(2, 1)

v1 + v2 = Vector(4, 5)

# abs
(|z| = root(x^2 + y^2))
v = Vector(3, 4)
abs(v) = 5.0

# Scalar
v * 3 = Vector(9, 12)
abs(v * 3) = 15.0


"""


import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        """
        해당 메서드가 없을 경우 <Vector object 0x0000> 으로 출력된다.

        """
        return f'Vector({self.x!r}, {self.y!r})'
        # !r 은 repr 특별 메서드를 호출하겠다는 의미다.
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
