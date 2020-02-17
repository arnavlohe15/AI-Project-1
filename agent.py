
class Agent:
    def __init__(self, grid):
        # STORE GRID
        self.grid = grid

        dim = len(grid)

        # INIT POS = [0,0], GOAL POS = [DIM-1, DIM-1]
        self.init_pos = (0, 0)
        self.goal_pos = (dim-1, dim-1)

        # SETUP FRINGE/CLOSED SET
        self.fringe = [] # unvisited nodes
        self.fringe.append(self.init_pos)
        self.closed = [] # visited nodes

    def dfs(self):
        # fringe is stack
        while len(self.fringe) != 0: # while fringe is not empty
            curr_pos = self.fringe.pop() # get current state
            if curr_pos == self.goal_pos:
                print("Success!")
                print("Current pos: ", curr_pos)
                print("Path: ", self.closed)
                return self.closed
            else:
                for child in self.get_children(curr_pos):
                    out_of_bounds = child[0] < 0 or \
                                    child[0] >= len(self.grid) or \
                                    child[1] < 0 or \
                                    child[1] >= len(self.grid)
                    if not out_of_bounds:
                        invalid = self.grid[child[0]][child[1]] == 1
                        if not invalid and child not in self.closed:
                            self.fringe.append(child)
                self.closed.append(curr_pos)
        print("No solution")
        return []

    def bfs(self):
        # fringe is stack
        while len(self.fringe) != 0:  # while fringe is not empty
            curr_pos = self.fringe.pop(0)  # get current state
            if curr_pos == self.goal_pos:
                print("Success!")
                print("Current pos: ", curr_pos)
                print("Path: ", self.closed)
                return self.closed
            else:
                for child in self.get_children(curr_pos):
                    out_of_bounds = child[0] < 0 or \
                                    child[0] >= len(self.grid) or \
                                    child[1] < 0 or \
                                    child[1] >= len(self.grid)
                    if not out_of_bounds:
                        invalid = self.grid[child[0]][child[1]] == 1
                        if not invalid and child not in self.closed:
                            self.fringe.append(child)
                self.closed.append(curr_pos)
        print("No solution")
        return []

    def a_star_euclidean(self):
        print('a_star_euclidean')

    def a_star_manhattan(self):
        print('a_star_manhattan')

    def bidirectional_bfs(self):
        print('bidirectional_bfs')

    def get_children(self, curr_pos):
        row = curr_pos[0] # access row of tuple
        col = curr_pos[1] # access col of tuple
        return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]


