n = int(input("Кол-во чисел: "))
sequence = [int(input(f"Число {i+1}: ")) for i in range(n)]

# Инициализация переменной to_add на случай, если последовательность уже является палиндромом
to_add = []

# Проверка и дополнение для создания симметрии
for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        to_add = sequence[:i][::-1]
        break

print("Последовательность:", sequence)
print("Нужно приписать чисел:", len(to_add))
print("Сами числа:", to_add)
