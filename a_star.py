#the popular path finding algortythm in python
#testing

import pygame
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (112,128,144)
RED = (255,0,0)
BLUE = (30,144,255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def a_star(maze,start_x, start_y,end_x, end_y):
    start = (start_x, start_y)
    end = (end_x, end_y)

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0


    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    while len(open_list) > 0:
    
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

    

grid = []
for row in range(28):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(51):
        grid[row].append(0)  # Append a cell

grid_clean = grid

border_grid = []
for row in range(28):
    # Add an empty array that will hold each cell
    # in this row
    border_grid.append([])
    for column in range(51):
        border_grid[row].append(0)  # Append a cell

path_grid = []
for row in range(28):
    # Add an empty array that will hold each cell
    # in this row
    path_grid.append([])
    for column in range(51):
        path_grid[row].append(0)  # Append a cell

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
                #border_grid.append([row,column])
                border_grid[row][column] = 1
                grid[row][column] = 3
                calculated = False
                path = a_star(border_grid,startpoint_x,startpoint_y, endpoint_x, endpoint_y)
                #print (path)
                for point in path:
                    grid[point[0]][point[1]]= 4
                calculated = True
                #print("Click ", pos, "Grid coordinates: ", row, column)
 
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
            if grid[row][column] == 4:
                color =BLUE
            
                # change color back from path color
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