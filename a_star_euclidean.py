import numpy as np

class node():

    def __init__(self, parent=None, location=None):
        self.parent = parent
        self.location = location

        self.g = float(0)
        self.h = float(0)
        self.f = float(0)

#returns euclidean distance between two nodes
#takes the locations/tuples of two nodes as arguments
#works properly
def euclidean_distance(node_1, node_2):
    return float((((node_2[1] - node_1[1])**2) + ((node_2[0] - node_1[0])**2))**0.5)

#to make extracting the value at a given location in the maze easier
#takes the maze and two integers as arguments
def get_value(maze, a, b):
    return maze[a][b]

def out_of_bounds(a, b, dim):
    return (a < 0 or a >= dim) or (b < 0 or b >= dim)

#Euclidean A* Search, takes the maze and dimension as arguments
def a_star_euclidean(maze, dim):
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

        #print(currentNode.location)

        row = currentNode.location[0]
        column = currentNode.location[1]

        #updating open list and closed list
        open_list.pop(currentNode_index)
        closed_list.append(currentNode)

        #in case goal node is already reached
        if currentNode.location == end.location:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.location)
                current = current.parent
            #return path[::-1] #returning the path from start to end
            return path

        #generating childs
        child_locations = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
        #print(child_locations)
        child_nodes = [node(currentNode, location) for location in child_locations]
        #print(child_nodes)

        for child in child_nodes:
            #declaring row and column variables for child nodes
            child_row = int(child.location[0])
            child_column = int(child.location[1])

            if not out_of_bounds(child_row, child_column, dim):

                # Child is on the closed list
                if child in open_list:
                    continue

                #computing g(n), h(n), f(n)
                child.g = float(currentNode.g + 1)
                child.h = float(euclidean_distance(child.location, end.location))
                child.f = float(child.g + child.h)

                #child is in open list
                if child in closed_list:
                    continue

                open_list.append(child)

            else:
                continue


def main():
    maze = []
    dim = int(input("Enter the dimension of the game: "))
    print(dim)
    for row in range(dim):
        maze.append([])
        for column in range(dim):
            maze[row].append(int(np.random.binomial(1, 0.3, 1)))
    maze[0][0] = 0
    maze[dim-1][dim-1] = 0
    print(maze)
    print(a_star_euclidean(maze,dim))

    #print(euclidean_distance((1,1), (2,2)))

main()
