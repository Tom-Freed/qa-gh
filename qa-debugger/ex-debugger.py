# #1)
# user_funds = 10.31
# item_price = price["Burger"] # price not defined i.e. no list called price

# if item_price < user_funds:
#     Print("You have enough money!") # lower case p
# if item_price = user_funds: # ==
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print(Sorry you don't have enough money) # need double quotes 
          
# #2)
# def product(n):
#     total == 1
#     for n in n: # using same variable name, first n should be 'i'
#         total *= i 
# return total

# print(product([4,4,5]))

# #3)
# import pdb
# pdb.set_trace()

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x): # x-1 to x
#             if (x % n) == 0: # '=' to '==', add brackets to x % n
#                 return False
#         return True # remove 1 indention level

# nums = 2, 3, 4, 5, 6, 7, 15, 20, 25

# for i in nums:
#     print(is_prime(i))

#4)
# import pdb
# pdb.set_trace()
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i) # remove item_list
    n += 1 # increment n by 1

print (item_list[4]) # add brackets, indicies start at 0 (change 5 to 4)