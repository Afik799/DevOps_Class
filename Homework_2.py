# #A
#
# X = 4
# Y = 5
# if X > Y:
#     print("BIG")
# elif Y > X:
#     print("small")
#
# #B
#
# for x in range(1, 6):
#     print(x)
#
# #C
#
# num = 2
# if num == 1:
#     print("summer")
# elif num == 2:
#     print("winter")
# elif num == 3:
#     print("fall")
# elif num == 4:
#     print("spring")
#
# #D
#
# count = 1
# while count < 11:
#     print(count)
#     count += 1
#
# ## the loop will run 10 times since count is starting from 1 and ends on 10, at 11 the loop breaks
#
# #E
#
# my_age = 25
# FirstLetter = "N"
# dollar = 3.35
# Flew = True
# AptNum = 8
#
# print(my_age, FirstLetter, dollar, Flew, AptNum)
# print(dollar + my_age)
#
# #F
#
# x = int(input("Enter your phone number please: \n"))
# print("Phone number is: " + str(x))
#
# #G
#
# def printHello():
#     print("hello")
# def calculate():
#     print(5+3.2)
#
# printHello()
# calculate()

# H

# def Name(name):
#     print(name)
#
# def Number(x):
#     print(x / 2)
#
# Name("afik")
# Number(4)

# I

# def Sum(x, y):
#     return x + y
#
# def String(str1, str2):
#     return str1 + " " + str2
#
# print(Sum(1, 2))
# print(String("afik", "navaro"))


# J

# new_array = [1, 2, 4]
# for x in new_array:
#     print(x)

# K
#
# my_list = []
# while len(my_list) < 5:
#     my_list.append(int(input("Enter a number: ")))
#
# print("Summerizing it... \n Sum is: " + str(sum(my_list)))

# L

# my_dict = {"first": "afik", "last": "Navaro", "address": "Tel Aviv", "age": 25}
# for x in my_dict.keys():
#     print(x)

# CHALLENGES

# M

# for x in range(1, 6):
#      for y in range(1):
#         print(x * "#")

{}
# N

tag = "#"
width = 7
lenght = 0
for x in range(1, 8):
    x = tag
    space = " "
    for y in range(1):
        y = tag
        j = space * lenght
        z = space * width
        print(j + y + z + tag)
        width = width - 3
        lenght = lenght + 1



# O

# def get_num():
#     x = int(input("Enter a number please: "))
#     listing = []
#     for y in str(x):
#         listing.append(y)
#     return listing
#
#
# def sum(y):
#     count = 0
#     # y = get_num()
#     for x in y:
#         x = int(x)
#         count = count + x
#     return count


# print(sum(get_num()))

# I am sure there alot of ways to do it, not sure if mine is the best.
# in the first function, I am converting the number to list
# in the second function I am adding up the indexes of the list
# This can also be done with the line that is commented out, but the varilable from the second func need to be removed


#P

# new_tup = (1, 4, "a", 5.7)
# string = ""
# for x in new_tup:
#     string = string + str(x)
# print(string)

#Q

# my_list = [200, 5, 7, 10]
# print(min(my_list))




