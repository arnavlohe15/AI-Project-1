#creating a 2d grid in Python
"""import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.random.random((10,10)));
plt.colorbar()
plt.show()"""

import numpy as np
from agent import Agent
import pygame

# SETUP GRID
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND = (79, 159, 159)
RED = (255, 0, 0)
MAROON = (176, 48, 96)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
# This sets the margin between each cell
MARGIN = 5

# Get dimension input
dim = int(input('Enter dimension: '))

# Set the width and height of the screen [width, height]
size = ((MARGIN + WIDTH) * dim + MARGIN, (MARGIN + WIDTH) * dim + MARGIN)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []

    pygame.display.set_caption("Maze Runner")

    # Loop until the user clicks the close button.
    done = False

    for row in range(dim):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(dim):
            grid[row].append(np.random.binomial(1, 0.2, 1))  # Append a cell
        grid[0][0] = 0

    pygame.init()

    # Initialize agent
    agent = Agent(grid)
    print("DFS")
    agent.dfs()
    print("BFS")
    agent.bfs()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BACKGROUND)

        # --- Drawing code should go here
        # Draw the grid
        for row in range(dim):
            for column in range(dim):
                if grid[row][column] == 0:
                    color = WHITE
                else:
                    color = BLACK
                #if row == 0 and column == 0:
                    #color = WHITE
                # color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    quit()

def show_dfs(agent, grid):
    # look at agent's closed states
        # color the squares in closed states maroon
    print('entered show_dfs')

    for pos in agent.closed:
        if row is pos()[0] and col is pos()[1]:
            color = MAROON
        pygame.draw.rect(screen,
                        color,
                        [(MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT])
    pygame.display.flip()

def show_bfs(agent, grid):
    return
def show_a_star_euclidean(agent, grid):
    return
def show_a_star_manhattan(agent, grid):
    return
def show_bidirectional_bfs(agent, grid):
    return


if __name__ == '__main__':
    main()
