"""
CODE FOR: BEGINNER LEVEL PYTHON COURSE
"""
# 0) BASIC DATA TYPES
import math

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
# 11) SLICE OPERATOR
"""
fruits = ['apples', 'pears', 'strawberries']
text = 'Hello I like python'
start = 0
stop = None  # to go all the way, if code doesn't always goes down
step = 2
print(text[start:stop:step])
# to insert elements, instead of append, which adds to the end of a list the given element, use:
place = 1
fruits[place:place] = 'b'
print(fruits)
"""
# 12) FUNCTIONS
"""
def do_something(some_parameters):
    return something
# and then, call function:
do_something(param)  # here, the function executes its code...
you can set function to a variable, or print it, or just execute it, depending on what the function does
"""
# 13) READ TEXT FILES
"""
file = open('file', 'r')
f = file.readlines()  # list of elements in file. separated by \n character
new_list = []
for line in f:
    if line[-1] == '\n':
        new_list.append(line[:-1])  # here, we remove \n character on all elements having it
    else:
        new_list.append(line)
# or, in a shorter and cleaner way:
new_list = []
for line in f:
    new_list.append(line.strip())  # or: new_list.append(line.replace('\n', ''))
print(new_list)
"""
# 14) WRITING TO A TEXT FILE
"""
file = open('file', 'w')
file.write('python\neasy\nnibbas')  # this will replace content of given file with whatever you provide
file.close()  # saves file changes
"""
# 15) USING .count() AND .find()
"""
# .find(), .count()
string = input('please type something')
# string.find('h'): if you place a character not in string, returns -1. Returns first place character is found
# string.count(''): counts how many times a character/s is repeated
if string.count('_') > 0:  # or if string.find('_') != -1
    print('not good')
else:
    print('good')
"""
# 16) INTRO TO MODULAR PROGRAMMING
"""
import math
import myModule

print(math.radians(60))
print(myModule.my_func(6))
"""
# 17) OPTIONAL PARAMETERS
"""
def func(x, text):
    print(x)
    if text == '1':
        print('text is 1')
    else:
        print('text is not 1')


func('hello', '1')

# now, make default values instead
def func(x, text='2'):
    print(x)
    if text == '1':
        print('text is 1')
    else:
        print('text is not 1')


func('hello', text='1')
"""
# 18) TRY AND EXCEPT
"""
# use it when you need to do something, but do not know if it is going to work...
text = input('username: ')
try:
    number = int(text)
    print(number)
except:
    print('invalid username')
"""
# 19) GLOBAL VS LOCAL VARIABLES
"""
var = 9  # this variables are global on the script
loop = True


def func(x):
    newVar = 7  # this variable is local of the function
    print(var)
    if x == 5:
        return newVar


func(5)
# you do not want to be dependent on global variables in your functions tho...
# also, if wue modify a global variable in a function...
def func(x):
    newVar = 7
    var = 0
    if x == 5:
        return newVar
# ... it will not be modified globally, but just inside the function itself:
func(5)
print(var) == 9


# to apply changes globally, use global keyword:
def func(x):
    global var
    newVar = 7
    var = 0
    if x == 5:
        return newVar
"""
# 20) CLASSES AND OBJECTS
"""
# object: any variable is an object, which have particular attributes
x = 'string'
y = 23
# z = x + y returns TypeError: can only concatenate str (not "int") to str

# class:
class Number:
    def __init__(self, num_):  # initialization function
        self.var = num_

    def display(self, x):
        print(x)


num = Number(23)
num.display(num.var)
"""
"module 2: classes and objects"
# 2) CREATING CLASSES
"""
class Dog(object):
    def __init__(self, name, age):
        self.name = name  # an attribute of the class
        self.age = age

    def speak(self):  # a method of the class
        print(f'hi, I am {self.name} and I am {self.age} years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tim = Dog('Tim', 5)
fred = Dog('Fred', 3)
tim.change_age(6)
tim.speak()
fred.speak()
tim.add_weight(70)

print(tim.name)
print(tim.weight)
print(fred.weight)  # it wont work as we have not yet defined it
"""
# 3) INHERITANCE
"""
class Cat(object):  # copies from class Dog and adds some stuff
    def __init__(self, name, age, color):
        self.name = name  # an attribute of the class
        self.age = age
        self.color = color

    def speak(self):  # a method of the class
        print(f'hi, I am {self.name} and I am {self.age} years old')
# a better way to do this is:
#        parent
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.name = 'Tech'  # overrides name attribute of parent

    def talk(self):
        print('Meow!')


tim = Cat('Tim', 5, 'red')
tim.speak()  # it inherit all the methods of the parent
tim.talk()  # overrides the parent method of talk


class Vehicle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep Beep')


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('Honk Honk')
"""
# 4) OVERRIDING METHODS
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coord = (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        import math  # to import only when needed (?)
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, point):  # __add__ is in function of python, here, we modify it
        return Point(self.x + point.x, self.y + point.y)
    # same for __sub__, __mul__ ...

    def __mul__(self, point):
        return self.x * point.x + self.y * point.y

    def __str__(self):  # used to show some meaningful value instead of coordinates of memory when printing
        return "{" + str(self.x) + "," + str(self.y) + "}"  # it has to return a string!!!

    def __gt__(self, point):  # compares which of the objects is greater given certain criteria
        return self.length() > point.length()

    def __ge__(self, point):  # greater or equal to
        return self.length() >= point.length()

    def __le__(self, point):  # less or equal to
        return self.length() <= point.length()

    def __eq__(self, point):  # equal to
        return self.length() == point.length()


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

p5 = p1 + p2  # will crush for now, we need to work on code, adding: def __add__(self, point)
p6 = p3 * p4  # not a point anymore, but a scalar
p7 = p2 <= p3
print(p5)  # returns object
print(p6)  # returns scalar
print(p7)  # returns bool
"""
# 5) STATIC METHODS AND CLASS METHODS
"""
class Dog:
    dogs = []  # class variable. Is useful for variables that you use statically for each instance of a class

    def __init__(self, name):
        self.name = name  # an attribute of the class
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):  # here, tho, you cannot call self methods!
        for _ in range(n):
            print('Bark!')


tim = Dog('Tim')
jim = Dog('Jim')
print(Dog.dogs)
# but also:
print(jim.dogs)

print(tim.num_dogs())

# now, staticmethod:
Dog.bark(2)  # no need to instantiate the class
# but also:
tim.bark(3)
"""
# 6) PRIVATE AND PUBLIC CLASSES
"""
# you can still use private classes and methods, it is just a convention to do so to inform other coders
class _Private:  # cannot be accessed outside the script
    # the underscore signals that we intend the class to be private
    def __init__(self, name):
        self.name = name


class NotPrivate:  # can be accessed outside the script
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        # underscore represent private method
        print('hello')

    def display(self):
        print('hi')


test = NotPrivate('tim')
test.display()
# you may also do:
test._display()  # but it will be underlined as protected member of a class
"""
"module 3: intermediate level"
# 1) OPTIONAL PARAMETERS
"""
def func(x, y=1):
    return x ** 2 / y


call = func(5, y=2)
print(call)
"""
# 2) MORE ON CLASS METHOD
"""
class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population
    
    @classmethod
    def add_to_pop(cls, amt):
        cls.population += amt

    def display(self):
        print(self.name, 'is', self.age, 'years old')


new_person1 = Person('tim', 18)
new_person2 = Person('jim', 20)
new_person2.add_to_pop(10)

print(Person.get_population())
print(new_person1.get_population())
"""
# 3) map() FUNCTION
"""
# is used to apply a function to a list and return a new list with the results
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(x):
    return x**x

# you may do as follows:
new_list = []
for i in li:
    new_list.append(func(i))
# but a better way would be:
new_list = list(map(func, li))  
# just shortcut, shouldn't improve performances that much
# you may also shorten code using a list comprehension:
new_list = [func(x) for x in li]
# which allows for more flexibility, as you can use if statements in it:
new_list = [func(x) for x in li if x > 2]
"""
# 4) filter() FUNCTION
"""
def add7(x):
    return x + 7


def is_odd(x):
    return x % 2 != 0


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = list(filter(is_odd, a))
print(b)
c = list(map(add7, b))
print(c)
"""
# 5) LAMBDA FUNCTIONS
"""
# anonymous functions, so funcs that are not defined directly
# you may want too apply it for very short and basic function to save space in code
def func(x):
    return x + 5

func2 = lambda x: x + 5  # useful for map and other builtin functions
print(func(2))
print(func2(9))

def func3(x):
    # useful when having functions inside of functions, instead of having to define them outside
    func4 = lambda x: x + 5
    return func4(x) + 85

print(func3(2))

a = [1,2,3,4,5,6,7,8,9]

# sums 5 to each element in list:
new_list = list(map(lambda x: x + 5, a))
print(new_list)
"""
# 6) COLLECTIONS/Counter()
"""
# containers:
#   list
#   set
#   dict
#   tuple - immutable
# Types:
#   counter <- this session
#   deque
#   namedTuple()
#   orderedDict
#   defaultDict

import collections
from collections import Counter

c = Counter('gallad')
d = Counter(['a', 'a', 'b', 'c', 'c'])
e = Counter({'a': 1, 'b': 2})
f = Counter(cats=4, dogs=5)
print(c)  # splits string and counts each character repetitions  
print(d)  # is its own specific object
print(e['c'])  # key not in keys doesn't return error
print(f['cats'])  # shows specific key

print(list(f.elements()))  # shows each element in counter object in its amount
print(c.most_common(2))  # shows the n most common elements

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']  # can use any other counter object, not only list
c.subtract(d)  # subtracts the counts form similar argument
print(c)
c.update(d)  # adds the counts
print(c)
c.clear()  # removes all the counts
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c+d)  # returns added values removes <= 0 ones
print(c-d)  # if an element count is <= 0 is going to be removed

print(c & d)  # intersection of the counters (so showing only common elements > 0
print(c | d)  # shows all > 0 elements in both counters, on their max amount

"""
# 7) COLLECTIONS/namedtuple()
"""
# useful when writing large files
from collections import namedtuple

point1 = namedtuple('Point', 'x y z')  # can also pass: ['x', 'y', 'z'] and other iterable
newP = point1(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)  # access each element, not doable in tuples
print(newP[0])

newP = newP._replace(y=6)
print(newP)

p2 = point1._make(['a', 'b', 'c'])  # replaces all values of keys with arguments in iterable
print(p2)
"""
# 8) COLLECTIONS/deque()  called 'deck'
"""
# useful as is faster to add elements at the beginning and end of a list
d = deque('hello')
print(d)
d.append('4')  # adds argument to the end of the list
print(d)
d.appendleft('5')  # adds argument to the beginning of the list
print(d)
d.pop()  # removes last element in iterable, popleft removes the first one
# d.clear()  # clears the iterable

d.extend('456')  # adds the new iterable at the end of the existing one
print(d)

d = deque('hello', maxlen=5)
print(d)
d.append(1)
print(d)  # h is removed to maintain the max amount of 5 elements
"""




