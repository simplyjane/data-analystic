# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# helper function to start and restart the game
def new_game():
    global secret_number
    global number_guess 
    secret_number = random.randrange(0,100)
    number_guess = 7
    print "New game"
    

# define event handlers for control panel
def range100():
    global secret_number 
    global number_guess
    number_guess = 7
    secret_number = random.randrange(0, 100)
    print "Range is from 0-100"
    print "You could guess 7 times"
    return secret_number
  
def range1000():
    global secret_number
    global number_guess
    number_guess = 10
    secret_number = random.randrange(0, 1000)
    print "Range is from 0-1000"
    print "You could guess 10 times"
    return secret_number
    
def input_guess(guess):
    int_guess = int(guess)
    global number_guess
    number_guess -= 1
    print "Guess was " + guess 
    print "Number of remaining guesses is " + str(number_guess)
    
    if number_guess > 0:
        if int_guess < secret_number:
            print "higher"
        elif int_guess == secret_number:
            print "Correct"
        else:
            print "lower"
    else:
        print" You cannot guess any more. Please start new game now."
        new_game()
# create frame
f = simplegui.create_frame("Guess number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# call new_game 
new_game()
