import guessing_game
import random

guessing_game.start()
feedback = guessing_game.guess (7)
guessing_game.guess = random.randint(0,10)

print (feedback)

guessing_game.reveal_number()