from enum import Enum
import numpy as np


class AStarNode:
    def __init__(self, state, ptr, g, h):
        self.state = state
        self.ptr = ptr
        self.g = g  # g == depth
        self.h = h  # h == heuristic
        self.f = self.g + self.h


class AStarSearch:
    def __init__(self, start_state, solution):
        self.start_node = AStarNode(start_state, "", 0, 1000)
        self.end_node = AStarNode(solution, "", 1000, 0)
        self.node_vector = np.array()

    def expand_node(self, node):
        moves = self.get_legal_ops(node)
        for item in moves:
            print(item)

    @staticmethod
    def get_legal_ops(node):
        state = node.state
        colpos = state.player_pos_col
        rowpos = state.player_pos_row
        parent = node.ptr

        print(state.board)

        legal_ops = []
        moves = {
            'up': True,
            'down': True,
            'left': True,
            'right': True
        }

        if node.ptr:
            if colpos < parent.player_pos_col:  # moved left, don't right
                moves['right'] = False
            elif colpos > parent.player_pos_col:  # moved right, don't left
                moves['left'] = False
            elif rowpos > parent.player_pos_row:  # moved down, don't up
                moves['up'] = False
            elif rowpos < parent.player_pos_row:  # moved up, don't down
                moves['down'] = False

        if colpos > 2:  # On far right col, right illegal
            moves['right'] = False
        elif colpos < 1:  # On far left col, left illegal
            moves['left'] = False
        if rowpos > 2:  # On bottom row, down illegal
            moves['down'] = False
        elif rowpos < 1:  # On top row, up illegal
            moves['up'] = False

        for key in moves:
            if moves[key] is True:
                legal_ops.append(key)

        return legal_ops

    def search(self):
        pass

    def prune(self):
        pass
