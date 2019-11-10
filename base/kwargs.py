def menu(food, *args, **kwargs):
    for k, v in kwargs.items():
        print(k,v)
d = {
    'entree': 'beef',
    'dring': 'coffee',
    'dessert': 'ice'

}


menu(**d)