valid_records = []
skipped_count = 0

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line:
                print(f"Рядок {line_number} пропущено: порожній рядок.")
                skipped_count += 1
                continue

            parts = line.split(";")
            if len(parts) != 2:
                print(f"Рядок {line_number} пропущено: неправильна кількість полів або відсутній роздільник ';'.")
                skipped_count += 1
                continue

            student_name = parts[0].strip()
            score_str = parts[1].strip()

            if not student_name:
                print(f"Рядок {line_number} пропущено: відсутнє ім'я студента.")
                skipped_count += 1
                continue

            try:
                score = int(score_str)
            except ValueError:
                print(f"Рядок {line_number} пропущено: бал не є числом.")
                skipped_count += 1
                continue

            if score < 0 or score > 100:
                print(f"Рядок {line_number} пропущено: бал поза діапазоном.")
                skipped_count += 1
                continue

            valid_records.append((student_name, score))

    valid_records.sort(key=lambda item: item[1], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as report_file:
        for student_name, score in valid_records:
            report_file.write(f"{student_name}; {score}\n")

    print(f"Правильних записів: {len(valid_records)}")
    print(f"Пропущено: {skipped_count}")
    print("Створено report.txt")

except FileNotFoundError:
    print("Помилка: файл students.txt не знайдено.")
