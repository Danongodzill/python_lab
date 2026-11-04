group_info = ("10-IT", "2026/2027")

students = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}

print(group_info[0], "-", group_info[1])

name = input("Введіть ім'я нового учня: ")
grades = list(map(int, input("Введіть 5 оцінок через пробіл: ").split()))

if len(grades) == 5 and all(1 <= grade <= 12 for grade in grades):
    students[name] = grades
    print("Учня додано!")
else:
    print("Помилка! Потрібно ввести рівно 5 оцінок від 1 до 12.")

print("\nЖурнал групи:")

for name, grades in students.items():
    print(name, "-", grades)

print("\nСередні бали:")

averages = {}

for name, grades in students.items():
    average = sum(grades) / len(grades)
    averages[name] = average
    print(name, "-", round(average, 2))

print("\nРейтинг учнів:")

rating = sorted(averages.items(), key=lambda x: x[1], reverse=True)

for name, average in rating:
    print(name, "-", round(average, 2))

best_student = max(averages, key=averages.get)

print("\nНайкращий результат:", best_student, "-", round(averages[best_student], 2))
