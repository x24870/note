def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fibon(6):
    print(x)


def fi(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b