##给属性指定默认值
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
    def get_descirptive_name(self):
        print(self.make+" "+self.model+" "+str(self.year))
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('BMW', 'M5 comptation', 2020)
print(my_new_car.get_descirptive_name())
my_new_car.read_odometer()
#修改属性的值
my_new_car = Car('Audi', 'A7', 2021)
print(my_new_car.get_descirptive_name())
my_new_car.odometer_reading = 520
my_new_car.read_odometer()
#通过方法修改属性的值
my_new_car = Car('Benz', 'E300', 2020)
print(my_new_car.get_descirptive_name())
my_new_car.update_odometer(27)
my_new_car.read_odometer()
#通过方法对属性的值进行递增
my_new_car = Car('BYD', '汉', 2022)
print(my_new_car.get_descirptive_name())
my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(527)
my_new_car.read_odometer()











