# Изначальный список гостей
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print("Сейчас на вечеринке", len(guests), "человек:", guests)
    action = input("Гость пришёл или ушёл? ").lower()
    if action == "пора спать":
        break
    name = input("Имя гостя: ")

    if action == "пришёл" or "пришел":
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif action == "ушёл" or "ушел":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")

print("Вечеринка закончилась, все легли спать.")
