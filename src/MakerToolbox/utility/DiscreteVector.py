from math import sqrt


class DiscreteVector:
    """
    Discrete vector consisting of 3 integers.
    """

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other: 'DiscreteVector'):
        return DiscreteVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: 'DiscreteVector'):
        return DiscreteVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar: float):
        return DiscreteVector(round(float(self.x) * scalar), round(float(self.y) * scalar), round(float(self.z) * scalar))

    def __eq__(self, other: 'DiscreteVector'):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
