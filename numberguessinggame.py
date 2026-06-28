secret_number = 7

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong guess. Try again!")