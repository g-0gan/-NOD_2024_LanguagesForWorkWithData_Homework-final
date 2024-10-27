n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
people = list(range(1, n + 1))

index = 0
while len(people) > 1:
    index = (index + k - 1) % len(people)
    print("Текущий круг людей:", people)
    print("Начало счёта с номера", people[index])
    print("Выбывает человек под номером", people.pop(index))

print("Остался человек под номером", people[0])
