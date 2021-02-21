import numpy as np


class Puzzle:
    def __init__(self, file=None):
        self.rows = 4
        self.cols = 4
        self.board = []
        self.solution = []
        self.player_pos_col = 0
        self.player_pos_row = 0

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
        self.player_pos_row, self.player_pos_col = self.get_player_position()

        # Get solution
        i = 0
        for col in range(self.cols):
            solution_row = []
            for row in range(self.rows):
                solution_row.append('i')
                i += 1
            self.solution.append(solution_row)

    def get_player_position(self):
        for col in range(self.cols):
            for row in range(self.rows):
                if self.board[col][row] == '0':
                    pos_row = col
                    pos_col = row
                    return pos_row, pos_col

    def is_solved(self):
        if self.board == self.solution:
            return True
        else:
            return False

    def move_up(self):
        posrow = self.player_pos_row
        poscol = self.player_pos_col
        if self.player_pos_row == 0:
            return print("Illegal move")
        else:
            self.board[posrow][poscol], self.board[posrow - 1][poscol]\
                = self.board[posrow - 1][poscol], self.board[posrow][poscol]
            self.player_pos_row, self.player_pos_col \
                = self.get_player_position()

    def move_down(self):
        posrow = self.player_pos_row
        poscol = self.player_pos_col
        if self.player_pos_row == 3:
            return print("Illegal move")
        else:
            self.board[posrow][poscol], self.board[posrow + 1][poscol] \
                = self.board[posrow + 1][poscol], self.board[posrow][poscol]
            self.player_pos_row, self.player_pos_col \
                = self.get_player_position()

    def move_left(self):
        posrow = self.player_pos_row
        poscol = self.player_pos_col
        if self.player_pos_col == 0:
            return print("Illegal move")
        else:
            self.board[posrow][poscol], self.board[posrow][poscol - 1] \
                = self.board[posrow][poscol - 1], self.board[posrow][poscol]
            self.player_pos_row, self.player_pos_col \
                = self.get_player_position()

    def move_right(self):
        posrow = self.player_pos_row
        poscol = self.player_pos_col
        if self.player_pos_col == 3:
            return print("Illegal move")
        else:
            self.board[posrow][poscol], self.board[posrow][poscol + 1] \
                = self.board[posrow][poscol + 1], self.board[posrow][poscol]
            self.player_pos_row, self.player_pos_col \
                = self.get_player_position()


