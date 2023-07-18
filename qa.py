input_mark = int(input("Enter mark: "))
if input_mark > 85:
    print("Distinction")
elif input_mark >= 65 and input_mark <= 85:
    print("Pass")
else:
    print("Fail")

if input_mark > 85:
    print("Distinction")
if input_mark >= 65 and input_mark <= 85:
    print("Pass")
if input_mark < 65:
    print("Fail")