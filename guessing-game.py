### Create our game
from random import shuffle
mylist = [' ', 'o', ' ']

def shuffle_list(mylist):
    # take in list, return shuffled version
    shuffle(mylist)

    return mylist

# print(mylist)
# print(shuffle_list(mylist))

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        # recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)

# player_guess()

# check the user's guess. Notice we only print here, since we don't need
# to save the user's guess or the shffled list.

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else: 
        print('Wrong! Better luck next time')
        print(mylist)

# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)
