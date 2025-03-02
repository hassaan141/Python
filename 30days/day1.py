#INT

#Division
print(3/2)

#Floor division
print(3//2)

#power of

print(3**2)

#power of 1/2
print(9**0.5)

#type() to find the type

#STRINGS

#String splicing
s = "Hello World"
print(s[:3])
print(s[-2])
#Get everything but the last letter
print(s[:-1])

#Skip every n numbers
print(s[::2])

# Can flip a string using this ::-1
print(s[::-1])
 
#Cannot concatonate to a string, s[0] == 'n' wont work
s += ' Something'
print(s)

#Can also use multiplication to create repetation
letter = 'a'
print(letter*10)

print(s.upper())
print(s.lower())
print(s)
print(s.split())

#LIST

#When adding new items to a list, you need to reassign it
a = [1,2,3,4]
print(a)
print(a+['s'])
print(a)
a = a + ['s']
print(a)

#To add something in a list, use .append()
a.append(5)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
#Can also assign popped item

#reverse and sort
a.reverse()
print(a)

# sorted(a)
# a.sort()

#DICT
my_dict = {'a': 1, 'b': 2, 'c':3}
print(my_dict['a'])

my_dict['a'] = 23
print(my_dict)

new_dict={'a': 1, 'b': [12, 23, 43], 'c':3}
print(new_dict['b'][2])

print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())

#SETS
#are used for unique collections of items
x = set([2,3,4,5])
x.add(1)
print(x)
x.add(1)
print(x)

#FILES
myfile=open('file.txt')
print(myfile.read())


#TEST
#Replace
list3 = [1,2,[3,4,'hello']]
list3[2][2]= "good"
print(list3)

#get hello
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

e = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(e['k1'][0]['nest_key'][1][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))