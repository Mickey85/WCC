import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

    # Test get_guess
#print get_guess() # Expected: Keeps prompting until user enters a valid number


def compare(numA,numB):
    if (numA > numB ):
        value = 'high'
        return str(value)
    else:
        value = 'low'
        return str(value)
#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'low'
#print compare(99,100) # Expected: 'low'



def play():

    # Pick a secret number
    secret_number = random.randint(1, 100)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")
    total_chances = 5

    guess = int(get_guess())
    #print('your guess is: ' + str(guess))
    # Keep prompting until they get it correct
    # For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'
    results=compare(guess,secret_number)

    if(guess!=secret_number):
        print("Too " + results + " . you have " +  str(total_chances) + " guesses left ")

        for guess_count in range(5,0,-1):
            if(guess!=secret_number):
                guess=int(get_guess())

                results=compare(guess,secret_number)
                if(guess_count == 1 and guess != secret_number):
                     print("Sorry, you ran out of guesses. The correct number was " + str(secret_number) + "." )

                if(guess_count != 1 and guess != secret_number):
                    print("Too " + results + " . you have " +  str(guess_count-1) + " guesses left ")
                #guess_count-=1



        print guess_count





    if(guess == secret_number):
        print('You got it! The number was ' + str(secret_number))
    # Print conclusion




# Run the game
play()
