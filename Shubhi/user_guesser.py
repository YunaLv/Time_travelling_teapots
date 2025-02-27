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
    guesses.add(your_guess)
    if feedback == "lower":
        if highest_number > your_guess:
            highest_number = your_guess
        print (f"highest: {highest_number}")
    elif feedback == "higher": 
        if lowest_number < your_guess:
            lowest_number = your_guess
        print (f"lowest: {lowest_number}")
    else: 
        print ("invalid input")
    #your_guess = random.randint(lowest_number, highest_number)
    your_guess = random.choice(list(set(range(lowest_number, highest_number)) - guesses))
    print (your_guess)
    feedback = input("feedback? ")
    print (f" I've guessed: {guesses}")
    if highest_number<lowest_number:
        print ("LIAR")
    #your_guess = random.randint(0,10)   
else: 
    print ("yay :)")
