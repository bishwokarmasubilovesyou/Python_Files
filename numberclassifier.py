positive = 0
negative = 0
zero = 0

for i in range(10):
    number = int(input("Enter an integer: "))

    if number > 0:
        print("Positive")
        positive += 1

    elif number < 0:
        print("Negative")
        negative += 1

    else:
        print("Zero")
        zero += 1

print("Total positive numbers:", positive)
print("Total negative numbers:", negative)
print("Total zeros:", zero)