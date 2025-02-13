import random

max = 100
#generator bot
number = random.randint(0, max)

#guessing bot
lowest_guess = 0
highest_guess = max
your_guess = random.randint(0,max)
guesses = set()
while number != your_guess:
    guesses.add(your_guess) 
    if (number < your_guess):
        #updating range (higher)
        highest_guess = your_guess
        print (f"{your_guess} is too high")
    elif (number > your_guess):
        #updating range (lower)
        lowest_guess = your_guess
        print (f"{your_guess} is too low")
    #guessing within new range without repeating
    your_guess = round((lowest_guess + highest_guess)/2)
    #your_guess = random.choice(list(set(range(lowest_guess,highest_guess)) - guesses))
else:
    print(f"Right! The number was {number}")

print (f"number of guesses = {len(guesses) +1}")
