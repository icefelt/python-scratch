# basic syntax for loop
# my_iterable = [1,2,3]
# for item_name in my_iterable: # item_name represents numbers in the list
#     print(item_name)

# mylist = [1,2,3,4,5,6,7,8,9,10]

# for num in mylist: # num represents numbers in the list
#     print(num)

# mylist = [1,2,3,4,5,6,7,8,9,10]

# for num in mylist:
#     # Check for even numbers
#     if num % 2 == 0:
#         print(num)
#     else: 
#         print(f'Odd Number: {num}')

# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0

# for num in mylist:
#     list_sum = list_sum + num

# print(list_sum)

# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0

# for num in mylist:
#     list_sum = list_sum + num

#     print(list_sum)

# mystring = 'Hello World'

# for letter in mystring:
#     print(letter)

# for letter in 'Hello World':
#     print(letter)


# for _ in 'Hello World':
#     print('Cool!')


# tup = (1,2,3)

# for item in tup:
#     print(item)


# tuples inside a list
# mylist = [(1,2), (3,4), (5,6), (7,8)]

# len(mylist)

# for item in mylist:
#     print(item)


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

# When iterating through a dictionary, you only iterate through the keys
# d = {'k1':1, 'k2':2, 'k3':3}

# for item in d:
#     print(item)


# To iterate through the items, you need to use .items
# d = {'k1':1, 'k2':2, 'k3':3}

# for item in d.items():
#     print(item)

# Tuple unpacking in dictionaries with only the values
# keep in mind, dictionaries are unordered
# d = {'k1':1, 'k2':2, 'k3':3}

# for key,value in d.items():
#     print(value)

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
