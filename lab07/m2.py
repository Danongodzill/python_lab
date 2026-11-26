query = input("Введіть фрагмент для пошуку: ").strip().lower()
found = False

with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        if query in clean_line.lower():
            print(f"{number}: {clean_line}")
            found = True

if not found:
    print("Збігів не знайдено.")
