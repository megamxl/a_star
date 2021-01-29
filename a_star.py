#the popular path finding algortythm in python

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (112,128,144)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(28):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(51):
        grid[row].append(0)  # Append a cell
 
border_grid =[]

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1280,720]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("a Star visualisation")
 
# Loop until the user clicks the close button.
done = False

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

start_color = True
end_color = True

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if start_color == True:
                startpoint_x = row
                startpoint_y = column
                print("startpint ", startpoint_x, startpoint_y)
                grid[row][column] = 1
                start_color = False
            elif end_color == True:
                endpoint_x= row
                endpoint_y = column
                print("endpiont", endpoint_x, endpoint_y)
                grid[row][column] = 2
                end_color = False
            else:
                border_grid.append([row,column])
                grid[row][column] = 3
                print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    
    for row in range(28):
        for column in range(51):
            color = WHITE
            if grid[row][column] == 1:
                    color = GREEN
            if grid[row][column] == 2:
                    color = RED
            if grid[row][column] == 3:
                color = GREY
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
                              
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()