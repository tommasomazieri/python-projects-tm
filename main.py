"""
CODE FOR: BEGINNER LEVEL PYTHON COURSE
"""
# 0) BASIC DATA TYPES
"""
int -> 5, -3, 0 ...
str -> "stuff", 'foo1' ...
bool -> True & False
float -> 1.3, -2.4, .5 ...
"""
# 1) VARIABLES
"""
name = 'Tommaso'
print(name)

a variable cannot start with a number, contain - or * or other ambiguous symbols

Variables are not case-insensitive:
NAME != name 
"""
# 2) BASIC OPERATORS & INPUT
"""
print('hello, what is your name?')
name = input()
print('hello,', name)

operators -> +, -, *, /
can be used only in certain data types:
num1 = 45
num2 = 3
print(num1 + num2)

other operators:
    exponent -> **
    integer division -> // -> 64/10 = 6.4; 64//10 = 6
    modulus -> % -> 5 % 2 = 1 (4 with remainder of 1)
    
print('pick a number: ')
num1 = input()
print('pick another number: ')
num2 = input()
SUM_str = num1 + num2  # gives a string, so sums the strings. to get number, convert input to number!
num1 = int(num1)
num2 = int(num2)
SUM_int = num1 + num2
print(SUM_int)

comparison operators: <, >, ==, !=, <=, >=
18 > 2 True
2 == 3 False  # as using = is a declaration, not a condition of equivalence
also: 'hello' != 'hello' False  # works with strings as well
"""
# 3) CONDITIONS
"""
print(2 < 3) -> True
print('hello' == 'helo') -> False
"""
# 4) IF, ELIF, ELSE
"""
if condition is True: -> x == y; stat is False...
----do thing  # 4 indents needed!

age = int(input('input your age: '))
if age >= 16:  # python firstly checks the first condition, if not met...
    print('you are older than 16!')
else:  # ... will go to the next
    print('you are younger than 16!')
    
height = float(input('how tall are you: '))
if height < 1:
    print('you cannot ride, under 1 meters')
elif height > 2:
    print('you cannot ride, over 2 meters')
else:
    print('you can ride!')    
"""
# 5) CHAINED CONDITIONALS AND NESTED STATEMENTS
"""
examples of chained conditions are:
x = 2
y = 3
if y == x and x + y == 5:  # &
    print('True')
else:
    print(':(')
if y == x or x + y == 5:  # |
    print('True')
# but also:
if not(y == x and x + y == 5):  # &
    print('True')

now, for the nested statements, we may have something like:
if x == 2:
    if y == 3:
        print('x == 2 and y == 3')
    else:
        print('x == 2, y != 3')
else:
    print('x != 2')
"""
# 6) FOR LOOPS
"""
for x in range(0, 10, 1):  # range parameters: start, stop, step
    print(x)
"""
# 7) WHILE LOOPS
"""
while condition == True:
    do this
    
for example:
loop = True
while loop:
    name = input('insert something: ')
    if name == 'stop':
        break  # or, set: loop = False
"""
# 8) LISTS AND TUPLES
"""
lists:
fruits = ['apple', 'pear', 3]
print(fruits)
# to access an individual item in the list:
print(fruits[1])
fruits.append('banana')  # add sto the end of the list given item
print(fruits)
# to change a given item in a list:
fruits[1] = 'strawberry'
print(fruits)

tuples:
position = (2, 3)  # works best for coordinate data!
"""
# 9) ITERATION BY ITEM
"""
fruits = ['apples', 'pears', 'strawberries']
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')
"""
# 10) STRING METHODS
"""
# .strip(), len(), .lower(), .upper(), .split(), ...
text = input('input something: ')
print(text)
print(text.strip())  # removes spaces
print(len(text))  # number of characters in string
print(text.lower())  # turns all characters to lower case
print(text.upper())  # turns all characters to upper case
print(text.split())  # creates a list out of the string, inside, define the delimiter of separation
# for more methods, look to documentation on python website...
"""


