import math  # importing math module

print('Hello World')
print("*" * 10)

x = 1
y = 2
unit_price = 3

# Variables - numbers, booleans and strings
student_count = 1000  # integer
rating = 4.99  # float
is_published = True  # boolean
course_name = "Python Programming"  # string
message = """Hey guys
Im Spencer
Thanks for coming to my TED talk
"""  # triple quotes for very long strings
print(student_count)
print(message)
print(len(course_name))  # finding length of a string
print(course_name[0])  # print first element in a string
print(course_name[-1])  # print last element in a string
print(course_name[0:6])  # print first 6 elements in a string
print(course_name[0:])  # prints the whole string
print(course_name[:3])  # prints the first 3 elements in a string
print(course_name[:])  # prints the whole string

name = "John \"Tricky"  # using escape sequence to add extra quotation marks
[print(name)]
"""escape sequence -
    \" - adding double quotes
    \' - adding single quotes
    \\ - adding a backslash
    \n -moving to the next line"""

first = "Spencer"
last = "Ofwiti"
full = first + " " + last  # string concatenation
names = f"{first} {last}"
print(full)
print(names)
trial = f"{len(first)} {3 + 4}"
print(trial)

example = "  How it is done "
print(example.upper())  # converts string to upper case
print(example.lower())  # converts string to lower case
print(example.title())  # converts first letter of each word to upper case
# removes all whitespace at the beginning or end of a string
print(example.strip())
print(example.find("it"))  # find index of certain elements in a string
print(example.replace("it is", "its"))  # replace certain elements in a string
print("it" in example)  # determine if a certain element is in a string
# determine if certain elements are not in a string
print("swift" not in example)

x = 1 + 2j  # a + bi - complex number
print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # produces a float
print(10 // 3)  # produces an integer
print(10 % 3)  # remainder
print(10 ** 3)  # exponent - to the power of
# Augmented assignment operators
x += 3  # Increment operator
x -= 3  # decrement operator
x *= 3  # multiplication operator
x /= 3  # division operator

print(round(2.9))  # rounds off to the nearest integer
print(abs(-2.9))  # returns absolute value of a number

print(math.ceil(2.2))  # return ceiling of a number or round upwards

z = input("Z : ")
print(type(z))  # show type of variable
v = int(z) + 1
print(f"Z : {z}, V : {v}")

# Type conversions
# int(z) to int
# float(z) to float
# bool(z) to boolean
# str(z) to string

# Falsy values
# "" empty strings
# 0 number zero
# None
print(bool(0))  # False
print(bool(1))  # True
print(bool(-3))  # True
print(bool(""))  # False
print(bool("False"))  # True

# Comparison operators
# > - greater than
# >= - greater than or equal to
# < - less than
# <= - less than or equal to
# == - equal to
# != - not equal to

# Conditional statements
temperature = 25
if temperature > 30:
    print("It is warm")
    print("Drink water")
elif temperature > 20:
    print("It is nice")
else:
    print("It is cold")
print("Done")

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"  # ternary operator
print(message)

# Logical operators
# AND - both are true for it to be true
# OR - either has to be true for it to be true
# NOT - if false becomes true

high_income = False
good_credit = True
student = False

# either has a high income or good credit and is not a student
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

if 18 <= age < 65:
    print("Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

for number in range(1, 10, 2):  # Range 1 to 10 taking steps of 2
    print("Attempt", number, number * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:  # prints when it doesn't break from the loop
    print("Attempted three times and failed")

for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

# iterable eg range , strings and lists
for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

count = 0
for number in range(1, 10):
    while number % 2 == 0:
        count += 1
        print(number)
        break
print(f"We have {count} even numbers")


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Spencer", "Ofwiti")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Spencer")
file = open("content.txt", "w")
file.write(message)


def increment(number, by=1):  # optional parameter
    return number + by


print(increment(2))
print(increment(2, 3))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="John", age=22)

message = "a"  # global variable


def new(name):
    message = name  # local variable
    print(message)

new("Spencer")
print(message)  # prints global variable

x, y = 1, 2  # Initializing two variables in the same line
print(x)
print(y)

age:
    int = 15  # type annotation
print(id(age))  # memory location of variable age

age = age + 1  # reassign a new memory location
print(id(age))  # memory location of variable age

age.append(4)  # added to the same memory location
print(id(age))  # memory location of variable age
