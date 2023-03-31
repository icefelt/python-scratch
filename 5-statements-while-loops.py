# syntax of a while loop
# while some_boolean_condition:
#     #do something

# You can use else statements with while statements
# while some_boolean_condition:
#     # do something
# else:
#     # do something different

# x = 0

# while x < 5:
#     print(f'The current value of x is {x}')
#     # x = x + 1 # same as below
#     x += 1
# else: 
#     print("X is no longer less than 5")


## break, continue, pass
# pass
# x = [1,2,3]

# for item in x:
#     # comment
#     pass # does nothing at all


# continue - goes to the top of the closest encosing loop
# mystring = "Scotty"
# for letter in mystring:
#     if letter == 'o':
#         continue
#     print(letter)

# break - breaks out of the current closest enclosing loop
# mystring = "Scotty"
# for letter in mystring:
#     if letter == 'o':
#         break
#     print(letter)

x = 0
while x < 5:
    if x ==2:
        break
    print(x)
    x += 1
