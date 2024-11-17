class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        print(f"Двигун потужністю {self.power} кВт запущений.")

class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def rotate_wheels(self):
        print(f"{self.wheel_count} колеса обертаються.")

class Lights:
    def __init__(self, light_type):
        self.light_type = light_type

    def turn_on_lights(self):
        print(f"Фари типу {self.light_type} увімкнено.")

class Vehicle(Engine, Wheels, Lights):
    def __init__(self, power, wheel_count, light_type):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        Lights.__init__(self, light_type)

    def vehicle_info(self):
        print("Інформація про транспортний засіб:")
        print(f"  Потужність двигуна: {self.power} кВт")
        print(f"  Кількість коліс: {self.wheel_count}")
        print(f"  Тип фар: {self.light_type}")

car = Vehicle(100, 4, "LED")

car.start_engine()
car.rotate_wheels()
car.turn_on_lights()
car.vehicle_info()
