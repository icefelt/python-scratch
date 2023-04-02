# Statement Assessment Test

### 1
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
   
        
### 2
# Use range() to print all the even numbers from 0 to 10.

# for num in range(0,11,):
#     if num % 2 == 0:
#         print(num)

# for num in range(0,11,2):
#     print(num)


### 3
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

list = [num for num in range(1,50) if num % 3 == 0]
print(list)

