# Создание списков роста учеников двух классов
class1 = list(range(160, 177, 2))
class2 = list(range(162, 181, 3))

# Объединение и сортировка списка
merged_class = sorted(class1 + class2)
print("Отсортированный список учеников:", merged_class)
