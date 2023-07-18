# input_mark = int(input("Enter mark: "))
# if input_mark > 85:
#     print("Distinction")
# elif input_mark >= 65 and input_mark <= 85:
#     print("Pass")
# else:
#     print("Fail")

# if input_mark > 85:
#     print("Distinction")
# if input_mark >= 65 and input_mark <= 85:
#     print("Pass")
# if input_mark < 65:
#     print("Fail")

# QA Community:

# count = 0
# while count < 5:
#     name = str(input("Enter name: "))
#     print(f"{name} is awesome")
#     count += 1

# # Starting at 10 will step up 2 each time stopping at 21, i.e. 20
# for i in range(10, 21, 2):
#     print(i)

# w3resource:

# 1)
# numbers = []
# for num in range (1500, 2701):
#     if num%7 == 0 and num%5 == 0:
#         numbers.append(num)
# print(numbers)

#2)
# scale = input("Select scale (C/F): ")
# temp = int(input("Enter number of degrees: "))

# if scale.upper() == 'C':
#     result = int(round((9 * temp) / 5 + 32))
#     print(f"{result}F")
# elif scale.upper() == 'F':
#     result = int(round((temp - 32) * 5 / 9))
#     print(f"{result}C")
# else:
#     print("Please enter in correct format")

#3)
# import random

# rand_num = random.randint(1,9)
# guess = 0
# while guess != rand_num:
#     guess = int(input("Guess the num, between 1 and 9: "))
# print ("Well guessed!")

#5)
# user_word = input("Enter a word: ")
# print(user_word[::-1])

#6)
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# odd = 0
# even = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"Number of even numbers: {even}, number of odd numbers {odd}")