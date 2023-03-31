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


# ## break, continue, pass
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

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

# x = 0

# while x < 10:
#     print('x is currently: ',x)
#     print('x is still less than 10, adding 1 to x')
#     x+=1
#     if x==3:
#         print('x==3')
#     if x==8:
#         print('x==8')
#     else:
#         print('continuing...')
#         continue


# break - breaks out of the current closest enclosing loop
# mystring = "Scotty"
# for letter in mystring:
#     if letter == 'o':
#         break
#     print(letter)

# x = 0
# while x < 5:
#     if x ==2:
#         break
#     print(x)
#     x += 1

x = 0

while x < 10:
    print('x is currently: ',x)
    print('x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

# Example of infinite loop. Avoid this
# while True:
#     print("I'm stuck in an infinite loop!")

