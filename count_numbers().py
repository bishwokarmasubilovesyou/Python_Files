def count_numbers():
    for number in range(1, 11):
        yield number


for number in count_numbers():
    print(number)