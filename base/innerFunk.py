def outer(a, b):

    def plus(c, d):
        return c + d
    r = plus(a, b)
    print(r)


def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    r2 = plus(b, a)
    print(r + r2)