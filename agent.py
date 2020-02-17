import math


class node():
    def __init__(self, parent, location):
        self.parent = parent
        self.location = location

        self.g = float(0)
        self.h = float(0)
        self.f = float(0)

    def __eq__(self, other):
        return self.location == other.location

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
                #print("Current pos: ", curr_pos)
                #print("Path: ", self.closed)
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
                #print("Current pos: ", curr_pos)
                #print("Path: ", self.closed)
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

    ## HELPER CLASS / FUNCTIONS FOR A* ##

    # returns euclidean distance between two nodes
    # takes the locations/tuples of two nodes as arguments
    def euclidean_distance(self, node_1, node_2):
        return float((((node_2[1] - node_1[1]) ** 2) + ((node_2[0] - node_1[0]) ** 2)) ** 0.5)

    # returns manhattan distance between two nodes
    # takes the locations/tuples of two nodes as arguments
    def manhattan_distance(self, node_1, node_2):
        return abs(node_1[0] - node_2[0]) + \
               abs(node_1[1] - node_2[1])


    # to make extracting the value at a given location in the maze easier
    # takes the maze and two integers as arguments
    def get_value(self, maze, a, b):
        return maze[a][b]

    def is_out_of_bounds(self, a, b, dim):
        return (a < 0 or a >= dim) or (b < 0 or b >= dim)

    # Euclidean A* Search, takes the maze and dimension as arguments
    def a_star_euclidean(self):
        maze = self.grid
        dim = len(self.grid)
        # initializing start node and end node
        start = node(None, (0, 0))
        end = node(None, (dim - 1, dim - 1))

        # initializing open list and closed list
        open_list = []
        closed_list = []
        open_list.append(start)

        while len(open_list) > 0:

            # assigning currentNode
            currentNode = open_list[0]
            currentNode_index = 0

            # current location - finding node with lowest f(n)
            for index, item in enumerate(open_list):
                if item.f < currentNode.f:
                    currentNode = item
                    currentNode_index = index

            # (currentNode.location)
            row = currentNode.location[0]
            column = currentNode.location[1]

            # updating open list and closed list
            open_list.pop(currentNode_index)
            closed_list.append(currentNode)

            # in case goal node is already reached
            if currentNode.location == end.location:
                path = []
                current = currentNode
                while current is not None:
                    path.append(current.location)
                    current = current.parent
                # return path[::-1] #returning the path from start to end
                path.reverse()
                print("Success!")
                return path
            else:
                closed_list.append(currentNode)

            # generating children
            child_locations = [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]
            # print(child_locations)
            child_nodes = [node(currentNode, location) for location in child_locations]
            # print(child_nodes)

            for child in child_nodes:
                # declaring row and column variables for child nodes
                child_row = int(child.location[0])
                child_column = int(child.location[1])

                if not self.is_out_of_bounds(child_row, child_column, dim):

                    # Child is on the closed list
                    if child in open_list:
                        continue

                    # computing g(n), h(n), f(n)
                    child.g = float(currentNode.g + 1)
                    child.h = float(self.euclidean_distance(child.location, end.location))
                    child.f = float(child.g + child.h)

                    # child is in open list
                    if child in closed_list:
                        continue

                    # included the second condition, remove if A* doesn't work
                    if self.get_value(maze, child_row, child_column) == 0 and child not in closed_list:
                        open_list.append(child)
                    else:
                        continue

                else:
                    continue

    def a_star_manhattan(self):
        maze = self.grid
        dim = len(self.grid)

        # initializing start node and end node
        start = node(None, (0, 0))
        end = node(None, (dim - 1, dim - 1))

        # initializing open list and closed list
        open_list = []
        closed_list = []
        open_list.append(start)

        while len(open_list) > 0:

            # assigning currentNode
            currentNode = open_list[0]
            currentNode_index = 0

            # current location - finding node with lowest f(n)
            for index, item in enumerate(open_list):
                if item.f < currentNode.f:
                    currentNode = item
                    currentNode_index = index

            # (currentNode.location)
            row = currentNode.location[0]
            column = currentNode.location[1]

            # updating open list and closed list
            open_list.pop(currentNode_index)
            closed_list.append(currentNode)

            # in case goal node is already reached
            if currentNode.location == end.location:
                path = []
                current = currentNode
                while current is not None:
                    path.append(current.location)
                    current = current.parent
                # return path[::-1] #returning the path from start to end
                path.reverse()
                print("Success!")
                return path
            else:
                closed_list.append(currentNode)

            # generating children
            child_locations = [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]
            # print(child_locations)
            child_nodes = [node(currentNode, location) for location in child_locations]
            # print(child_nodes)

            for child in child_nodes:
                # declaring row and column variables for child nodes
                child_row = int(child.location[0])
                child_column = int(child.location[1])

                if not self.is_out_of_bounds(child_row, child_column, dim):

                    # Child is on the closed list
                    if child in open_list:
                        continue

                    # computing g(n), h(n), f(n)
                    child.g = float(currentNode.g + 1)
                    child.h = float(self.manhattan_distance(child.location, end.location))
                    child.f = float(child.g + child.h)

                    # child is in open list
                    if child in closed_list:
                        continue

                    # included the second condition, remove if A* doesn't work
                    if self.get_value(maze, child_row, child_column) == 0 and child not in closed_list:
                        open_list.append(child)
                    else:
                        continue

                else:
                    continue

    def bidirectional_bfs(self):
        print('bidirectional_bfs')

    def get_children(self, curr_pos):
        row = curr_pos[0] # access row of tuple
        col = curr_pos[1] # access col of tuple
        return [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]


