def even_numbers():
    for number in range(0, 20, 2):
        yield number


for number in even_numbers():
    print(number)