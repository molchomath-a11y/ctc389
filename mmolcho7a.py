#Moshe Molcho CTC389 Lab 7 A ( Review of Lab #1 and 2 )

number = 7

guess =int(input("Guess my number: "))

while guess != number and guess > number -3 and guess < number +3:
    guess = int(input("Close, try again: "))


if guess == number:
                print("Well done! You guessed my number.")
elif guess > number:
                print("Sorry, you lost. Your guess was higher than my number which is ",number,".")
else:
                print("Sorry, you lost. Your guess was lower than my number which is ",number,".")

