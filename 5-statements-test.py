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

st = 'Print every word in this sentence that has an even number of letters'
    
for letters in st.split():
    if len(letters) % 2 == 0:
        print(letters + ' is even')