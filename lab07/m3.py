selected_students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue
        name, score_str = clean_line.split(";")
        score = int(score_str.strip())
        if score > 80:
            selected_students.append([name.strip(), score])

selected_students.sort(key=lambda student: student[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in selected_students:
        print(f"{name};{score}", file=file)

print("Дані успішно записано у result.txt.")
