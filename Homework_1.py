#A

first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

#B

a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a, b, c)

#C

name = 'john'
name = "john"
### no difference between the two

my_number = 5+5
print("result is: " + str(my_number))


#D

x = 5
y = 2.36
print(x + int(y))
### output will be 7, casting float to int will cause it to ignore the numbers after .

#E

X = 5
Y = 10
if X > Y:
    print("BIG")
elif X < Y:
    print("small")

#F

seasons = input("enter a number from 1-4:\n")
if seasons == 1:
    print("summer")
elif seasons == 2:
    print("winter")
elif seasons == 3:
    print("fall")
elif seasons == 4:
    print("spring")
else:
    print("invalid")

#CHALLENGE

a = 8
b = "123"

print(a, b)

