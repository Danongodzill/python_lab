import math

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def main():
    print("Оберіть фігуру:")
    print("1 - круг")
    print("2 - прямокутник")
    print("3 - трикутник")
    
    choice = input("Ваш вибір (1-3): ").strip()
    
    if choice == "1":
        r = float(input("Введіть радіус круга: "))
        print("Площа круга:", round(circle_area(r), 2))
    elif choice == "2":
        w = float(input("Введіть ширину прямокутника: "))
        h = float(input("Введіть висоту прямокутника: "))
        print("Площа прямокутника:", rectangle_area(w, h))
    elif choice == "3":
        b = float(input("Введіть основу трикутника: "))
        h = float(input("Введіть висоту трикутника: "))
        print("Площа трикутника:", triangle_area(b, h))
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()
