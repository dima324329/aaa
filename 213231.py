import sqlite3

conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_звiра TEXT,
    Тип_звiра TEXT
)
""")

cursor.execute("INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES ('Лев', 'Ссавець')")
cursor.execute("INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES ('Крокодил', 'Плазун')")
cursor.execute("INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES ('Орел', 'Птах')")
cursor.execute("INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES ('Морська черепаха', 'Плазун')")
cursor.execute("INSERT INTO Animals (Назва_звiра, Тип_звiра) VALUES ('Мавпа', 'Ссавець')")

cursor.execute("UPDATE Animals SET Назва_звiра = 'Сокіл' WHERE Назва_звiра = 'Орел'")

print("Звірі типу 'Ссавець':")
cursor.execute("SELECT * FROM Animals WHERE Тип_звiра = 'Ссавець'")
for row in cursor.fetchall():
    print(row)

print("\nВсі записи про звірів:")
cursor.execute("SELECT * FROM Animals")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
