#creating a 2d grid in Python

import numpy as np
from agent import Agent
import pygame

# SETUP GRID
# Defining some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND = (79, 159, 159)
RED = (255, 0, 0)
PINK = (243,202,244)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
# This sets the margin between each cell
MARGIN = 5

# Getting dimension input
dim = int(input('Enter dimension: '))
index_max = dim - 1

# Setting the width and height of the screen [width, height]
size = ((MARGIN + WIDTH) * dim + MARGIN, (MARGIN + WIDTH) * dim + MARGIN)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []


    # Looping until the user clicks the close button.
    done = False

    for row in range(dim):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(dim):
            grid[row].append(np.random.binomial(1, 0.2, 1))  # Append a cell
            if (row == column == dim - 1):
                grid[row][column] = 0
        grid[0][0] = 0

    pygame.display.set_caption("Empty Maze")
    pygame.init()

    # Initializing agent and obtaining paths
    agent = Agent(grid)
    dfs_path = agent.dfs()
    bfs_path = agent.bfs()
    #euclid_path = agent.a_star_euclidean())
    #manhattan_path = agent.a_star_manhattan())


    # -------- Obtaining Blank Maze -----------
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)

    # -------- Displaying DFS Path -----------
    pygame.display.set_caption("DFS")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    if (row, column) in dfs_path:
                        color = PINK
                    else:
                        color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)

    # -------- Displaying BFS Path -----------
    pygame.display.set_caption("BFS")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    if (row, column) in bfs_path:
                        color = PINK
                    else:
                        color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)
    quit()

    """# -------- Displaying A* Euclidean Path -----------
    pygame.display.set_caption("A* Euclidean")
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    if (row, column) in euclid_path:
                        color = PINK
                    else:
                        color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)
    quit()

    # -------- Displaying A* Manhattan Path -----------
    pygame.display.set_caption("A* Manhattan")
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    if (row, column) in manhattan_path:
                        color = PINK
                    else:
                        color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)
    quit()

    # -------- Displaying Bidirectional BFS Path -----------
    pygame.display.set_caption("Bidirectional BFS")
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND)
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
        clock.tick(60)
    quit()"""

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
