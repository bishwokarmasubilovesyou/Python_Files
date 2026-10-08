def DoubleIt(value):
    return value * 2


def TimesFour(value):
    return DoubleIt(DoubleIt(value))


a = TimesFour(3)
print(a)