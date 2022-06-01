##导入类
from car import Car
my_new_car = Car('Audi', 'a7', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#导入多个类
from car import Car,ElectricCar
my_beetle = Car('BMW', 'M5', 2022)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
#导入整个类
import car
my_tesla = car.ElectricCar('tesla', 'model 3', 2017)
print(my_tesla.get_descriptive_name())