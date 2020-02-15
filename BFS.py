import numpy as np

#************************************************************************************************************************
#creating 2d grid
grid = []
dim = int(input("Enter the dimension of the game: "))
print(type(dim))
for row in range(dim):
    grid.append([])
    for column in range(dim):
        grid[row].append(int(np.random.binomial(1, 0.3, 1)))
        #grid[row].append(node((int(np.random.binomial(1, 0.3, 1)[0])), False))
        #inserting binomial random variable
#grid[0][0] = node(0, False)
grid[0][0] = 0
#print(grid[0][3].visited)
#print(grid[0][4])
#print((1,5)[1]) #square brackets are indexes for tuple

#************************************************************************************************************************
#to make extracting the value at a given location in the grid easier
def get_value(a, b):
    return grid[a][b]

#************************************************************************************************************************
#Declaring and initializing queue and visited lists for BFS/both will store tuple (row, column)
#Q.append(item)
#Q.pop(0)
Q = []
visited = []
Q.append((0,0))
visited.append((0,0))

path_reached = False

while len(Q) != 0:

    #current location
    v = Q[0]
    row = v[0]
    column = v[1]

    #Identifying all neighbors of current location
    neighbors = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]

    #BFS
    for child in neighbors:
        if (child[0] < dim and child[0] >= 0) and (child[1] < dim and child[1] >= 0): #to make sure that indices within range are being enqueued
            if child not in visited and get_value(child[0], child[1]) == 0: #if child has not been visited already and is valid
                Q.append(child)
                visited.append(child)
                if child == (dim-1, dim-1): #if child is the goal state then break the loop and return "Goal Reached"
                    path_reached = True
                    print((child, "Goal Reached"))
                    Q = []
                    break

    #pop from the queue if it is not empty
    if len(Q) > 0:
        Q.pop(0)

#might need to add more to only print if a path has not been found
if path_reached == False:
    print("No path")
