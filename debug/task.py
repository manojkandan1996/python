# Category 1
# Task 1
# def greet(name) 
# print("Hello, " + name) 
def greet(name):
    print("Hello, " + name)
# Task 2
# if x = 10: 
# print(x)
if x == 10:
    print(x)
# Task 3
# list = [1, 2, 3 
# print(list) 
my_list = [1, 2, 3]
print(my_list)
# Task 4
# print "Hello World" 
print("Hello World")
# Task 5
# for i in range(5) 
# print(i)
for i in range(5):
    print(i)
# Task 6
# def add(a, b): 
# return a + b 
def add(a, b):
    return a + b
# Task 7
# name = input('Enter name: ') 
# print('Hello, ' + name) 
name = input('Enter name: ') 
print('Hello, ' + name)
# Task 8
# my_dict = {'a': 1, 'b': 2, 'c': 3 
# print(my_dict['b']) 
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])
# Task 9
# a = 5 
# b = '5' 
# print(a + b) 
a = 5 
b = '5' 
print(a + int(b)) 
# Task 10
# def func(x, y=2, z): 
# return x + y + z 
def func(x, z, y=2):
    return x + y + z
# Category 2
# Task 11
# def is_even(n): 
# return n % 2 == 1 
def is_even(n): 
    return n % 2 == 0
# Task 12
# def factorial(n): 
# result = 1 
# for i in range(n): 
# result *= i 
# return result 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Task 13
# def reverse_list(lst): 
# return lst.sort()
def reverse_list(lst):
    return list(reversed(lst))
# Task 14
# def find_max(numbers): 
#     max = 0 
#     for n in numbers: 
#         if n > max: 
#             max = n 
#     return max 
def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val
# Task 15
# def average(numbers): 
#  return sum(numbers) / len(numbers) if numbers != None else 0 
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
# Task 16
# for i in range(10): 
#     if i == 5: 
#         break 
#     else: 
#         continue 
#     print(i)
for i in range(10): 
    if i == 5: 
        break 
    print(i)
# Task 17
# a = [1, 2, 3] 
#  b = a 
#  b.append(4) 
#  print(a)
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# Task 18
# x = 5 
# def change(): 
#     x = 10 
# change() 
# print(x) 
x = 5
def change():
    global x
    x = 10
change()
print(x)
# Task 19
# nums = [10, 20, 30, 40] 
# print(nums.index(100)) 
nums = [10, 20, 30, 40]
try:
    print(nums.index(100))
except ValueError:
    print("100 is not in the list")
# Task 20
# a = 0.1 + 0.2 
# print(a == 0.3) 
import math
a = 0.1 + 0.2
print(math.isclose(a, 0.3))
# Category 3
# Task 21
# print(1 / 0) 
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
# Task 22
# try: 
# my_list[5] 
# except: 
# print('An error occurred') 
my_list = [1, 2,]
try:
    print(my_list[5])
except IndexError:
    print('Index out of range')
# Task 23
# def divide(a, b): 
# try: 
# return a / b 
# except ZeroDivisionError: 
# return "Can't divide by zero" 
# finally: 
# return "Done"
def divide(a, b): 
    try: 
        return a / b 
    except ZeroDivisionError: 
        return "Can't divide by zero" 
    finally: 
        print("Finished  division")
# Task 24
# d = {'x': 1, 'y': 2} 
# print(d['z']) 
d = {'x': 1, 'y': 2}
print(d.get('z', 'Key not found'))
# Task 25
# f = open('file.txt') 
# print(f.read()) 
try:
    with open('file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("file.txt not found")
# Task 26
# import math 
# print(math.sqrt(-1))
import cmath
print(cmath.sqrt(-1))
# Task 27
# a = [1, 2, 3] 
# print(a[3])
a = [1, 2, 3]
try:
    print(a[3])
except IndexError:
    print("Index out of range")
# Task 28
# s = 'hello' 
# print(int(s)) 
s = 'hello'
try:
    print(int(s))
except ValueError:
    print("Cannot convert to integer")
# Task 29
# from datetime import datetime 
# print(datetime.now().strftime('%Y-%m-%d %h:%m:%s')) 
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# Task 30
# nt_list = list(map(int, ['1', '2', 'three', '4'])) 
input_list = ['1', '2', 'three', '4']
int_list = []

for item in input_list:
    try:
        int_list.append(int(item))
    except ValueError:
        print(f"Skipping invalid item: {item}")

print(int_list)
# Category 4
# Task 31
# def increment(n): 
# n += 1 
# increment(5) 
# print(n) 
def increment(n): 
    n += 1
    return n

n = increment(5)
print(n)
# Task 32
# counter = 0 
# def increase(): 
# global counter 
# counter += 1 
# increase() 
# print(counter) 
def increase(counter):
    return counter + 1

counter = 0
counter = increase(counter)
print(counter)
# Task 33
# def append_item(item, lst=[]): 
# lst.append(item) 
# return lst 
def append_item(item, lst=None): 
    if lst is None:
        lst = []
    lst.append(item) 
    return lst
# Task 34
# def greet(name, greeting='Hello'): 
# return greeting + name 
# print(greet('John', greeting='Hi', 'Mr.')) 
def greet(name, greeting='Hello'): 
    return greeting + ' ' + name

print(greet('Mr. John', greeting='Hi')) 
# Task 35
# x = 10 
# def outer(): 
# x = 20 
# def inner(): 
# print(x) 
# inner() 
# outer() 
x = 10
def outer():
    x = 20 
    def inner():
        print(x)  
    inner()

outer()
# Task 36
# def modify_list(lst): 
# lst = lst + [1] 
# my_list = [0] 
# modify_list(my_list) 
# print(my_list) 
def modify_list(lst):
    lst.append(1)

my_list = [0]
modify_list(my_list)
print(my_list) 
# Task 37
# def test(): 
# return 
# print('unreachable') 
def test():
    print('reachable')
    return

test()
# Task 38
# a = [1, 2, 3] 
# for i in a: 
# a.remove(i) 
# print(a) 
a = [1, 2, 3]
for i in a[:]:  
    a.remove(i)
print(a) 
# Task 39
# def multiply(a, b): 
# return a * b 
# print(multiply(2)) 
def multiply(a, b=1):
    return a * b

print(multiply(2))      
print(multiply(2, 3))
# Task 40
# def square(x): 
# print(x ** 2) 
# result = square(4) 
# print(result)
def square(x):
    return x ** 2

result = square(4)
print(result) 
# Category 5
# Task 41
# my_set = set([1, 2, 3]) 
# print(my_set[0]) 
my_set = set([1, 2, 3])
print(list(my_set)[0]) 
# Task 42
# my_dict = {'a': 1, 'b': 2} 
# print(my_dict.get('c', 'No key')) 
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c', 'No key'))
# Task 43
# nums = [1, 2, 3, 4, 5] 
# for i in range(len(nums)): 
# print(nums[i + 1]) 
nums = [1, 2, 3, 4, 5]
for i in range(len(nums) - 1):
    print(nums[i + 1])
# Task 44
# i = 0 
# while i < 5: 
# print(i) 
i = 0
while i < 5:
    print(i)
    i += 1
# Task 45
# my_tuple = (1) 
# print(type(my_tuple))
my_tuple = (1,)
print(type(my_tuple)) 
# Task 46
# def merge_dicts(d1, d2): 
# return d1.update(d2) 
def merge_dicts(d1, d2):
    d1.update(d2)
    return d1
# Task 47
# for i in range(3): 
# print(i) 
# else: 
# break 
for i in range(3):
    print(i)
    if i == 1:
        break
# Task 48
# items = ['apple', 'banana', 'cherry'] 
# for i in range(len(items)): 
# print(items[i + 1]) 
items = ['apple', 'banana', 'cherry']
for i in range(len(items) - 1):
    print(items[i + 1])
# Task 49
# a = [1, 2, 3] 
# print(a.pop(3)) 
a = [1, 2, 3]
print(a.pop(2))
# Task 50
# def foo(): 
# try: 
# return 1 
# finally: 
# return 2 
# print(foo()) 
def foo():
    try:
        return 1
    finally:
        return 2

print(foo())
