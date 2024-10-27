# Ввод чисел для списков
list1 = [int(input(f"Введите {i+1}-е число для первого списка: ")) for i in range(3)]
list2 = [int(input(f"Введите {i+1}-е число для второго списка: ")) for i in range(7)]

# Объединение и удаление дубликатов
list1.extend(list2)
unique_list = list(set(list1))
print("Новый первый список с уникальными элементами:", unique_list)
