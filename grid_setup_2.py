# Creating a grid visualization based off a 2D numpy array to be used for graph search algorithms
import pygame
import numpy as np

# Creating a node class to represent individual entries in the game Grid
class node:

    def __init__(self, value, visited):
        self.value = value
        self.visited = visited

#x = node(0, True)
#if x.visited:
    #print("yes this works")


# Defining RGB Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND = (79, 159, 159)
RED = (255, 0, 0)

# Declaring dimensions for each box in the grid
WIDTH = 40
HEIGHT = 40

# Declaring the margin size between each cell
MARGIN = 5

# Creating a two-dimensional array to represent our grid
grid = []
dim = int(input("Enter the dimension of the game: "))
print(type(dim))
for row in range(dim):
    grid.append([])
    for column in range(dim):
        #grid[row].append(np.random.binomial(1, 0.3, 1))
        grid[row].append(node((int(np.random.binomial(1, 0.3, 1)[0])), False))
        #inserting binomial random variable
grid[0][0] = node(0, False)

#print(grid)
# Initializing pygame object
pygame.init()

# Setting the width and height of the screen [width, height]
size = ((MARGIN + WIDTH) * dim + MARGIN, (MARGIN + WIDTH) * dim + MARGIN)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Looping until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
            if grid[row][column].value == 0:
                color = WHITE
            else:
                color = BLACK
            if row == 0 and column == 0:
                color = WHITE
            #color = WHITE
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
pygame.quit()
