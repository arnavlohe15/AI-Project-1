
class Agent:
    global grid
    def __init__(self, my_grid):
        grid = my_grid
        dim = len(grid)

        # INIT POS = [0,0], GOAL POS = [DIM-1, DIM-1]
        self.init_pos = [0, 0]
        self.goal_pos = [dim-1, dim-1]

        # SETUP FRINGE/CLOSED SET
        self.fringe = [] # unvisited nodes
        self.fringe.append(self.init_pos)
        self.closed = [] # visited nodes

    def dfs(self):
        while len(self.fringe) != 0:
            curr_pos = self.fringe.pop()
            if curr_pos == self.goal_pos:
                print ('Success!')


    def bfs(self):
        print('bfs')

    def a_star_euclidean(self):
        print('a_star_euclidean')


    def a_star_manhattan(self):
        print('a_star_manhattan')


    def bidirectional_bfs(self):
        print('bidirectional_bfs')



