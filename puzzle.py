
class Puzzle:
    def __init__(self, board=None):
        self.rows = 4
        self.cols = 4
        self.board = [[] * self.cols] * self.rows
        if board is None:
            pass  # init board with rand
        else:
            self.board = board
