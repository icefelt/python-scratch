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

### Simple example of a function
def say_hello():
    print('hello')

say_hello()