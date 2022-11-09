from random import randint


class Player:

    def __init__(self, name, points=0):
        self.name = name
        self.points = points
        self.card_name = []

    def __str__(self):
        return f'\nУ игрока {self.name}\n{self.card_name}    ({self.points} очков)'


class Deck:

    def __init__(self):
        self.deck = [[2, 'двойка черви '], [2, 'двойка бубен'], [2, 'двойка пики'],
                     [2, 'двойка крести'], [3, 'тройка черви'], [3, 'тройка бубен'],
                     [3, 'тройка пики'], [3, 'тройка крести'], [4, 'четвёрка черви'],
                     [4, 'четвёрка бубен'], [4, 'четвёрка пики'], [4, 'четвёрка крести'],
                     [5, 'пятёрка черви'], [5, 'пятёрка бубен'], [5, 'пятёрка пики'],
                     [5, 'пятёрка крести'], [6, 'шестёрка черви'], [6, 'шестёрка бубен'],
                     [6, 'шестёрка пики'], [6, 'шестёрка крести'], [7, 'семёрка черви'],
                     [7, 'семёрка бубен'], [7, 'семёрка пики'], [7, 'семёрка крести'],
                     [8, 'восьмёрка черви'], [8, 'восьмёрка бубен'], [8, 'восьмёрка пики'],
                     [8, 'восьмёрка крести'], [9, 'девятка черви'], [9, 'девятка бубен'],
                     [9, 'девятка пики'], [9, 'девятка крести'], [10, 'десятка черви'],
                     [10, 'десятка бубен'], [10, 'десятка пики'], [10, 'десятка крести'],
                     [10, 'валет черви'], [10, 'валет бубен'], [10, 'валет пики'],
                     [10, 'валет крести'], [10, 'дама черви'], [10, 'дама бубен'],
                     [10, 'дама пики'], [10, 'дама крести'], [10, 'король черви'],
                     [10, 'король бубен'], [10, 'король пики'], [10, 'король крести'],
                     [11, 'туз черви'], [11, 'туз бубен'], [11, 'туз пики'], [11, 'туз крести']
                     ]

    def pick_card(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


class Game:

    def __init__(self, p_1, p_2):
        self.player_1 = p_1
        self.player_2 = p_2

    def game_start(self, deck):
        for _ in range(2):
            self.get_card(deck, self.player_1)
            self.get_card(deck, self.player_2)
        print(self.player_1)

    def get_card(self, deck, player):
        card = deck.pick_card()
        if player.points > 21:
            card[0] = 1
        player.points += card[0]
        player.card_name.append(card[1])

    def winner(self):
        if self.player_1.points == 21 and self.player_2.points == 21:
            print('Ничья')
        elif self.player_1.points > 21 >= self.player_2.points:
            print('Победил', self.player_2.name)
        elif self.player_1.points <= 21 < self.player_2.points:
            print('Победил', self.player_1.name)
        elif self.player_1.points > self.player_2.points:
            print('Победил', self.player_1.name)
        elif self.player_1.points < self.player_2.points:
            print('Победил', self.player_2.name)
        else:
            print('Ничья')
        self.player_1.points = 0
        self.player_2.points = 0


player_1 = Player('PLAYER')
player_2 = Player('Computer')
deck = Deck()
game = Game(player_1, player_2)
a = deck.pick_card()
flag = True
while True:
    try:
        if flag:
            game.game_start(deck)
            flag = False
        if input('\nВведите "взять", чтобы взять ещё одну карту или "стоп", чтобы вскрыть карты: ').lower() == 'взять':
            game.get_card(deck, player_1)
            print(player_1)
        else:
            game.winner()
            if input('\nВведите "да", если желаете ещё партию: ').lower() == 'да':
                flag = True
                game.player_1 = player_1
                game.player_1.card_name = []
                game.player_2 = player_2
                game.player_2.card_name = []
                print(game.player_1.points)
            else:
                print('\n***Спасибо за игру!***')
                break
    except ValueError:
        print('В колоде закончились карты :(')
        if input('Обновить колоду? ').lower() == 'да':
            print(deck.deck)
            deck = Deck()
            print(deck.deck)
        else:
            print('Спасибо за игру!')
