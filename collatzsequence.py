number = int(input("Enter a positive integer: "))

sequence = str(number)
steps = 0
largest = number

while number != 1:

    if number % 2 == 0:
        number = number // 2

    else:
        number = number * 3 + 1

    sequence = sequence + " → " + str(number)
    steps += 1

    if number > largest:
        largest = number

print("Sequence:", sequence)
print("Number of steps:", steps)
print("Largest number:", largest)