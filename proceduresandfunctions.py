# #QA Community:

# def grade_calc(homework, assessment, exam):
#     grade_per = round(((homework + assessment + exam)/ 175) * 100,2)
#     return grade_per

# name = input("Enter name: ")
# homework = int(input("Enter homework mark: "))
# assessment = int(input("Enter assessment mark: "))
# exam = int(input("Enter exam mark: "))

# grade = grade_calc(homework, assessment, exam)

# if grade >= 80:
#     grade_let = 'A'
# elif grade >= 70:
#     grade_let = 'B'
# elif grade >= 60:
#     grade_let = 'C'
# elif grade >= 50:
#     grade_let = 'D'
# else:
#     grade_let = 'F'

# print(f"{name}: {grade}% - {grade_let}")

#w3resources:

#1)
# def max3nums(num1, num2, num3):
#     return(max(num1, num2, num3))

# num1 = 3
# num2 = 600
# num3 = 156

# print(max3nums(num1, num2, num3))

#2)
# def sumnumlist(list_nums):
#     total = 0
#     for i in list_nums:
#         total += i
#     return(total)

# list_nums = (8, 2, 3, 0, 7)

# print(sumnumlist(list_nums))

#3)
# def multinumlist(list_nums):
#     total = 1
#     for i in list_nums:
#         total *= i
#     return(total)

# list_nums = (8, 2, 3, -1, 7)

# print(multinumlist(list_nums))

#4)
# def reverse(string):
#     revStr = string[::-1]
#     return(revStr)

# print(reverse("1234abcd"))

#5)
# def factorial(num):
#     total = 1
#     for i in range(1,num+1):
#         total *= i
#     return(total)

# print(factorial(5))