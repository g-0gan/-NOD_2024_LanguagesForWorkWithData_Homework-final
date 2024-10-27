n = int(input("Кол-во друзей: "))
k = int(input("Долговых расписок: "))
balance = [0] * n

for _ in range(k):
    debtor = int(input("Кому: ")) - 1
    creditor = int(input("От кого: ")) - 1
    amount = int(input("Сколько: "))
    balance[debtor] -= amount
    balance[creditor] += amount

print("Баланс друзей:")
for i, bal in enumerate(balance):
    print(f"{i + 1}: {bal}")
