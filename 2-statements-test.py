# Statement Assessment Test

### Question 1
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'

# st = 'Print only the words that start with s in this sentence'
# for words in st.split():
    # if words[0] == 's' or word[0] == 'S':
    #     print(words)

# st = 'Print only the words that start with s in this sentence'
# for words in st.split():
    # if words[0].lower == 's':
    #     print(words)
   
        
### Question 2
# Use range() to print all the even numbers from 0 to 10.

# for num in range(0,11,):
#     if num % 2 == 0:
#         print(num)

# for num in range(0,11,2):
#     print(num)


### Question 3
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# list = [num for num in range(1,50) if num % 3 == 0]
# print(list)


### Question 4
# Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'

# use split()
# use modulo % 2
# use len()

# st = 'Print every word in this sentence that has an even number of letters'
    
# for letters in st.split():
#     if len(letters) % 2 == 0:
#         print(letters + ' is even')


### Question 5
# Write a program that prints the integers from 1 to 100. But for multiples of three 
# print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else: 
#         print(num)



### Question 6
# Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'

st = 'Create a list of the first letters of every word in this string'

list = [x[0] for x in st.split()]
print(list)