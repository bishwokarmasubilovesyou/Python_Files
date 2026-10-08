numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])

except ValueError:
    print("Invalid input. Please enter an integer.")

except IndexError:
    print("Invalid index. Please enter an index from 0 to 4.")

finally:
    print("List access completed.")