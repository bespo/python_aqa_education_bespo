import sys
import logging

from tictactoe import EMPTY_SPOT, PLAYER_ONE, INCORRECT_INPUT_ERROR, SPOT_ALREADY_TAKEN_ERROR, PLAYER_TWO


class Loggers:
    def __init__(self, filename):
        self.filename = filename
        logging.basicConfig(
            filename=self.filename,
            filemode='a',
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def write_log(message):
        print(message)
        logging.info(message)

    def read_log(self):
        f = open(self.filename, "r")
        print(f.read())

    def clean_log(self):
        open(self.filename, 'w').close()


class CellNotAvailableEx(Exception):
    def __init__(self):
        self.message = GAME.SPOT_ALREADY_TAKEN_ERROR

    def __str__(self):
        return self.message


class WrongCommandEx(Exception):
    def __init__(self):
        self.message = GAME.INCORRECT_INPUT_ERROR

    def __str__(self):
        return self.message


class TicTacToe:
    EMPTY_SPOT = ' [ ] '
    PLAYER_ONE = '  X  '
    PLAYER_TWO = '  O  '
    INCORRECT_INPUT_ERROR = 'Please enter correct number in range 1-9.'
    SPOT_ALREADY_TAKEN_ERROR = 'This spot is already taken.'

    def __init__(self):
        self.logger = Loggers("games.log")

    class Render:

        def __init__(self, game_instance):
            self.game_instance = game_instance
            self.logger = Loggers("games.log")
            self.clear_board()

        def set_board(self, board):
            self.game_instance.board = board

        def get_board(self):
            return self.game_instance.board

        def display_board(self):
            print(''.join(self.get_board()[:3]))
            print(''.join(self.get_board()[3:6]))
            print(''.join(self.get_board()[6:]))

        def clear_board(self):
            self.set_board([EMPTY_SPOT for i in range(9)])

        def clear_screen(self):
            print('\n' * 10)

    class Game:
        current_player = PLAYER_ONE
        board = None

    class GameLogic:

        def __init__(self, game_instance):
            self.game_instance = game_instance
            self.logger = Loggers("games.log")

        def get_current_player(self):
            return self.game_instance.current_player

        def set_current_player(self, player):
            self.game_instance.current_player = player

        def get_board(self):
            return self.game_instance.board

        def handle_player_move(self):
            position = self.get_player_move()
            self.set_player_position(self.get_board(), position)

        def get_player_move(self):
            while True:
                position = input(f'Player {self.get_current_player()} please enter a number 1-9: ')
                position = get_user_input_as_int(position)
                if position is None or position not in range(9):
                    print(INCORRECT_INPUT_ERROR)
                    continue
                if self.check_is_spot_is_empty(position):
                    return position
                else:
                    print(SPOT_ALREADY_TAKEN_ERROR)

        def set_player_position(self, board, position):
            board[position] = self.get_current_player()

        def check_is_spot_is_empty(self, position):
            return self.get_board()[position] == EMPTY_SPOT

        def check_for_end_of_game(self):
            if self.check_for_win_condition_match(PLAYER_ONE) or self.check_for_win_condition_match(PLAYER_TWO):
                return True

        def check_for_win_condition_match(self, player):
            board = self.get_board()
            win_conditions = board[:3], board[3:6], board[6:], board[::3], board[1::3], board[2::3], board[::4], board[
                                                                                                                 2:7:2]

            for win_condition in win_conditions:
                if win_condition.count(player) == 3:
                    print(f'Player {player} is a winner')
                    return True

        def switch_player(self):
            self.set_current_player(PLAYER_ONE if self.get_current_player() == PLAYER_TWO else PLAYER_TWO)

    def play_game(self):
        game_instance = self.Game()
        render = self.Render(game_instance)
        logic = self.GameLogic(game_instance)
        render.display_board()
        while True:
            logic.handle_player_move()
            render.clear_screen()
            render.display_board()
            if logic.check_for_end_of_game():
                return
            logic.switch_player()

    def check_history(self):
        print("Here is wins history:")
        self.logger.read_log()

    def clean_history(self):
        self.logger.clean_log()
        print("History was cleared")


def get_user_input_as_int(value):
    try:
        value = int(value)
    except ValueError:
        return None
    return value - 1


# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         Loggers.write_log("Total session time is: %d seconds" % (end - start))
#
#     return wrapper
#
#
# @timer
# def main():
#     GAME = TicTacToe()
#     while True:
#         if not TicTacToe.GameLogic():
#             break


GAME = TicTacToe()


def run_game():
    while True:
        print('\nChoose an action:\n1. Play\n2. Check history\n3. Clean history\n4. Exit')
        choice = get_user_input_as_int(input('Select an option:\n'))
        if choice in range(4):
            if choice == 1:
                GAME.play_game()
            elif choice == 2:
                TicTacToe.check_history()
                GAME.set_current_player = "game_ready"
            elif choice == 3:
                TicTacToe.clean_history()
                GAME.set_current_player = "game_ready"
            elif choice == 4:
                print("Bye!")
                sys.exit()


if __name__ == '__main__':
    run_game()
