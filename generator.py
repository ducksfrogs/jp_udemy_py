#l = ["Good morning", "Good afternoon", "Good night"]
#
#for i in l:
#    print(i)
#

def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()
print('############################')

def grreting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

#for g in grreting():
#    print(g)

g = grreting()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print("@@@@@")
print(next(g))
