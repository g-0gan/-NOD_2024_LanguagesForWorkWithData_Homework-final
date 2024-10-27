# Список деталей с ценами
shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
    ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200],
    ['седло', 2700]
]

# Запрос названия детали
detail = input("Название детали: ")
quantity = sum(1 for item in shop if item[0] == detail)
total_cost = sum(item[1] for item in shop if item[0] == detail)

print(f"Кол-во деталей — {quantity}")
print(f"Общая стоимость — {total_cost}")
