secret_number = 57
attempts = 0

while attempts < 7:

    guess = int(input("Enter a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Error: Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Correct!")
        print("Attempts used:", attempts)
        break

    elif guess > secret_number:
        print("Try a smaller number")

    else:
        print("Try a larger number")

if attempts == 7 and guess != secret_number:
    print("You failed to guess the number.")
    print("The correct number was:", secret_number)