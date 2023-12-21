from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    # Открыть файл results.txt в режиме «добавление».
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    file = open('results.txt', 'a', encoding='utf-8')
    # Записать в файл содержимое переменной result.
    file.write(result + '\n')
    file.close()

def main():
    # Создать игровое поле - объект класса Board.
    game = Board()

    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True

    # Отрисовать поле в терминале.
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')
        
        # Запускается бесконечный цикл.
        while True:

            try:
        # Тут пользователь вводит координаты ячейки.
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError

            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                
                continue
            # Если в блоке try исключения не возникло...

            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue

            except ValueError:
                # ...выводятся сообщения...
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')

                continue
            
            except Exception as e:
                print(f'Возникла ошибка: {e}')

            else:
                # ...значит введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        # Разместить на поле символ по указанным координатам — сделать ход.
        game.make_move(row, column, current_player)
        
        print('Ход сделан!')
        # Перерисовать поле с учётом сделанного хода.
        game.display()

        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            # Сформировать строку.
            result = f'Победили {current_player}.'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False
        elif game.is_board_full():
            # Сформировать строку.
            result = 'Ничья!'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False

        # Тернарный оператор, через кототорый реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'



if __name__ == '__main__':
    main()



