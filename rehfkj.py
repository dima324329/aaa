import random

class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        self.money += 40
        print("I am working today")

    def eat(self):
        self.house.food -= random.randint(1, 10)
        self.house.pollution += random.randint(1, 5)
        print("I ate")

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(1, 10)
        if self.car is None:
            print("I went to the store on foot")
        else:
            if self.car.drive(random.randint(1, 10) * 10):
                print("We drove to the store")
            else:
                print("I went to the store on foot")

    def chill(self):
        self.money -= random.randint(10, 20)
        self.house.pollution += random.randint(1, 5)
        print("I had a good rest")

    def cleaning(self):
        if self.house.pollution < 20:
            print("I did light cleaning")
            self.house.pollution -= random.randint(1, 5)
            self.money -= 5 
        else:
            print("I did a deep cleaning")
            self.house.pollution -= random.randint(10, 20)
            self.money -= 20

        self.house.pollution = max(0, self.house.pollution)

    def info(self):
        print(f"Money - $ {self.money}")
        print(self.house)
        if self.car is not None:
            print(self.car)

    def live(self, day):
        print(f"Day #{day}")
        choice = random.randint(1, 5)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()
        elif choice == 5:
            self.cleaning()

        if self.money > 1000:
            print("Buying a car")
            self.money -= 500
            self.car = Car("Tesla Model S")

        self.info()
        print()

    def is_alive(self):
        return self.money >= 0

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"House info: food - {self.food}, pollution - {self.pollution}"

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        consumption = length * 0.1
        if self.fuel - consumption < 0:
            print("Journey not possible, not enough fuel")
            return False
        else:
            print(f"We drove {length} km, used {consumption} L of fuel")
            self.fuel -= consumption
            self.state -= length * 0.01
            return True

    def add_fuel(self, fuel):
        self.fuel = min(self.fuel + fuel, 60)

    def __str__(self):
        return f"Car {self.model}\nFuel - {self.fuel} L, condition - {int(self.state)} %"

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Job: {self.name}, salary - {self.salary}"

job = Job("Crypto investor", 1000)
human = Human(input("Name = "), job=job)
for day in range(366):
    if not human.is_alive():
        break
    human.live(day)
