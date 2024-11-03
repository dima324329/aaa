import random

class Student:
    def __init__(self, name, money=100, health=100, knowledge=0, fatigue=0):
        self.name = name
        self.money = money
        self.health = health
        self.knowledge = knowledge
        self.fatigue = fatigue

    def work(self):
        if self.health > 20 and self.fatigue < 80:
            earned_money = random.randint(10, 50)
            self.money += earned_money
            self.fatigue += 20
            self.health -= 10
            print(f"{self.name} працював і заробив {earned_money} грн.")
        else:
            print(f"{self.name} занадто втомлений або має недостатнє здоров'я, щоб працювати.")

    def study(self):
        if self.health > 30 and self.fatigue < 70:
            self.knowledge += 10
            self.fatigue += 30
            self.health -= 5
            print(f"{self.name} навчається і підвищив свої знання.")
        else:
            print(f"{self.name} занадто втомлений або має недостатнє здоров'я, щоб навчатися.")

    def rest(self):
        if self.money >= 10:
            self.money -= 10
            self.fatigue = max(0, self.fatigue - 30)
            self.health = min(100, self.health + 20)
            print(f"{self.name} відпочиває, витративши 10 грн.")
        else:
            print(f"{self.name} не має достатньо грошей на відпочинок.")

    def live_one_day(self):
        if self.money < 20:
            self.work()
        elif self.health < 40 or self.fatigue > 70:
            self.rest()
        elif self.knowledge < 50:
            self.study()
        else:
            print(f"{self.name} проводить день спокійно.")

    def live_one_year(self):
        days = 365
        for day in range(1, days + 1):
            print(f"\nДень {day}:")
            self.live_one_day()
            print(f"Статус: гроші: {self.money}, здоров'я: {self.health}, знання: {self.knowledge}, втома: {self.fatigue}")
            if self.health <= 0:
                print(f"{self.name} втратив здоров'я і не зміг продовжувати.")
                break

student = Student("Іван", money=50, health=100, knowledge=0, fatigue=0)
student.live_one_year()
