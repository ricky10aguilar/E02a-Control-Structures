#!/usr/bin/env python3
import sys, random #importing infomation from a library 

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" # requiring Python to run


print('Greetings!') # Will print "greetings" to user
colors = ['red','orange','yellow','green','blue','violet','purple'] # a list of the colors that can be guessed
play_again = '' # allows game to be played again 
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #creates loops unless user says no or n to play again 
    match_color = random.choice(colors) #chooses a random number
    count = 0 #establishes where the count will begin 
    color = '' #provides program to reply with color chosen 
    while (color != match_color): #creates loop of guessing unless they get the answer right
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # turns any answer provided into lowercase and ignores any additional spaces
        count += 1 # determines what value to count by
        if (color == match_color): # the path of choosing the right color 
            print('Correct!') #giving feedback to player for guessing right
        else: # path of choosing wrong color
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #provides feedback of wrong answer and how many guesses player has inputed
    
    print('\nYou guessed it in {} tries!'.format(count)) #feedback to player after guessing correctly, and giving them their total guesses

    if (count < best_count): #new function to give player feedback based upon other trails like a highscore
        print('This was your best guess so far!') # print the feedback to the player 
        best_count = count #stores the score for future trials

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() # allows player to play again

print('Thanks for playing!') #printed if the player says no, ending the whole loop of the game