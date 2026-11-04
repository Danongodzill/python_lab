numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
even = []
multiple_3 = []

for number in numbers:
    if number > 0:
        positive.append(number)

    if number < 0:
        negative.append(number)

    if number % 2 == 0:
        even.append(number)

    if number % 3 == 0:
        multiple_3.append(number)

print("Додатні:", positive)
print("Від'ємні:", negative)
print("Парні:", even)
print("Кратні 3:", multiple_3)

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", round(sum(numbers) / len(numbers), 2))
