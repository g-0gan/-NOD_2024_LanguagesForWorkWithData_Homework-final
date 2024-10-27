class Cell:
    """Класс для представления клетки на игровом поле."""

    def __init__(self, number):
        """
        Инициализирует клетку с заданным номером и пустым значением.

        :param number: Номер клетки от 1 до 9.
        """
        self.number = number
        self.value = str(number)  # Изначально клетка отображает свой номер

    def is_occupied(self):
        """Проверяет, занята ли клетка."""
        return self.value in {"X", "O"}

    def set_value(self, value):
        """Устанавливает значение клетки."""
        if not self.is_occupied():
            self.value = value


class Board:
    """Класс игрового поля, содержащий клетки и методы для взаимодействия с ними."""

    def __init__(self):
        """Создает игровое поле с нумерацией клеток от 1 до 9."""
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        """Выводит текущее состояние игрового поля."""
        print("\n".join([
            f"{self.cells[0].value} | {self.cells[1].value} | {self.cells[2].value}",
            "- + - + -",
            f"{self.cells[3].value} | {self.cells[4].value} | {self.cells[5].value}",
            "- + - + -",
            f"{self.cells[6].value} | {self.cells[7].value} | {self.cells[8].value}"
        ]))

    def check_winner(self):
        """Проверяет, есть ли победитель на доске."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
            (0, 4, 8), (2, 4, 6)  # диагонали
        ]
        for (x, y, z) in winning_combinations:
            if (self.cells[x].value == self.cells[y].value == self.cells[z].value) and self.cells[x].is_occupied():
                return self.cells[x].value  # Возвращает символ победителя (X или O)
        return None

    def is_full(self):
        """Проверяет, заполнено ли игровое поле."""
        return all(cell.is_occupied() for cell in self.cells)


class Player:
    """Класс игрока, представляющий его имя и символ (X или O)."""

    def __init__(self, name, symbol):
        """
        Инициализирует игрока с именем и символом.

        :param name: Имя игрока.
        :param symbol: Символ игрока ('X' или 'O').
        """
        self.name = name
        self.symbol = symbol

    def make_move(self, board, cell_number):
        """
        Делает ход, устанавливая значение клетки на доске.

        :param board: Игровое поле.
        :param cell_number: Номер клетки (1-9).
        """
        cell = board.cells[cell_number - 1]
        if not cell.is_occupied():
            cell.set_value(self.symbol)
            return True
        return False


def play_game():
    """Функция для управления игровым процессом."""
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")
    current_player = player1

    while True:
        board.display()
        print(f"Ходит {current_player.name} ({current_player.symbol})")

        try:
            move = int(input("Выберите клетку (1-9): "))
            if move < 1 or move > 9:
                print("Введите номер клетки от 1 до 9.")
                continue
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        if not current_player.make_move(board, move):
            print("Эта клетка уже занята. Попробуйте другую.")
            continue

        winner = board.check_winner()
        if winner:
            board.display()
            print(f"Победил {current_player.name} ({winner})!")
            break
        elif board.is_full():
            board.display()
            print("Ничья!")
            break

        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    play_game()
