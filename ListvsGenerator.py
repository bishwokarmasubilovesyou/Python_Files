numbers_list = [1, 2, 3, 4, 5]


def generate_numbers():
    for number in range(1, 6):
        yield number


numbers_generator = generate_numbers()

print("List:", numbers_list)
print("Generator:", numbers_generator)

print("Values generated:")

for number in numbers_generator:
    print(number)