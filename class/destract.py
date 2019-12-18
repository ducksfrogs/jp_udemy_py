
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_hello(self):
        print("I am {}. hello".format(self.name))
        self.run()

    def run(self):
        print('run')

    def __del__(self):
        print("Good by")

person = Person('Mike')
person.say_hello()

del person