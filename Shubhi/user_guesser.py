import random 

#to keep track of the number guesses
number = input ("What is the number? ")
number = int(number)

your_guess = random.randint(0, 100)
print (your_guess)
feedback = input("feedback? ")
#to avoid repeat guessing and to count how many guesses at the end
guesses = set()
#to create range within which to guess
lowest_number = 0
highest_number = 100
#while incorrect, as long as the guessing isn't taking very long 
while feedback != "correct" and len(guesses) >10:
    #setting higher limit 
    if feedback == "lower":
        if highest_number > your_guess:
            highest_number = your_guess
            guesses.add(your_guess)
    #setting lower limit
    elif feedback == "higher": 
        if lowest_number < your_guess:
            lowest_number = your_guess
            guesses.add(your_guess)
    #in case of typos etc 
    else: 
        print ("invalid input")
    your_guess = random.choice(list(set(range(lowest_number, highest_number)) - guesses))
    #checking:
    #print (f" I've guessed: {guesses}")
    print (your_guess)
    feedback = input("feedback? ")
    #does nothing because computer only guesses within the range 
    if highest_number<lowest_number:
        print ("LIAR") 
else: 
    print ("yay :)")

print (f"I took {len(guesses) + 1} guesses ")