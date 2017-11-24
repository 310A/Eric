# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    
    global input_number
    global remain_guesses
    global random_result
    remain_guesses = 7
    random_result = random.randrange(0, range_number, 1)
    print "New game. Range is from 0 to", range_number
    print "Number of remaining guesses is", remain_guesses
    print
    
    
# initialize global variables used in your code here
remain_guesses = 7
range_number = 100
random_result = random.randrange(0, range_number, 1)


# define event handlers for control panel
def range100():
    
    # button that changes the range to [0,100) and starts a new game 
    global range_number
    range_number = 100
    new_game()
    # remove this when you add your code    


def range1000():
    
    # button that changes the range to [0,1000) and starts a new game     
    global range_number
    range_number = 1000
    new_game()

    
def input_guess(guess):
    
    # main game logic goes here	
    if(random_result > guess):
        print "Higher!"
    elif(random_result < guess):
        print "Lower!"
    else:
        print "Correct!"
    print

    # remove this when you add your code

def get_input(number):
    
    global remain_guesses
    if(remain_guesses == 0):
        new_game()
        return 0
    remain_guesses -= 1
    print "Guess was", number
    print "Number of remaining guesses is", remain_guesses
    input_guess(int(number))
    
# create frame
f = simplegui.create_frame("guess the number", 200, 200)

# register event handlers for control elements and start frame


f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# call new_game 
new_game()

f.start()


# always remember to check your completed program against the grading rubric

