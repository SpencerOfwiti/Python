import mymodule as mx
import platform
from mymodule import person1
import datetime
import json
import re  # Regular expressions
import camelcase
import os

print("Hey there")
if(5 > 2):
    print("Five is greater than Two")
# This is a comment
"""This is a
multiline docstring"""
# Variables do not need to be of any particular type
x = 5
y = "John"
print(x, y)
print("Your name is " + y)
a = "Python is "
b = "awesome"
c = a + b
print(c)
# + is used to combine a text and a variable or a variable and another variable
# for numbers + works as a mathematical operator

# Numeric types in Python
x = 1  # int - whole number positive or negative without decimal
y = 2.8  # float - number positive or negative containing one or more decimals
# or with an exponent to indicate to the power 10"""
z = 3 + 5j  # complex - numbers written with a j as the imaginary part
print(type(x))  # type() function is used to show type of an object in python
print(type(y))
print(type(z))

# Type casting
k = int(2.8)  # k will be 2
l = float(3)  # l will be 3.0
m = str(3.0)  # m will be "3.0"

s = "Hello, World!"
print(s[1])  # Print character at index 1
print(s[2:5])  # Print characters from index 2 to 5
print(s.strip())  # Removes any whitespace at the beginning or end
print(len(s))  # Returns length of string
print(s.lower())  # Returns the string in lower case
print(s.upper())  # Return string in upper case
print(s.replace("H", "J"))  # Replaces string with another string
print(s.split(","))  # Splits the string into substrings

print("Enter your name: ")
n = input()  # Command line input
print("Hello " + n)

# Arithmetic operators:
# + - addition,
# - - subtraction, * - multiplication,
# / - division,
# % - modulus, ** - Exponentiation, // - Floor division

# Assignment operators:
# x = 5 - equating
# x += 3 same as x = x + 3
# x -+ 3 same as x = x - 3
# x *= 3 same as x = x * 3
# x /= 3 same as x = x / 3
# x %= 3 same as x = x % 3
# x //= 3 same as x = x // 3
# x **= 3 same as x = x ** 3
# x &= 3 same as x = x & 3
# x |= 3 same as x = x | 3
# x ^= 3 same as x = x ^ 3
# x >>= 3 same as x = x >> 3
# x <<= 3 same as x = x << 3

# Comparison operators:
#  == - equal to, != - not equal to,
#  > - greater than,
#  < - less than,
#  >= - greater than or equal to,
#  <= - les than or equal to

# Logical operators:
#  AND - true if both are true,
#  OR - false if both are false,
#  NOT - true if it was initially false

# identity operator:
#  is -true if both variables are the same object,
#  is not - true if both objects are not the same

# Membership operators:
# in - True if a sequence with the specified value is present in the object,
# not in - True if a sequence with the specified value is not present in object

# Bitwise operators: & - Sets each bit to 1 if both bits are 1,
# | - Sets each bit to 1 if one of two bits is 1
# ^ - Sets each bit to 1 if only one of two bits is 1
# ~ - Inverts all the bits
# << - Shift left pushing zeros in from the right letting leftmost bits fall
#  off
# >> - Shift right by pushing copies of the leftmost bit in from the left, and
#  let the rightmost bits fall off

# List is a collection which is ordered and changeable. Allows duplicate
#  members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate
#  members.
# Set is a collection which is unordered and un-indexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed.
#  No duplicate members.

# LISTS
thislist = ["apple", "banana", "cherry"]  # creating a list
print(thislist)
print(thislist[1])  # item in index 1
thislist[1] = "blackcurrant"  # change value at a certain index
print(thislist)
for x in thislist:  # iterate through list
    print(x)
if "apple" in thislist:  # determine if an item is present in the list
    print("Yes, 'Apple' is in the fruit list")
print(len(thislist))  # return length of list
thislist.append("orange")  # add item to the end of the list
print(thislist)
thislist.insert(1, "banana")  # add an item at a specified index
print(thislist)
thislist.remove("orange")  # remove an item from the list
print(thislist)
thislist.pop()  # removes specified index or last index if not indexed
print(thislist)
del thislist[0]  # removes a specified index
print(thislist)
thislist.clear()  # empties the list
print(thislist)
del thislist  # deletes list completely
# print(thislist) will show an error

# You can use a list() constructor to make a list
newlist = list(("Me", "You"))
print(newlist)

# List methods:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the
#  current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# TUPLES
thistuple = ("apple", "banana", "cherry")  # creating a tuple
print(thistuple)
print(thistuple[1])  # Returns item in index 1
# Values in a tuple are unchangeable they cant be added or removed
for x in thistuple:  # looping through tuple items
    print(x)
if "apple" in thistuple:  # determine if an item is present in the tuple
    print("Yes, 'Apple' is in the fruit list")
print(len(thistuple))  # return length of tuple

# You can use a tuple() constructor to make a list
newtuple = tuple(("Me", "You"))
print(newtuple)

# Tuple methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of
#  where it was found

# SETS
thisset = {"apple", "banana", "cherries"}  # create a set
print(thisset)
# sets have no index
for x in thisset:  # will be output in no definite order
    print(x)
print("banana" in thisset)  # check if there is an item banana in the set
thisset.add("orange")  # adding an item to the set
print(thisset)
thisset.update(["mango", "grapes"])  # adding multiple items in a set
print(thisset)
print(len(thisset))  # return length of set
thisset.remove("banana")  # remove an item from the set
print(thisset)
thisset.discard("grapes")  # remove an item from the set
print(thisset)
thisset.pop()  # removes a random item
print(thisset)
thisset.clear()  # empties the set
print(thisset)
del thisset  # delete the whole set

# You can use a set() constructor to make a list
newset = set(("Me", "You"))
print(newset)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["model"])  # accessing items in a dictionary
print(thisdict.get("year"))  # accessing using get() method
thisdict["year"] = 2018  # changing the value of a specific item
print(thisdict)

for x in thisdict:
    print(x)  # prints key names
    print(thisdict[x])  # prints values

for x in thisdict.values():  # return values
    print(x)

for x, y in thisdict.items():  # return both keys and values
    print(x, y)

d = 250
e = 200
f = 300
if e > f and f > d:
    print("e is greater than d")
elif e < f and d > f:
    print("d is greater than e")
elif d > f or d > e:
    print("d is greater than one")
else:
    print("e is equal to f")

print("E") if e > f else print("F")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # stop the loop
    i += 1

j = 10
while j > 6:
    j -= 1
    if j == 8:
        continue  # continues to the next iteration
    print(j)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break  # stops loop
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "apple":
        continue  # skips apple
    print(x)

for x in range(2, 30, 3):  # values 2 to 30 (not including 30)incrementing by 3
    print(x)
else:
    print("Finally finished`")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


def myFunction(name="there"):  # default parameter
    print("Hello " + name + " from this function")

myFunction("Lubia")
myFunction()


def square(x):
    return x * x

print(square(3))

# Recursion example


def tri_recursion(k):
    if(k > 0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\n Recursion Example Results")
tri_recursion(6)

# lambda - small anonymous function
# x = lambda a: a + 10
# print(x(5))


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(5))
print(mytripler(4))

cars = ["Ford", "Volvo", "BMW"]  # Array
cars[0] = "Toyota"  # Adding an item to the array
print(len(cars))  # return size of array
cars.append("Honda")  # adding items to an array
cars.pop(1)  # removing items from an array
cars.remove("BMW")  # removing an item from an array
for x in cars:
    print(x)

# Array methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the
#  current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


class MyClass:  # creating a class called MyClass
    x = 5  # a property of the class named x

p1 = MyClass()  # creating an object called p1
print(p1.x)  # printing value of x from p1


class Person:
    def __init__(self, name, age):
        # using __init__() function to assign values for name and age
        self.name = name
        self.age = age

    def myfunc(self):  # defining a function in the class
        print("Hello my name is " + self.name)

# self is a reference to the class instance itself used to access variables belonging to the class
# it can be called anything but has to be the first parameter of any function
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

p1.age = 40  # modifying properties on objects
print(p1.age)

del p1.age  # deleting properties on objects
del p1  # deleting objects

# an iterator implements the iterator protocol which consists of the methods __iter__() and __next__()
# iterable object have an iter() method used to get an iterator
mytuple = ("Apple", "Banana", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystring = "Banana"
myit = iter(mystring)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# to create an object or a class as an iterator you have to implement the __iter__() and __next__() methods to your object


class MyNumbers:  # returns numbers starting with 1 and increasing by one
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Stopping the iteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)


# import mymodule as mx - should be at the top of the page

mx.greeting("Max")

a = mx.person1["age"]
print(a)

x = platform.system()
y = dir(platform)  # list all function names in a module
print(x)
print(y)
print(person1["age"])  # using imported dictionary from mymodule

z = datetime.datetime.now()  # display current date
print(z)
print(z.year)
print(z.strftime("%A"))  # method for formatting date objects into readable strings
# takes one parameter to specify the format of the returned string

f = datetime.datetime(2020, 5, 17)  # creating a date object
print(f)

# Format codes for time
# %a 	Weekday, short version 	Wed
# %A 	Weekday, full version 	Wednesday
# %w 	Weekday as a number 0-6, 0 is Sunday 	3
# %d 	Day of month 01-31 	31
# %b 	Month name, short version 	Dec
# %B 	Month name, full version 	December
# %m 	Month as a number 01-12 	12
# %y 	Year, short version, without century 	18
# %Y 	Year, full version 	2018
# %H 	Hour 00-23 	17
# %I 	Hour 00-12 	05
# %p 	AM/PM 	PM
# %M 	Minute 00-59 	41
# %S 	Second 00-59 	08
# %f 	Microsecond 000000-999999 	548513
# %z 	UTC offset 	+0100
# %Z 	Timezone 	CST
# %j 	Day number of year 001-366 	365
# %U 	Week number of year, Sunday as the first day of week, 00-53 	52
# %W 	Week number of year, Monday as the first day of week, 00-53 	52
# %c 	Local version of date and time 	Mon Dec 31 17:41:00 2018
# %x 	Local version of date 	12/31/18
# %X 	Local version of time 	17:41:00
# %% 	A % character 	%

# Converting json to python
x = '{"name" : "John", "age" : 30, "city" : "New York"}'  # some JSON
y = json.loads(x)  # parse x
print(y["age"])

# Converting python to json
x = {  # a python object
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)  # convert into JSON
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Python toJSON equivalents
# dict 	Object
# list 	Array
# tuple 	Array
# str 	String
# int 	Number
# float 	Number
# True 	true
# False 	false
# None 	null

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))
# adding indents, separators and order

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # search if it starts with the and ends with spain

# Functions in re
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	Replaces one or many matches with a string

# Metacharacters
# [] 	A set of characters 	"[a-m]" 	
# \ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
# . 	Any character (except newline character) 	"he..o" 	
# ^ 	Starts with 	"^hello" 	
# $ 	Ends with 	"world$" 	
# * 	Zero or more occurrences 	"aix*" 	
# + 	One or more occurrences 	"aix+" 	
# {} 	Excactly the specified number of occurrences 	"al{2}" 	
# | 	Either or 	"falls|stays" 	
# () 	Capture and group

# Special sequences
# \A 	Returns a match if the specified characters are at the beginning of the string 	"\AThe" 	
# \b 	Returns a match where the specified characters are at the beginning or at the end of a word 	r"\bain" r"ain\b" 	

# \B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word 	r"\Bain" r"ain\B" 	

# \d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d" 	
# \D 	Returns a match where the string DOES NOT contain digits 	"\D" 	
# \s 	Returns a match where the string contains a white space character 	"\s" 	
# \S 	Returns a match where the string DOES NOT contain a white space character 	"\S" 	
# \w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w" 	
# \W 	Returns a match where the string DOES NOT contain any word characters 	"\W" 	
# \Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z"

# Sets
# [arn] 	Returns a match where one of the specified characters (a, r, or n) are present 	
# [a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
# [^arn] 	Returns a match for any character EXCEPT a, r, and n 	
# [0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
# [0-9] 	Returns a match for any digit between 0 and 9 	
# [0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
# [a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
# [+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
x = re.findall("portugal", str)
print(x)
x = re.search("\s", str)
print("The first white-space character is located in position:" ,x.start())
x = re.search("Portugal", str)
print(x)
x =re.split("\s", str)  #returns list where string has been split at every match
print(x)
x =re.split("\s", str, 1)  #Asplit at first occurences
print(x)
x = re.sub("\s", "9", str)  #substitute splits with 9
print(x)
x = re.sub("\s", "9", str, 2)  #substitute splits with 9
print(x)
x = re.search("ai", str)
print(x)  #returns match object

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

x =re.search(r"\bS\w+", str)  #words that start with uppercase s
print(x.span())
print(x.string)
print(x.group())

c = camelcase.CamelCase()
txt = "hello world!"
print(c.hump(txt))

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(q)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else: 
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

try:
  q = open("demofile.txt")
  q.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")

#File handling
#Modes for opening a file 
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt", "x")  # creates a file
f = open("demofile.txt", "w")  # open for writing
f.write("Hello! Welcome to demofile.txt ")  # overwrites content
f = open("demofile.txt", "a")  # open file for appending
f.write("This file is for testing purposes. ")  # adds content at the end
f.write("Good Luck! ")
f = open("demofile.txt", "rt")  # open for reading with text mode. These are default and dont ned to be written.
print(f.read())  # read contents of a file
print(f.read(5))  # read first 5 characters of a file
print(f.readline())  # return one line
print(f.readline())  # return second line
for x in f:
    # read whole file line by line
    print(x)

os.remove("demofile.txt")  # deletes a file
if os.path.exists("demofile.txt"):  # chacks if file exists
    os.remove("demofile.txt")  # deletes a file
else:
    print("File does not exist")

# os.rmdir("myfolder") - delete a folder