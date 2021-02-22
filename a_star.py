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
        self.start_node = AStarNode(start_state, "", 0, 0)
        self.start_node.h = self.manhattan(self.start_node)
        self.start_node.f = self.start_node.h
        self.end_node = AStarNode(solution, "", 1000, 0)
        self.open_list = []
        self.open_list.append(self.start_node)
        self.closed_list = []
        self.nodes_visited = 0

    def expand_node(self, node):
        moves = self.get_legal_ops(node)

        for item in moves:
            # print(item)
            new_node = self.create_successor(node)

            if item == "up":
                new_node.state = new_node.state.move_up()
            elif item == 'down':
                new_node.state = new_node.state.move_down()
            elif item == "left":
                new_node.state = new_node.state.move_left()
            elif item == "right":
                new_node.state = new_node.state.move_right()

            new_node.h = self.manhattan(new_node)
            new_node.f = new_node.g + new_node.h
            self.open_list.append(new_node)

        # bestnode = self.choose_bestnode()
        # for item in self.open_list:
        #     print(item.f)

    @staticmethod
    def create_successor(node):
        new_node = AStarNode(node.state, node, node.g + 1, node.h)
        return new_node

    @staticmethod
    def get_legal_ops(node):
        state = node.state
        colpos = state.player_pos_col
        rowpos = state.player_pos_row
        parent = node.ptr

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

    @staticmethod
    def manhattan(node):
        solpos = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (0, 3),
                  '5': (1, 0), '6': (1, 1), '7': (1, 2), '8': (1, 3),
                  '9': (2, 0), '10': (2, 1), '11': (2, 2), '12': (2, 3),
                  '13': (3, 0), '14': (3, 1), '15': (3, 2), '0': (3, 3)
                  }
        h = node.h
        for col in range(0, 4):
            for row in range(0, 4):
                tile = node.state.board[col][row]
                endpos = solpos[tile]
                solcol = endpos[0]
                solrow = endpos[1]
                h += abs(solcol - col)
                h += abs(solrow - row)
        h *= 10
        # print(h)
        return h

    def choose_bestnode(self):
        self.open_list.sort(key=lambda x: x.f)
        for item in self.open_list:
            print(item.f)
        bestnode = self.open_list.pop(0)
        self.nodes_visited += 1
        self.close_list.append(bestnode)
        return bestnode

    def search(self):
        solved = False
        while solved is False:
            if not self.open_list:
                print("Failure")
                exit()
            bestnode = self.choose_bestnode()
            if bestnode.state.is_solved(self.end_node.state):
                solved = True
                break
            
        print("Puzzle solved")
        print("Steps: ", bestnode.g)
        print("Nodes visited: ", self.nodes_visited)
        exit()


    def prune(self):
        pass
