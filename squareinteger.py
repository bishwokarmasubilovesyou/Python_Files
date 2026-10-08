try:
    number = int(input("Enter an integer: "))
    square = number ** 2

    print("Square:", square)

except ValueError:
    print("Invalid input. Please enter an integer.")

finally:
    print("Program execution completed.")
    