###导入类
'''一个可用于汽车的类'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):   #在定义子类必须在括号指定父类的名称
    def __init__(self, make, model, year):
        '''初始化父类的属性'''
        super().__init__(make, model, year)  #super()特殊函数让父类和子类关联起来
        self.battery_size = 70  #添加一个新的属性并设置默认值
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    '''重写父类的方法'''
    def fill_gas_tank(self):
        print("this car doesn't need a gas tank!")

class Battery():
    def __init__(self, battery_siza = 90, car_model = 'model 3'):
        self.battery_size = battery_siza
        self.car_model = car_model
    def descibe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 90 and self.car_model == 'model s':
            range = 240
        elif self.battery_size == 100 and self.car_model == 'model x':
            range = 270
        message = "a "+self.car_model+" can go "+str(range)
        message += " miles on a full charge"
        print(message)