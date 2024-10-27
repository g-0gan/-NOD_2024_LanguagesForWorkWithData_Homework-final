# Ввод размеров коньков
n_skates = int(input("Кол-во коньков: "))
skate_sizes = [int(input(f"Размер {i+1}-й пары: ")) for i in range(n_skates)]

# Ввод размеров ног людей
n_people = int(input("Кол-во людей: "))
foot_sizes = [int(input(f"Размер ноги {i+1}-го человека: ")) for i in range(n_people)]

# Подсчет возможных пар
skate_sizes.sort()
foot_sizes.sort()
count = 0
for foot in foot_sizes:
    for i in range(len(skate_sizes)):
        if skate_sizes[i] >= foot:
            count += 1
            skate_sizes.pop(i)
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", count)
