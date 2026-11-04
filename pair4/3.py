prices = {
    "bread": 35,
    "milk": 48,
    "cheese": 120
}

name = input("Введіть назву товару: ")
price = int(input("Введіть ціну товару: "))

prices[name] = price

search = input("Який товар знайти? ")

print("Пошук:", prices.get(search, "Товар не знайдено"))

minimum = int(input("Мінімальна ціна: "))
maximum = int(input("Максимальна ціна: "))

print("Товари у заданому діапазоні:")

for product, price in prices.items():
    if minimum <= price <= maximum:
        print(product, "-", price, "грн")
