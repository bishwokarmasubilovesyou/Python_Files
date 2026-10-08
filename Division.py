try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter numbers.")

finally:
    print("Program execution completed.")