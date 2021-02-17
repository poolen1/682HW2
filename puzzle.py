
class Puzzle:
    def __init__(self, board=None):
        self.rows = 4
        self.cols = 4
        if board is None:
            self.board = [[]*self.cols]*self.rows
