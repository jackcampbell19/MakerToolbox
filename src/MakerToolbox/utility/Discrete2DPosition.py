
class Discrete2DPosition:
    """
    XY integer position.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Discrete2DPosition'):
        return Discrete2DPosition(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Discrete2DPosition'):
        return Discrete2DPosition(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Discrete2DPosition'):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))
