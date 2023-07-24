#Exercise
class Student:
    '''
    Creates Student class with init and avg_test functions
    '''
    def __init__(self, name: str, age: str, stu_class: str="student") -> None:
        '''
        Initalises the object setting the parameters
        '''
        self.name = name
        self.age = age
        self.stu_class = stu_class

    def avg_test(self, mark1: int, mark2: int, mark3: int) -> float:
        '''
        Returns a float of the avg of the 3 tests
        '''
        return (mark1 + mark2 + mark3)/3


if __name__ == '__main__':
    Bob = Student('Bob', '25')
    print(Bob.name, Bob.age, Bob.stu_class)
    print(f"{Bob.name}'s average test result {Bob.avg_test(60, 90, 30)}")