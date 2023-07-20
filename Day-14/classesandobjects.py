#Exercise
class Student:

    def __init__(self, name, age, stu_class="student"):
        self.name = name
        self.age = age
        self.stu_class = stu_class

    def avg_test(self,mark1, mark2, mark3):
        print((mark1 + mark2 + mark3)/3)

Bob = Student('Bob', '25')

print(Bob.age, Bob.stu_class)

Bob.avg_test(60, 90, 27)


