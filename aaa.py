def user():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    print(f"Привіт {name}, тобі {age}!")

user()

def check_age():
    age = int(input("Скільки вам років? "))
    if age > 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")

check_age()
