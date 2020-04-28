from random import randint

print("Welcome to Guess_The_Number. Guess a number between 1 and 20\n")
guess = int(input())

numberlist = range(1, 21)
number = numberlist[randint(1, 21)]
answer = False


while answer == False:
    if guess == number:
        print("You guessed the number correctly")
        answer = True
    elif guess > number:
        if (guess - number) >= 10:
            print("Your guess is too large. Try a smaller number")
            guess = int(input())
        elif 5 <= (guess - number) < 10:
            print("Your guess is quite large. Try a smaller number")
            guess = int(input())
        elif 1 <= (guess - number) < 5:
            print("Your guess is almost correct. Try a smaller number")
            guess = int(input())
    elif guess < number:
        if (number - guess) >= 10:
            print("Your guess is too small. Try a larger number")
            guess = int(input())
        elif 5 <= (number - guess) < 10:
            print("Your guess is quite small. Try a larger number")
            guess = int(input())
        elif 1 <= (number - guess) < 5:
            print("Your guess is almost correct. Try a larger number")
            guess = int(input())
    else:
        print("Confirm that your input is correct")


