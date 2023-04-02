# List comprehensions 
# Python includes a more advnaced operation, call list comprehensions.
# List comprehensions allow us to build lists using different notation. 
# Basic Syntax
# newList = [ expression(element) for element in oldList if condition ] 


# This is one line for loop build inside brackets 

### Example 1
# Grab every letter in a string

# lst = [x for x in 'word']
# print(lst)


### Example 2
# square numbers in range and turn into list

# lst = [x**2 for x in range(0,11)]
# print(lst)


### Example 3
# add an if statement to list comprehension
# check for numbers in a range
# lst = [x for x in range(100) if x % 2 == 0]
# print(lst)


### Example 4
# convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

