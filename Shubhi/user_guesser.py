import random 

number = input ("What is the number? ")
number = int(number)

your_guess = random.randint(0, 100)
print (your_guess)
feedback = input("feedback? ")
guesses = set()
lowest_number = 0
highest_number = 100
while feedback != "correct":
    if feedback == "lower":
        if highest_number > your_guess:
            highest_number = your_guess
            guesses.add(your_guess)
    elif feedback == "higher": 
        if lowest_number < your_guess:
            lowest_number = your_guess
            guesses.add(your_guess)
    else: 
        print ("invalid input")
    your_guess = random.choice(list(set(range(lowest_number, highest_number)) - guesses))
    print (f" I've guessed: {guesses}")
    print (your_guess)
    feedback = input("feedback? ")
    #does nothing because computer only guesses within the range 
    if highest_number<lowest_number:
        print ("LIAR") 
else: 
    print ("yay :)")

print (f"I took {len(guesses) + 1} guesses ")