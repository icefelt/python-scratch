# use range function for iteration
# for num in range(10): #start, stop, step
#     print(num)

# use range function for iteration    
# for num in range(2,20,3): #start, stop, step
#     print(num)

# generators - special function to generate information; instead of saving it to memory
# I'm not able to print this from a .py file
# I do see output from an interactive prompt. 
# What am I missing? 
# I expect to see the output: 
# list(range(2,20,3))
# [0, 2, 4, 6, 8, 10]

# for num in range(0,11,2): #start, stop, step
#     print(num)

# enumerate function - can take in iterable object and 
# returns index counter and the object or element itself

# index_count 
# index_count = 0

# for letter in 'abcde':
#     print('At index {} the letter is {}'.format(index_count,letter))
#     index_count += 1


# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(word[index_count])
#     index_count += 1


# We get back tuples
# doing index_count automatically with tuples
# word = 'abcde'

# for item in enumerate(word):
#     print(item)

# word = 'abcde'

# for index,letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')

# zip operator
# mylist1 = [1,2,3]
# mylist2 = ['a','b','c']
# mylist3 = [100,200,300]

# for item in zip(mylist1,mylist2):
#     print(item)


# in keyword operator
# expect to see True or False, but I don't see itin file, only in interactive prompt
# 'x' in [1,2,3]
# 'a' in 'a world'

# how can I print the result? 
# use if statement and print function to print a 'true' string
# fruits = ["apple", "banana", "cherry"]

# if "banana" in fruits:
#   print("true")

# or we can print the list  
# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#   print(x)

# >>> d = {'mykey' : 345}
# >>> 345 in d.values()
# True
# >>> 345 in d.keys()
# False

# min max are built in functions
# mylist =[10,20,20,40,100]
# print (min(mylist))
# print (max(mylist))

#  random library
# from random import shuffle
# mylist = [1,2,3,4,5,6,7,8,9,10]
# shuffle(mylist)
# print(mylist)

# from random import randint
# mynum = randint(0,10)
# print(mynum)

# result = input('Enter a number: ')
# print(int(result))