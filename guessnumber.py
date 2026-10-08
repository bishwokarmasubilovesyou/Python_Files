secret_number = 37
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        break

print("Total attempts:", attempts)