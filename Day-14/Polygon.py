# Goal: “Create class and sub-class objects which represent different geometrical shapes, 
# such as Rectangles and Squares” objects should have methods to display area and perimeter

class Shape:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def sq_rect(self):
        if self.length == self.width:
            return "square"
        else:
            return "rectangle"
    
    def area(self):
        print(f"The area of this {self.sq_rect()} is {self.length * self.width}")
    
    def perimeter(self):
        print(f"The perimeter of this {self.sq_rect()} is {(self.length * 2) + (self.width * 2)}")
    
a = Shape(5,5)
a.area()
a.perimeter()

b = Shape(5,10)
b.area()
b.perimeter()
