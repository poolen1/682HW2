import numpy as np


class Puzzle:
    def __init__(self, file=None):
        self.rows = 4
        self.cols = 4
        self.board = []
        self.solution = []
        self.player_pos_col = 0
        self.player_pos_row = 0

        solvable = False
        while not solvable:
            self.init_board(file)
            # Get player pos
            self.player_pos_row, self.player_pos_col = \
                self.get_player_position()
            # Check for solvability
            solvable = self.is_solvable()
            print("is solvable: ", solvable)
            if (file is not None) & solvable is False:
                exit()

        # Get solution
        i = 1
        for col in range(self.cols):
            solution_row = []
            for row in range(self.rows):
                solution_row.append(str(i))
                i += 1
            self.solution.append(solution_row)
        self.solution[3][3] = '0'
        print(self.solution)

    def init_board(self, file):
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

    def get_player_position(self):
        for col in range(self.cols):
            for row in range(self.rows):
                if self.board[col][row] == '0':
                    pos_row = col
                    pos_col = row
                    return pos_row, pos_col

    def is_solvable(self):
        solvable = False
        inv_count = self.count_inversions()
        print("inversions: ", inv_count)
        print("pos row: ", self.player_pos_row % 2)
        if self.player_pos_row % 2 == 0:  # Empty pos is on even row
            # odd number of inversions
            # print ("inv_count: ", inv_count % 2)
            if inv_count % 2 == 1:
                solvable = True
        else:  # Empty pos is on odd row
            # even number of inversions
            if inv_count % 2 == 0:
                solvable = True
        # print("is_solvable: ", solvable)
        return solvable

    def count_inversions(self):
        inv_count = 0
        arr = []
        for idn, n in np.ndenumerate(self.board):
            arr.append(n)
        for i in range(len(arr)):
            # print("i: ", i)
            if arr[i].astype(np.int) == 0:
                continue
            for j in range(i + 1, 16):
                # print("i, j, n, m: ", i, j, arr[i], arr[j])
                if arr[j].astype(np.int) == 0:
                    continue
                if arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

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


