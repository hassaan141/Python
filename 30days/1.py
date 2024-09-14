# 1-3. Built in functions

# len(): Gives length of a string/list
# type(): Gives the data type
# str(): Converts the number to a String 
# int(): To int

# Variable Names

# Cannot have -, $, @, &. Only can have _

# Variables

# list []: a list of things, can be different datatypes are are mutable
# tuple (): A set of data, different types, immputable/fixed
# set {}: No repeating things,
# dict {}: Have a name and defination

# print(type([1, 2, 3, 4]))     # list
# print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
# print(type((1,2)))                                              # tuple
# print(type(zip([1,2],[3,4])))    

#####################################################
# 4. String and Splicing

# Strings on multiple lines, use triple quotes
# spaces count as letters

# String interpolation
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')

#Unpacking characters in string to get each individual characters
# language = 'Python'
# a,b,c,d,e,f = language

# Can get the index of the of a String 
# language = 'Python'
# print(language[0]) will print P

# To get the last index do print(language[-1]), for 2nd last print(language[-2])

# to splice a string, do language[0:3], will give the first 3 letters

# to get from a certain index to the end is language[3:]

# flipping a string is: greetings[::-1]

# language.count('a') gives all the occurences of 

# find give the first occurence of that things index

# isalnum() sees if the string follows alphanumeric casing, spaces do not count as alpha numeric

#converting from array to string 
  #final = ' ' +join(arr)

# string = 'Thirty', 'Days', 'Of', 'Python'
# con = ' '.join(string)
# print(con)
# print(con.upper())
# print(con.lower())


# print(con.index('Thirty'))
# print(con.replace('Python', 'Seed'))
# print(con.split('y'))
# print(con[10])
# print(con.find('t'))

###########################################################
# 5. LISTS

# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10

# To check if an item exists within a list, do 
#   if banana in lists

# to remove from a list, .remove("apple")
#adding to the end of a list, is append
#insert is inserting in a specific position in a list
#pop removes a specific index or the last one in a list
#You can remove the last one ir 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)       

# newFruits = fruits
# print (newFruits)
# fruits[0]= 'new'

# print(newFruits)

#### When assinging one list to another, its pass by refernce and they share the same memory address, so change in one is also present in the other
### When copying, you assign the new list a new memory address

# sort an array is array.sort()
# reverse sort is array.sort(reverse=True)

#############################################################

# 6-7. Tuples and Sets
# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[0]
# second_fruit = fruits[]
# print(second_fruit)

# Can change a tuple to a list by using list function

#   new_list = list(tupleName)

# Can change it back to a tuple by using the tuple using the tuple function

#   new_tuple = tuple(listName)9

# To see if something is common to both sets, use intersects

# To check if something isnt common to both sets, use differece()
  # difference()

###########################################################

# 8. Dictionaries

# dict = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dict['key1']) 
# print(dict['key4']) 

# # To add a new key and value pair to a dict, do, can also change items this way
# dict['key5'] = 'value'

# # to print out onlu that values can do 

# keys = dict.keys()
# print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# values = dict.values()
# print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

#####################################################################

# 10. While and For loops

# When iterating a list

# numbers = [1,2,3,4,5]
# words = 'Python'

# for i in numbers:
#   print(i)

# When iterating over a dictionary, use .items()

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# # for key in person:
# #     print(key)
# # for value in person:
# #     print(value)

# # for key, value in person.items():
# #     print(key, value) # this way we get both keys and values printed out
  
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3)) # 9

#############################################################

# 12. Modules in Python


# main.py file
# import module
# print(module.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

# TO import functions from a file, you can specifically import those
  #from mymodule import generate_full_name, sum_two_nums, person, gravity

# Can also rename functions when importing 
  #from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g


# Famous modules are 

#   OS, imports directory
#   statistics
#   math 
#   string 
#   random

# import random 
# import string

# def randomPas(*args):

#   string = args
#   print(string)




# for i in range(7):
#   randomPas(string.ascii_letters, string.digits, string.punctuation)


############################################################

# 14. Map/Filter/Reduce function 

  #Takes a function and an interable as its parameters and returns a new list
# numbers = [1, 2, 3, 4, 5] # iterable
# def square(x):
#    return x ** 2
# numbers_squared = map(square, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# #Filter Function: Takes a boolean value and for each specific iterable and returns it

# numbers = [1, 2, 3, 4, 5]  # iterable

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))       # [2, 4]


# #Reduce function returns an a single variable
# numbers_str = ['1', '2', '3', '4', '5']  # iterable
# def add_two_nums(x, y):
#     return int(x) + int(y)

# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15

#Excersizes

  # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  # def squareN(x):
  #   return x**2


  # squareNum = map(squareN, numbers)
  # print(list(squareNum))

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# def countriesFilter(x):
#   if x[0]=='E':
#     return False
#   return True

# landEnding=filter(countriesFilter, countries)
# print(list(landEnding))

# import functools

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# def addCount(x,y):
#   return x+', '+ y

# add = functools.reduce(addCount, countries)
# print(add)


############################################################

# 15. Errors
  #Chatgpt and Stackoverflow

# 16. Date & Time

# from datetime import datetime
# new_year = datetime.now()
# print(new_year)      # 2020-01-01 00:00:00
# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second

# from datetime import datetime
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)

####################################################

# Unpacking a 
# Can unpack a list using a* method

# numbers = [1,2,3,4,5,6]
# first, second, *third = numbers

# print(first, second, third)

# enumerate
 #To get an index and the value, can you enumeratie

# for index,x in enumerate(numbers):
#   print(str(x)+ ' is in index '+str(index))

##############################################3#\##########

# 19. File Handling

# To open a file, do 
  # open('filename', r)

# f = open('file.txt')
# txt = f.read()
# print(txt)
# f.close()

# #Or 

# with open('file.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

#Read line

# f = open('file.txt')
# txt = f.readline()
# print(txt)
# f.close()

#Add to a file or create a new file

# f = open('file.txt','a')
# f.write('Sheikh Muhammad Ayyub')
# txt= f.read()
# print(txt)
# f.close()

#JSON TO DICT, JSON IS TYPE STRING
# import json
# # python dictionary
# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# # let's convert it to  json

# person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
# print(type(person_json))
# print(person_json)

# import json

# person= {
#   'name' : 'Muhammad',
#   'Hobby':'Arm',
#   'Skills':['Throwing', 'trolling']
# }

# f = open('jsonTest.json','w', encoding = 'utf-8')
# json.dump(person, f, ensure_ascii=False)

############################################
# 20. PIP manager

# import webbrowser

# url = 'https://www.youtube.com/watch?v=pM520_JLR6w'

# webbrowser.open_new_tab(url)

# import requests

# url = 

# https://www.tesla.com/en_CA/careers/search/job/internship-correctness-reliability-engineer-dojo-winter-spring-2025-226993
# https://www.tesla.com/en_CA/careers/search/job/internship-ml-performance-software-engineer-dojo-winter-spring-2025-226976
# https://www.tesla.com/en_CA/careers/search/job/internship-android-engineer-mobile-software-winter-spring-2025-225141
# https://www.tesla.com/en_CA/careers/search/job/internship-test-automation-and-validation-engineer-vehicle-firmware-winter-spring-2025-225750
# https://www.tesla.com/en_CA/careers/search/job/internship-system-validation-automation-engineer-vehicle-firmware-winter-spring-2025-224835
# https://www.tesla.com/en_CA/careers/search/job/internship-integration-platforms-software-developer-vehicle-firmware-winter-spring-2025-225936
# https://www.tesla.com/en_CA/careers/search/job/internship-bms-embedded-systems-software-engineer-vehicle-firmware-winter-spring-2025-225929
# https://www.tesla.com/en_CA/careers/search/job/internship-reinforcement-learning-engineer-tesla-bot-winter-spring-2025-223250
# https://www.tesla.com/en_CA/careers/search/job/internship-embedded-software-engineer-firmware-platforms-winter-spring-2025-225195

##############################################################################

# 22. Web Scrapping

# import requests
# from bs4 import BeautifulSoup 

# url= 'http://www.bu.edu/president/boston-university-facts-stats/'
# response = requests.get(url)
# # lets check the status
# status = response.status_code
# content=response.content
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)


###########################################################

# 21. Classes and Objects

# class Person:
#   def __init__(self, firstname, lastname, age, country):
#     self.lastname = lastname
#     self.firstname = firstname
#     self.age = age
#     self.country = country

#   def firstAndLast(self):
#     return f'This persons full name is {self.firstname} {self.lastname}'
  

# p = Person('Muhammad', 'Farooqi', '19', 'Canada')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.firstAndLast())



##########################################################

# 23. Virtual Env

# python -m venv venv 
# then activate


# 24. Numpy

# Can create arrays using numpy and do addition subtraction multiplication and division

# Can get first rows by first_row = two_dimension_array[0]
# can get first column by first_column= two_dimension_array[:,0]\


# 25. Pandas 