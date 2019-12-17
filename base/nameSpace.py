animal = 'cat'

def f():
    global animal
    print('after ', animal)

f()
print('global ;', animal)