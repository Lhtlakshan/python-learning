a = 20
b = 2.25
c = "lakshan"
d = False

# data types
print(type(a)) # int
print(type(b)) # float
print(type(c)) # str
print(type(d)) # bool

print("a + b = ", a + b)   # addition
print("a - b = ", a - b)   # subtraction
print("a * b = ", a * b)   # multiplication
print("a / b = ", a / b)   # division (float result)
print("a // b = ", a // b)  # floor division (whole number)
print("a % b = ", a % b)   # remainder
print("a ** b = ", a ** b)  # power (10^3)


# name = input("Enter your name ")
# print("Hello", name)
#
# num1 = int(input("Enter no 1 : "))
# num2 = int(input("Enter no 2 : "))
#
# print("Sum of : ", num1+num2)


# uses f-string for more easier
age = 25
school = "St. Servatius College"

print(f"My school is {school}. My age is {age}")

# Swap two variables without a third variable.
x = 25
y = 30

x = x+y
y = x-y
x = x-y

print ("X :", x , "and Y :", y )