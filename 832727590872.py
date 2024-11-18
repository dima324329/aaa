class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return f"{self.species} издаёт звук."


class Pet:
    def __init__(self, name):
        self.name = name

    def show_affection(self):
        return f"{self.name} показывает привязанность."


class Dog(Animal, Pet):
    def __init__(self, species, name, breed):
        Animal.__init__(self, species)
        Pet.__init__(self, name)
        self.breed = breed

    def bark(self):
        return f"{self.name} лает."

    def get_info(self):
        return (f"Вид: {self.species}, Порода: {self.breed}, Имя: {self.name}")

my_dog = Dog("Собака", "Бобик", "Лабрадор")
print(my_dog.speak())
print(my_dog.show_affection())
print(my_dog.bark())
print(my_dog.get_info())
