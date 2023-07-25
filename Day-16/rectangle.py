class Rectangle:

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        
    def __int__(self):
        return self.calc_area()
    
    def __add__(self, rect2):
        return Rectangle((self.height + rect2.height), (self.width + rect2.width))
    
    def __str__(self):
        return ('* ' * self.width + '\n') + (('* ' + ('  ' * (self.width - 2)) + '*' + '\n') * (self.height-2)) + ('* ' * self.width)
    
    def calc_area(self):
        return self.height * self.width
    

if __name__ == '__main__':
    a = Rectangle(5,2)
    print(int(a))
    print(a)
    b = Rectangle(10,4)
    print(int(b))
    print(b)
    c = a + b
    print(int(c))
    print(c)