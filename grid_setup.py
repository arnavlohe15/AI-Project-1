#creating a 2d grid in Python
import pygame
import numpy as np

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND = (79, 159, 159)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
dim = int(input("Enter the dimension of the game: "))
print(type(dim))
for row in range(dim):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(dim):
        grid[row].append(np.random.binomial(1, 0.3, 1))  # Append a cell

#print(grid)

pygame.init()

# Set the width and height of the screen [width, height]
size = (455, 455)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
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
            if grid[row][column] == 0:
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
