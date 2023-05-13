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
# 4 IF, ELIF, ELSE
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

