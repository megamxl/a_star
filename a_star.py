#the popular path finding algortythm in python

import pygame
import math
 
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
def is_bloked(border_grid, current_point,):
    x = current_point[0]
    y = current_point[1]
    f= 0
    for i in border_grid:
        if x == border_grid[f][0] and y == border_grid[f][1]:
            f +=1
            return True
        else:
            f +=1
            if f == len(border_grid):
                return False            


def is_valid(currentpoint):
    if currentpoint[0] > 27 or currentpoint[0] < 0:
        return False
    elif currentpoint[1]> 51 or currentpoint[1] < 0:
        return False
    else:
        return True

def is_endpoint(currentpoint):
    if currentpoint[0] == endpoint_x and currentpoint[1] == endpoint_y:
        return True
    else:
        return False

def calculateHvalue(currentpoint,dest_x, dest_y):
    return math.sqrt(((currentpoint[0]-dest_x)*(currentpoint[0]-dest_x))+(currentpoint[1]-dest_y)+(currentpoint[1]-y))

def aStarbegin(border_grid,start_x,start_y,end_x,end_y,currentpoint):
    start_arry=[start_x,start_y]
    end_array=[end_x,end_y]       
    if is_bloked(border_grid,start_arry) or is_bloked(border_grid,end_array):
        print("point is blocked")
        return 
    arr = [[0 for i in range(cols)] for j in range(rows)]   
    
grid = []
for row in range(28):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(51):
        grid[row].append(0)  # Append a cell

grid_clean = grid

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
                aStarbegin(border_grid,startpoint_x,startpoint_y,endpoint_x,endpoint_y)
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