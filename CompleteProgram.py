numbers = []

try:
    for i in range(1, 6):
        number = float(input("Enter number " + str(i) + ": "))
        numbers.append(number)

    squares = [number ** 2 for number in numbers]

    def generate_cubes():
        for number in numbers:
            yield number ** 3

    print("\nSquares:", squares)

    print("\nCubes:")
    for cube in generate_cubes():
        print(cube)

except ValueError:
    print("Invalid input. Please enter a number.")

finally:
    print("\nThank you for using the program.")