import numpy as np


class AStarNode:
    def __init__(self, state, ptr, g, h):
        self.state = state
        self.ptr = ptr
        self.g = g  # g == depth
        self.h = h  # h == heuristic
        self.f = self.g + self.h
        self.successors = []


class DFSNode:
    def __init__(self, state, ptr, depth):
        self.state = state
        self.ptr = ptr
        self.d = depth


class AStarSearch:
    def __init__(self, start_state, solution):
        self.start_node = AStarNode(start_state, None, 0, 0)
        self.start_node.h = self.manhattan(self.start_node)
        self.start_node.f = self.start_node.h
        self.end_node = AStarNode(solution, "", 1000, 0)
        self.open_list = []
        self.open_list.append(self.start_node)
        self.closed_list = []
        self.nodes_visited = 0

    def expand_node(self, bestnode):
        # print("expand successors: ", bestnode.successors)
        if bestnode.successors:
            self.closed_list.append(bestnode)
            return
        moves = self.get_legal_ops(bestnode)

        # for succ in bestnode.successors:
        #     # print("first", succ.state, succ.f)
        # bestnode.successors = []

        # # print("start successors: ", len(bestnode.successors))

        for item in moves:
            # # print(item)
            new_node = self.create_successor(bestnode)

            if item == "up":
                # print('up')
                new_node.state = new_node.state.move_up()
            elif item == 'down':
                # print('down')
                new_node.state = new_node.state.move_down()
            elif item == "left":
                # print('left')
                new_node.state = new_node.state.move_left()
            elif item == "right":
                # print('right')
                new_node.state = new_node.state.move_right()

            is_dupe = self.is_dupe(new_node)
            # # print(is_dupe)
            if is_dupe:
                if is_dupe[2] == 'open':
                    old = is_dupe[1]
                    if new_node.g > old.g:
                        # print("open dupe better path: ", new_node.g, old.g)
                        old.ptr = new_node.ptr
                        new_node = old
                    self.open_list.remove(old)
                    # print("removed old from open")
                elif is_dupe[2] == 'closed':
                    old = is_dupe[1]
                    # # print("old")
                    if new_node.g > old.g:
                        # print("closed dupe better path: ", new_node.g, old.g)
                        old.ptr = new_node.ptr
                        new_node = old
                        # self.propagate_closed_old(old)
                    self.closed_list.remove(old)
                    # print("removed old from closed")

            new_node.h = self.manhattan(new_node)
            new_node.f = new_node.g + new_node.h
            # # print(new_node.state, new_node.f)

            valid_successor = True
            if bestnode.successors:
                valid_successor = False
                for node in bestnode.successors:
                    if new_node.state.board == node.state.board:
                        if new_node.f < node.f:
                            bestnode.successors.remove(node)
                            valid_successor = True
                    else:
                        valid_successor = True

            # print(bestnode.successors)
            # # print('successor count', len(bestnode.successors))
            # print(valid_successor)

            if valid_successor:
                bestnode.successors.append(new_node)

        self.open_list += bestnode.successors

        # bestnode = self.choose_bestnode()
        # for item in self.open_list:
        #     # print(item.state.board)
        #     # print(item.f)
        # exit()

    @staticmethod
    def create_successor(node):
        new_node = AStarNode(node.state, node, node.g + 1, node.h)
        new_node.successors = []
        # # print(new_node.state, new_node.g)
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
            if colpos < parent.state.player_pos_col:  # moved left, don't right
                moves['right'] = False
            elif colpos > parent.state.player_pos_col:  # moved right, don't left
                moves['left'] = False
            elif rowpos > parent.state.player_pos_row:  # moved down, don't up
                moves['up'] = False
            elif rowpos < parent.state.player_pos_row:  # moved up, don't down
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
        h = 0
        for col in range(0, 4):
            for row in range(0, 4):
                tile = node.state.board[col][row]
                endpos = solpos[tile]
                solcol = endpos[0]
                solrow = endpos[1]
                h += abs(solcol - col)
                h += abs(solrow - row)
        h *= 10
        # # print(h)
        return h

    def choose_bestnode(self):
        self.open_list.sort(key=lambda x: x.f, reverse=True)
        dupecount = 0
        closedcount = 0
        open_length = len(self.open_list)
        closed_length = len(self.closed_list)
        open_remove_list = []
        closed_remove_list = []
        bestnode = self.open_list.pop()
        if bestnode.successors:
            low = bestnode
            for node in bestnode.successors:
                if node.f < low.f:
                    low = node
            if low == bestnode:
                bestnode = self.choose_bestnode()
            else:
                bestnode = low
        # print("========")
        # # print("Bestnode Successors: ", bestnode.successors)
        # # print("Count: ", len(bestnode.successors))
        for i in range(0, len(self.open_list)):
            if bestnode.state.board == self.open_list[i].state.board:
                dupecount += 1
        for i in range(0, len(self.closed_list)):
            if bestnode.state.board == self.closed_list[i].state.board:
                closedcount += 1
        # print("bestnode: ", bestnode.f)
        # print("open dupecount: ", dupecount)
        # print("closed dupecount: ", closedcount)
        # print("========")
        self.prune(bestnode)
        self.closed_list.append(bestnode)
        return bestnode

    def search(self):
        solved = False
        while solved is False:
            if not self.open_list:
                # print("Failure")
                exit()
            bestnode = self.choose_bestnode()
            self.nodes_visited += 1
            # print("nodes visited: ", self.nodes_visited)
            # print("open list: ", len(self.open_list))
            # ("bestnode: ", bestnode.state, bestnode.f)
            if bestnode.state.is_solved(self.end_node.state.board):
                # print("solved")
                solved = True
                continue
            # print("to expand successors: ", bestnode.successors)
            self.expand_node(bestnode)

        print("Puzzle solved")
        print("Steps: ", bestnode.g)
        print("Nodes visited: ", self.nodes_visited)
        print(self.start_node.state.board)
        print(bestnode.state.board)
        return

    def is_dupe(self, node):
        duplicate = False
        for open_node in self.open_list:
            if node.state.board == open_node.state.board:
                # print("open dupe: ", self.nodes_visited)
                duplicate = True
                return duplicate, open_node, 'open'

        for closed_node in self.closed_list:
            if node.state.board == closed_node.state.board:
                # print('closed dupe: ', self.nodes_visited)
                duplicate = True
                return duplicate, closed_node, 'closed'
        return duplicate

    @staticmethod
    def propagate_closed_old(old):
        start_node = DFSNode(old, None, 0)
        d_limit = 1000
        open_list = [start_node]
        closed_list = []
        while True:
            if not open_list:
                return
            # # print(open_list)
            n = open_list.pop(0)
            # # print(n)
            closed_list.append(n)

            if n.d <= d_limit:  # d is less than Depth limit
                if n.state.successors:  # if n has successors
                    for successor in n.state.successors:  # for each successor
                        # if successor points to n, or successor is more expensive,
                        # update new node and continue propagation
                        if successor.ptr == n.state or successor.g < n.state.g:
                            new_node = DFSNode(successor, n, n.d + 1)
                            new_node.state.g = n.state.g + 1
                            new_node.state.f = new_node.state.g + new_node.state.h
                            open_list.append(new_node)

    def prune(self, bestnode):
        cutoff_value = bestnode.f * 10
        cutoff_index = 0
        maxf = 0
        for i in range(0, len(self.open_list)):
            node = self.open_list[i]
            if node.f > maxf:
                maxf = node.f
            if node.f >= cutoff_value:
                print("cutoff: ", node.f)
                cutoff_index = i
                del self.open_list[cutoff_index:]
                break
        # print("bestnode: ", bestnode.f)
        # print('max: ', maxf)

    def get_path(self):
        pass
