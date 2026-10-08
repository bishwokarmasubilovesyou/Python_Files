number = int(input("Enter a number: "))

for i in range(1, 21):
    result = number * i

    if result % 2 == 0:
        print(number, "×", i, "=", result, "→ Even")

    else:
        print(number, "×", i, "=", result, "→ Odd")