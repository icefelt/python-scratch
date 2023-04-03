# Functions
# Functions group together a set of statements so they can be run more than once. 
# Functions enable us to specify parameters to serve as inputs to the functions.
# Functions allow us to write DRY code and reuse code more easily. 
# Use Functions when you plan on using code multiple times. 

### Function Topics
# def keyword
# simple example of a function
# calling a function with ()
# accepting parameters
# print versus return
# adding in logic inside a function
# multiple returns inside a function
# adding in loops inside a function
# tuple unpacking
# interactions between functions

# def name_of_function(arg1,arg2):
#     '''
#     This is where the function's Document String (docstring) goes.
#     When you call help() on your function it will be printed out.
#     '''
#     # do stuff
#     # return desired result

'''
We begin with def then a space followed by the name of the function. Keep names relevant. 
For example len() is a good name for a length() function. Also be careful with names. 
You wouldn't want to call a function the same name as a built-in function in Python (such as len).

Next come a pair of parentheses with a number of arguments separated by a comma. 
These arguments are the inputs for your function. You'll be able to use these inputs in 
your function and reference them. After this you put a colon.

Now here is the important step, you must indent to begin the code inside your function correctly. 
Python makes use of whitespace to organize code. Lots of other programing languages do not do this.

Next you'll see the docstring, this is where you write a basic description of the function.
Using Jupyter and Jupyter Notebooks, you'll be able to read these docstrings by pressing Shift+Tab
after a function name. Docstrings are not necessary for simple functions. 
However, it's good practice to put them in so you or other people can easily understand the code you write.

After all this you begin writing the code you wish to execute.
'''

# ### Simple example of a function
# def say_hello():
#     print('hello')

# say_hello()


### Accepting parameters (arguments) in functions
# write a funciton greeting people with their name

# def greeting(name):
#     print(f'Hello {name}')

# greeting('Purple People Eater')


### Using return keyword to save the resulting variable
# return allows a function to return a result and store it as a variable
# or in another manner. 

# def add_num(num1,num2):
#     return num1+num2

# result = add_num(63,81)
# print(result)

# using return with strings
# def add_num(num1,num2):
#     return num1+num2

# result = add_num('one','two')
# print(result)


### Difference between return and print
# return keyword lets you ave the result of output of a function as a variable. 
# print() function simply displays the output, but it doesn't save for future use. 

# def print_result(a,b):
#     print(a+b)

# def return_result(a,b):
#     return a + b

# print_result(10,5)

# return_result(10,5) # You won't see output when run in .py script

# If you wawnt to save for later
# my_result = print_result(20,20)
# print(type(my_result))


### more print vs. return
# Be careful! Notice how print_result() doesn't let you actually save the result to a variable! 
# It only prints it out, with print() returning None for the assignment!

# def print_result(a,b):
#     print(a+b)

# def return_result(a,b):
#     return a + b

# my_result = return_result(20,20)

# print(my_result)

# add results to each other
# def return_result(a,b):
#     return a + b

# my_result = return_result(20,20)

# print(my_result + my_result)



### Add logic to internal function operations
# We know if/else/elif statements, for loops, while loops, checking if an item is in a list
# or not in a list (use operations). Now, we'll perform these operations on functions.

# Create a function see check if a number is even

# def even_check(number):
#     return number % 2 == 0

# print(even_check(20))
# print(even_check(21))

# return boolean if any number in a list is even
# Note: return breaks out of the loop and exits function

# def check_even_list(num_list):
#     # iterate through each number
#     for number in num_list:
#         # once get find a match, we return True
#         if number % 2 == 0:
#             return True
#         # otherwise don't do anything
#         else:
#             pass

# print(check_even_list([1,2,3]))

# This is wrong. It contains a logic error. 
# We're not returning anything if they are all odd numbers!
# def check_even_list(num_list):
#     # Go through each number
#     for number in num_list:
#         # Once we get a "hit" on an even number, we return True
#         if number % 2 == 0:
#             return True
#         # This is WRONG! This returns False at the very first odd number!
#         # It doesn't end up checking the other numbers in the list!
#         else:
#             return False

# print(check_even_list([1,2,3]))


# Correct approach is to initiate a return False _after_ runnign through the entire loop
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

print(check_even_list([1,2,3]))
print(check_even_list([1,3,5]))
