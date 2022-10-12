# create a class Triangle , with 3 properties and two methods

class Triangle:
    def __int__(self,base,height,hyp):
        self.base = base
        self.height = height
        self.hyp = hyp

    def area(self):
        area = 1/2 *(self.base * self.height)
        print(area)

    # def perimeter(self):
    #     perimeter =

triangle1 = Triangle(23,12)

triangle1.area()