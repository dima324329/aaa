import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.mood = "щасливий"
    
    def eat(self):
        if self.hunger > 2:
            self.hunger -= 2
            self.energy += 1
            print(f"{self.name} поїв і тепер трохи ситий!")
        else:
            print(f"{self.name} не голодний і не хоче їсти.")
        self.update_mood()
    
    def sleep(self):
        if self.energy < 8:
            self.energy += 3
            self.hunger += 1
            print(f"{self.name} поспав і тепер відчуває себе більш відпочилим!")
        else:
            print(f"{self.name} не хоче спати.")
        self.update_mood()
    
    def play(self):
        if self.energy > 2:
            self.energy -= 2
            self.hunger += 1
            print(f"{self.name} грається та веселиться!")
        else:
            print(f"{self.name} занадто втомлений, щоб грати.")
        self.update_mood()
    
    def update_mood(self):
        if self.hunger >= 8:
            self.mood = "голодний"
        elif self.energy <= 2:
            self.mood = "втомлений"
        else:
            self.mood = random.choice(["щасливий", "цікавий", "лінивий"])
    
    def get_status(self):
        print(f"Настрій: {self.mood}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print("="*20)

kitty = Cat("Мурчик")

kitty.get_status()
kitty.eat()
kitty.get_status()
kitty.play()
kitty.get_status()
kitty.sleep()
kitty.get_status()
