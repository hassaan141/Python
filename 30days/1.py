# Built in functions

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
# String and Splicing

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

language.count('a') gives all the occurences of 

find give the first occurence of that things index
