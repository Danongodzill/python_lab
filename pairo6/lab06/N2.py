import random
import statistics

N = 10
grades = []

for i in range(N):
    grades.append(random.randint(1, 12))

min_grade = min(grades)
max_grade = max(grades)
mean_grade = statistics.mean(grades)
median_grade = statistics.median(grades)

high_count = 0
for grade in grades:
    if grade >= 10:
        high_count += 1

print("Оцінки:", grades)
print("Min:", min_grade)
print("Max:", max_grade)
print("Середнє:", round(mean_grade, 2))
print("Медіана:", median_grade)
print("Оцінок 10-12:", high_count)
