highest_guess= 100
lower_guess =1
choice = (lower_guess + highest_guess)//2
print(choice)
response = input('the number to be guessed is:')
number_guess= 1

while response != "correct":
    if response == "too low":
        lower_guess= choice +1
        number_guess= number_guess+1
    elif response == "too high":
        highest_guess= choice -1
        number_guess= number_guess+1
    choice = (lower_guess + highest_guess) // 2
    print(f"My next guess is: {choice}") 
    response = input()


if response == "correct":
    print(f'I got it! The correct answer is {choice}, the number of guess is {number_guess}')