### Adding block comments Examples when finisihed.
### Uncomment code blocks to run again

# basic syntax for loop
# my_iterable = [1,2,3]
# for item_name in my_iterable: # item_name represents numbers in the list
#     print(item_name)

### Example 1

# mylist = [1,2,3,4,5,6,7,8,9,10]

# for num in mylist: # num represents numbers in the list
#     print(num)

### Example 2
# Print only the even numbers from a list

# mylist = [1,2,3,4,5,6,7,8,9,10]

# for num in mylist:
#     # Check for even numbers
#     if num % 2 == 0:
#         print(num)
#     else: 
#         print(f'Odd Number: {num}')

### Example 3
# running tally using for loop
# start sum at zero

# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0

# for num in mylist:
#     list_sum = list_sum + num

#     print(list_sum)

# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0

# for num in mylist:
#     list_sum += num

# print(list_sum)

### Example 4
# for loops with strings

# for letter in 'This is a string.':
#     print(letter)

# mystring = 'Hello World'

# for letter in mystring:
#     print(letter)

# for letter in 'Hello World':
#     print(letter)


# for _ in 'Hello World':
#     print('Cool!')


### Example 5
# for loops with tuples

# tup = (1,2,3)

# for item in tup:
#     print(item)


### Example 6
# tuple inside a list
# tuple unpacking using for loops
# During for loops, unpacking tuple inside a sequence

# mylist = [(1,2), (3,4), (5,6), (7,8)]

# for item in mylist:
#     print(item)

# print(len(mylist))

# tuple unpacking
# mylist = [(1,2), (3,4), (5,6), (7,8)]

# for (a,b) in mylist:
#     print(a)
#     print(b)


# Common to use without parenthesis in a,b
# mylist = [(1,2), (3,4), (5,6), (7,8)]

# for a,b in mylist:
#     print(a)
#     print(b)

# mylist = [(1,2,3),(4,5,6),(7,8,9)]
# for a,b,c in mylist:
#     print(b)


### Example 7
# iterating through dictionaries with for loops

# When iterating through a dictionary, you only iterate through the keys
# d = {'k1':1, 'k2':2, 'k3':3}

# for item in d:
#     print(item)

# Tuple unpacking in dictionaries with only the values
# To iterate through the items, you need to use .items
# keep in mind, dictionaries are unordered

# d = {'k1':1, 'k2':2, 'k3':3}
# for key,value in d.items():
#     print(value)

# d = {'k1':1,'k2':2,'k3':3}

# for k,v in d.items():
#     print(k)
#     print(v)


# To obtain a true list of keys
# use list(d.keys())
# d = {'k1':1,'k2':2,'k3':3}

# for k in list(d.keys()):
#     print(k)

# To obtain a sorted list
# use sorted(d.values())
d = {'k1':1,'k2':45,'k3':3,'k4':98,'k5':101}

for v in sorted(d.values()):
    print(v)