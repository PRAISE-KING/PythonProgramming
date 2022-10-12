# square

class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(area)

    def pr(self):
        pr = 2 * (self.width + self.height)
        print(pr)

square1 = Square(10, 10)
# square1.width = 10
# square1.height = 10

square1.area()
square1.pr()
