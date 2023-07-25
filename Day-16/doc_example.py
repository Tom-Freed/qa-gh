class Example():
    '''
    Example of docstring for a class
    '''
    def __init__(self) -> None:
        pass

    def factorial(x: int) -> int:
        '''
        Returns the product of all of the integers from 1 to x inclusive
        <add any enviroment inforation as well>
        '''
        result = 1
        for i in range (2, x + 1):
            result *= i
        return result

if __name__ == '__main__':
    print(factorial(3))
    print(factorial(5))
    print(factorial(10))