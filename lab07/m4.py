def load_grades(filename):
    records = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            name, subject, grade_str = clean_line.split(";")
            name = name.strip()
            grade = int(grade_str.strip())
            
            if name not in records:
                records[name] = []
            records[name].append(grade)
    return records

def analyze_students(records):
    summary = []
    for name, grades in records.items():
        count = len(grades)
        average = sum(grades) / count
        summary.append({
            "name": name,
            "count": count,
            "average": average
        })
    summary.sort(key=lambda item: item["average"], reverse=True)
    return summary

def save_report(filename, summary):
    with open(filename, "w", encoding="utf-8") as file:
        for student in summary:
            print(f"{student['name']} — оцінок: {student['count']} — середній: {student['average']:.2f}", file=file)
        
        if summary:
            max_avg = summary[0]["average"]
            best_students = [s["name"] for s in summary if abs(s["average"] - max_avg) < 1e-9]
            best_names = " та ".join(best_students)
            print(f"\nНайкращий результат: {best_names} ({max_avg:.2f})", file=file)

grades_data = load_grades("grades.csv")
students_summary = analyze_students(grades_data)
save_report("report.txt", students_summary)
print("Звіт report.txt сформовано.")
