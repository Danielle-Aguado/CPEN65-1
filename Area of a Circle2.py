class Circle:
    def __init__(self, PI, r, d):
        self.PI = PI
        self.r = r
        self.d = d

    def Area(self):
        print("The area of the circle using radius is", self.PI * self.r ** 2)

    def Area2(self):
        print("The area of the circle using diameter is", (self.PI / 4) * self.d ** 2)


c = Circle(3.14, 4, 8)
c.Area()
c.Area2()