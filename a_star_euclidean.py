import numpy as np

class node():

    def __init__(self, parent=None, location=None):
        self.parent = parent
        self.location = location

        self.g = float(0)
        self.h = float(0)
        self.f = float(0)

#returns euclidean distance between two nodes
#takes the locations of two nodes as arguments
def euclidean_distance(node_1, node_2):
    return float((((node_2[1] - node_1[1])**2) + ((node_2[0] - node_1[0])**2))**0.5)

#to make extracting the value at a given location in the grid easier
#takes the grid and two integers as arguments
def get_value(grid, a, b):
    return grid[a][b]

#Euclidean A* Search, takes the grid and dimension as arguments
def a_star_euclidean(grid, dim):
    #initializing start node and end node
    start = node(None, (0,0))
    end = node(None, (dim-1, dim-1))

    #initializing open list and closed list
    open_list = []
    closed_list = []
    open_list.append(start)

    while len(open_list) > 0:

        #assigning currentNode
        currentNode = open_list[0]
        currentNode_index = 0

        #current location
        for index, item in enumerate(open_list):
            if item.f < currentNode.f:
                currentNode = item
                currentNode_index = index

        print(currentNode.location)

        row = currentNode.location[0]
        column = currentNode.location[1]

        #updating open list and closed list
        open_list.pop(currentNode_index)
        closed_list.append(currentNode)

        #in case goal node is already reached
        if currentNode == end:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.location)
                current = current.parent
            #return path[::-1] #returning the path from start to end
            return path

        #generating neighbors
        neighbor_locations = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
        neighbor_nodes = [node(currentNode, location) for location in neighbor_locations]

        for neighbor in neighbor_nodes:


            #declaring row and column variables for neighbor nodes
            neighbor_row = int(neighbor.location[0])
            neighbor_column = int(neighbor.location[1])
            if (neighbor_row < dim and neighbor_row >= 0) and (neighbor_column < dim and neighbor_column >= 0): #to make sure that indices within range are being enqueued
                continue
            else:
                neighbor_nodes.remove(neighbor)

            # Child is on the closed list
            for closed_child in closed_list:
                if neighbor == closed_child:
                    continue


            #computing g(n), h(n), f(n)
            neighbor.g = float(currentNode.g + 1)
            neighbor.h = float(euclidean_distance(neighbor.location, end.location))
            neighbor.f = float(neighbor.g + neighbor.h)

            #child is in open list
            for open_node in open_list:
                if neighbor == open_node and neighbor.g > open_node.g:
                    continue

            """if (neighbor_row < dim and neighbor_row >= 0) and (neighbor_column < dim and neighbor_column >= 0): #to make sure that indices within range are being enqueued
                if (neighbor in closed_list) and (get_value(grid,neighbor_row,neighbor_column) == 0): #if child has not been visited already and is valid
                    continue
                if (neighbor in open_list) and (get_value(grid,neighbor_row,neighbor_column) == 0):
                    open_list.append(neigbor)
                    continue"""

            open_list.append(neighbor)

def main():
    grid = []
    dim = int(input("Enter the dimension of the game: "))
    print(type(dim))
    for row in range(dim):
        grid.append([])
        for column in range(dim):
            grid[row].append(int(np.random.binomial(1, 0.3, 1)))
            grid[0][0] = 0
    print(grid)
    print(a_star_euclidean(grid,dim))

main()
