### Function Practice Exercises

# Lesser of two evens: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd. 
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             print(a)
#     if a  % 2 == 1 or b % 2 == 1:
#         print(b)

# lesser_of_two_evens(4,12)

### Animal Crackers
# write a function that takes two-word string and returns True if 
# both words begin with the same letter. 
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# split()
# index[0]

def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]

simple = animal_crackers('Levelheaded Llama')
#simple = animal_crackers('Crazy Kangaroo')
print(simple)


### Makes Twenty
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
# If not, return False