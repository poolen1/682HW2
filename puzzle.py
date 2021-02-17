import numpy as np


class Puzzle:
    def __init__(self, board=None):
        self.rows = 4
        self.cols = 4
        self.board = [[0] * self.cols] * self.rows
        if board is None:
            for row in range(self.rows):
                for col in range(self.cols):
                    n = np.random.randn()
                    self.board[row][col] = n
        else:
            self.board = board
