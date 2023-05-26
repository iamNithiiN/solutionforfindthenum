def guess_number():
    # initialize variables
    low = 1
    high = 1000
    guess = 500
    num_guesses = 0

    # loop until the guess is correct
    while True:
        num_guesses += 1
        print("Is your number", guess, "?")
        feedback = input("Enter 'h' if the number is higher, 'l' if the number is lower, or 'c' if the guess is correct: ")
        # update the range of possible numbers based on the feedback
        if feedback == "h":
            low = guess + 1
        elif feedback == "l":
            high = guess - 1
        else:
            print("I guessed your number in", num_guesses, "guesses!")
            return
        # make a new guess
        guess = (low + high) // 2

# call the function to start the game
guess_number()
