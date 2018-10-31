class Cube:
    x = 1

    def __init__(self, x):
        self.x = x

    def rotate(self):
        self.x = self.x + 1
        return self

    def __str__(self):
        return 'Cube with x: ' + str(self.x)


class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx, dy, dz):
        self.x -= dx
        self.y -= dy
        self.z -= dz


print(Cube(1).rotate())
