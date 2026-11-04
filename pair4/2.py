group1 = {"Anna", "Ivan", "Olha"}
group2 = {"Ivan", "Maksym", "Olha"}

print("Спільні:", group1 & group2)
print("Тільки group1:", group1 - group2)
print("Тільки group2:", group2 - group1)
print("Усі:", group1 | group2)
