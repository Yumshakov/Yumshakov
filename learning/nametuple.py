from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
print(Car('Blue', 56000))
electric_car = namedtuple('ElectricCar', Car._fields + ('charge',))
print(electric_car('Blue', 56000, '450A'))
