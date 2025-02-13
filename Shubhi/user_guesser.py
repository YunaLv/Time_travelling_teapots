import random 

number = input ("What is the number? ")
number = int(number)

your_guess = random.randint(0, 10)
print (your_guess)
feedback = input("feedback? ")

guesses = set()
lowest_number = 0
highest_number = 10
while feedback != "correct":
    print (your_guess)
    guesses.add(your_guess)
    if feedback == "lower":
        if highest_number > your_guess:
            highest_number = your_guess
        print (f"lowest: {highest_number}")
    elif feedback == "higher": 
        if lowest_number < your_guess:
            lowest_number = your_guess
        print (f"highest: {lowest_number}")
    #your_guess = random.randint(lowest_number, highest_number)
    your_guess = random.choice(list(set(range(0,10)) - guesses))
    #your_guess = random.randint(0,10) 
    if highest_number < lowest_number:
        print ("LIARRR")
    feedback = input("feedback? ")
else: 
    print ("yay :)")
