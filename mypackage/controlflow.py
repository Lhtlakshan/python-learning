# # if else elif
#
# num = 10
#
# if num > 20:
#     print("Num is greater than 20")
# elif num > 15:
#     print("Num is greater than 15")
# else:
#     print("Num is less than 15")
#
#
# # logical operators usage
# x = 10
# y = 5
#
# if x > 5 and y < 10:
#     print("Both conditions are True")
#
# if x > 5 or y > 10:
#     print("At least one condition is True")
#
# if not x > 20:
#     print("x is not greater than 20")
#
#
# # Loop from 0 to 4
# for i in range(5):
#     print(i)
#
# # Loop over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# while num > 0:
#     print(num)
#     num -= 1
#
#
# # break
# for i in range(10):
#     if i == 5:
#         break  # stop the loop
#     print(i)
#
# # continue
# for i in range(5):
#     if i == 2:
#         continue  # skip this iteration
#     print(i)
#
# # pass
# for i in range(3):
#     pass  # do nothing, placeholder


# exersice
# print all numbers divisible by 3
for i in range(1, 51):
    if i % 3 == 0:
        print(i)

# Ask the user for a number and print if it is positive, negative, or zero.

num = int(input("Enter the number"))

if num > 0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Password checker: keep asking the user to enter the password until it matches "Python123"

while True:
    password = input("Enter your password")
    if password == "Python123":
        print("Password is correct")
        break
    else:
        print("Try again")


# Print all items in a list except one specific item using continue.
names = ["saman", "kamal", "nimal"]

for i in names:
    if i == "kamal":
        continue
    print(i)
