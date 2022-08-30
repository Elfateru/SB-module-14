violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
timelap = 0
songs_amount = int(input('Сколько песен вырбрать? '))
for songs in range(songs_amount):
    print(f'Название {songs + 1}-й песни:', end='')
    song = input()
    for index in range(len(violator_songs)):
        if song == violator_songs[index][0]:
            timelap += violator_songs[index][1]
            break
print('\nОбщее время звучания песен:', round(timelap, 2), 'минуты')
