numbers = [12, 5, 8, 21, 10, 33, 16, 7]

greater_than_10 = [number for number in numbers if number > 10]

odd_numbers = [number for number in numbers if number % 2 != 0]

cubes = [number ** 3 for number in numbers]

print("Numbers greater than 10:", greater_than_10)
print("Odd numbers:", odd_numbers)
print("Cubes:", cubes)