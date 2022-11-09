class Player:

    def __init__(self, name, point=None):
        self.name = name
        self.go_point = point


class Board:

    def __init__(self):
        self.board = list(range(1, 10))

    def __str__(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.board[0 + i * 3], '|', self.board[1 + i * 3], '|', self.board[2 + i * 3], '|')
            print('-' * 13)
        return ' '

    def check_cell(self, player):
        if 1 <= player.go_point <= 9:
            if isinstance(self.board[player.go_point - 1], int):
                self.board[player.go_point - 1] = player.name
                return True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Введите число от 1 до 9')

    def step(self, player):
        valid = False
        while not valid:
            try:
                print(self)
                player.go_point = int(input('Куда поставим: ' + player.name + '? '))
                valid = self.check_cell(player)
            except ValueError:
                print('Некорректный ввод, попробуйте ещё раз')

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i_sym in win_coord:
            if self.board[i_sym[0]] == self.board[i_sym[1]] == self.board[i_sym[2]]:
                print(self, 'YPA')
                return False
        return True


def start_game(game, p_1, p_2):
    count_step = 0
    for _ in range(9):
        if count_step % 2 == 0:
            game.step(p_1)
        else:
            game.step(p_2)
        count_step += 1
        if count_step > 4:
            flag = game.check_win()
            if not flag:
                break


player_1 = Player('X')
player_2 = Player('O')
new_game = Board()
start_game(new_game, player_1, player_2)
