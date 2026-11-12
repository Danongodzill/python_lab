def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count

def main():
    grades = [10, 8, 12, 9, 11]
    threshold = 9
    
    print("Оцінки:", grades)
    print("Поріг:", threshold)
    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print("Вище", threshold, ":", count_above(grades, threshold))

if __name__ == "__main__":
    main()
```[cite: 26]
