# Список песен с продолжительностью
violator_songs = [
    ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29], ['Clean', 5.83]
]

n = int(input("Сколько песен выбрать? "))
total_duration = 0

for i in range(1, n + 1):
    song_name = input(f"Название {i}-й песни: ")
    for song in violator_songs:
        if song[0].lower() == song_name.lower():
            total_duration += song[1]

print("Общее время звучания песен:", round(total_duration, 2), "минуты")
