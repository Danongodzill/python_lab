students = ["Олена Коваль", "Максим Ткаченко", "Ірина Бондар", "Дмитро Шевченко"]
subjects = {
    "математика": 10,
    "українська мова": 11,
    "інформатика": 12,
    "фізика": 9,
}

choice = input("1 - учень, 2 - предмет: ").strip()

if choice == "1":
    try:
        index = int(input("Індекс: "))
        print("Учень:", students[index])
    except ValueError:
        print("Помилка: індекс повинен бути цілим числом.")
    except IndexError:
        print("Помилка: учня з таким індексом немає.")
elif choice == "2":
    subject = input("Назва предмета: ").strip().lower()
    try:
        print("Оцінка:", subjects[subject])
    except KeyError:
        print("Помилка: такого предмета немає у словнику.")
else:
    print("Помилка: невідомий пункт меню. Оберіть 1 або 2.")
