class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class Toyotacar(Car):
    def run(self):
        print('first')

class TeslaCar(Car):
    def run(self):
        print("super first")
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyotaCar = Toyotacar('Nexus')
print(toyotaCar.model)
toyotaCar.run()
print('########')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
