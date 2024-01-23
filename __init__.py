# количество клеток
board_size = 3

# игровое поле
game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    '''Выводим игровое поле(рисунок поля для игры)'''
    print('____' * board_size)
    for i in range(board_size):
        print((' ' * board_size + '|') * board_size)
        print('', game_board[i * board_size], '|', game_board[1 + i * board_size], '|',
              game_board[2 + i * board_size], '|')
        print(('_' * board_size + '|') * board_size)


def game_step(index, char):
    '''следующий ход игры, где char это следующий символ для ввода'''
    if (index > 10 or index < 1 or game_board[index - 1] in ('X', 'O')):
        return False
    game_board[index - 1] = char
    return True


def check_win():
    '''проверка условия выигрыша игроков'''
    win = False
    # создаем кортеж из координат выигрышных комбинаций
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # выигрышные горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # выигрышные вертикальные линии
        (0, 4, 8), (2, 4, 6)              # выигрышные диагональные линии
    )

    for pos in win_combination:
        if (game_board[pos[0]] == game_board[pos[1]] and
            game_board[pos[1]] == game_board[pos[2]]):

                win = game_board[pos[0]]

    return win



def start_game():
    '''Вызываем игровое поле'''
    current_player = 'X'  # текущий игрок
    step = 1  # номер шага
    draw_board()
    while ((step < 10) and (check_win() == False)):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля(0 - выход):')

        if (int(index) == '0'):
            break

        # если получается сделать шаг
        if (game_step(int(index), current_player)):
            print('Следующий ход')

            if (current_player == 'X'):  # определяем кто ходит следующим
                current_player = 'O'
            else:
                current_player = 'X'
            draw_board()  # Выводим этот ход
            step += 1  # следующая итерация хода
        else:
            print('Неверный ход, повторите ввод!!!')
    if (step == 10):
        print('Игра окончена ничьей!')
    else:
        print('Выиграл ' + check_win())


print("Добро пожаловать в игру!!!")
start_game()
