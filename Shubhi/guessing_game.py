import random

# This is the number the user will try to guess
number = -1


def start(limit=10):
    '''
    This function will pick a random number between 1 and the given limit.
    :param limit: The upper limit of the number to be picked (default is 10)
    :return: None
    '''
    global number

    # Check if the limit is less than 1
    if limit < 1:
        raise ValueError("Cannot pick a number below 1")

    # Pick a random number between 1 and the limit
    number = random.randint(1, limit)
    print(f"Guess a number between 1 and {limit}")


def guess(guess):
    '''
    This function will take a guess and return a string response,
    telling the user if the guess is too high, too low or correct.
    :param guess: The user's guess
    :return: A string response, either "too high", "too low" or "correct"
    '''
    global number

    # Check if the user has called start() before calling guess()
    if number == -1:
        raise ValueError("You must call start() before calling guess()")

    # Report the user's guess
    print(f"You guessed {guess}")

    # Check if the guess is equal to the number, too low or too high
    if guess == number:
        return "correct"
    elif guess < number:
        return "too low"
    else:
        return "too high"


def reveal_number():
    '''
    This function will reveal the selected number to the user.
    '''
    global number

    print(f"The number is {number}")
