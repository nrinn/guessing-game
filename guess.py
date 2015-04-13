import random

random_number = random.randrange(1, 101)

print "Hello player, what is your name?",
name = raw_input()
print "%r, I'm thinking of a number between 1 and 100" % (name)
guess = int(input("Try to guess my number."))

while True:
#while guess != random_number:

    if guess > random_number:
        print "Your guess is high, try again"
        guess = int(input("Try to guess my number."))
    elif guess < random_number:
        print "Your guess is too low, try again."
        guess = int(input("Try to guess my number."))
    elif guess == random_number:
        print "You guessed it! The number was ", + random_number
        break