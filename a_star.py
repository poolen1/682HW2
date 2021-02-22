
class AStarNode:
    def __init__(self, state, ptr, g, h):
        self.state = state
        self.ptr = ptr
        self.g = g  # g == depth
        self.h = h  # h == heuristic
        self.f = self.g + self.h


class AStarSearch:
    def __init__(self, start_state, solution):
        start_node = AStarNode(start_state, "", 0, 0)

        pass
