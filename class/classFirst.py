
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_hello(self):
        print("I am {}. hello".format(self.name))
        self.run()

    def run(self):
        print('run')


person = Person('Mike')
person.say_hello()