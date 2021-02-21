import numpy as np


class Puzzle:
    def __init__(self, file=None):
        self.rows = 4
        self.cols = 4
        self.board = []
        self.solution = []
        self.player_position = (0, 0)

        # Set up board randomly
        if file is None:
            n = np.random.choice(range(16), 16, replace=False)
            i = 0
            for col in range(self.cols):
                board_row = []
                for row in range(self.rows):
                    board_row.append(str(n[i]))
                    i += 1
                self.board.append(board_row)
        # Set up board with file
        else:
            for line in file.readlines():
                self.board.append(line.split())
        # Get player pos
        self.player_position = self.get_player_position()
        # Get solution


    def get_player_position(self):
        for col in range(self.cols):
            for row in range(self.rows):
                if self.board[col][row] == '0':
                    pos = (col, row)
                    return pos

    def is_solved(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass


