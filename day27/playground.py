def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')

car = Car(model='BMW', year='2019', make='Nissan')
print(car.colour)