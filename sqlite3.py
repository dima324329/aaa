import sqlite3

conn = sqlite3.connect('AnimalKingdom.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Animals (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Назва_звiра TEXT NOT NULL,
                    Тип_звiра TEXT NOT NULL
                )''')

animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]
cursor.executemany('INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES (?, ?)', animals)

cursor.execute('''UPDATE Animals SET Назва_звiра = 'Сокіл' WHERE Назва_звiра = 'Орел' ''')

cursor.execute('''SELECT * FROM Animals WHERE Тип_звiра = 'Ссавець' ''')
mammals = cursor.fetchall()

cursor.execute('''SELECT * FROM Animals''')
all_animals = cursor.fetchall()

print("Ссавці:", mammals)
print("Всі звірі:", all_animals)