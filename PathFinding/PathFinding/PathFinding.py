import pygame, math
import Color as color
from Node import Node
from queue import PriorityQueue

#Set up Window for Simulation
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding")

#Create a Grid for the Simulation
def create_Grid(rows, width):
    #Create a List to aid in illustrating functionality for AI
    grid = []

    #Calculate the gap in the grid
    gap = width // rows

    #Add nodes in the grid
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

#Draw the grid lines so the simulation can be seen better
def draw_gridlines(win, rows, width):

    #Calculate the gap in the grid
    gap = width // rows

    #Draw Lines Vertically and Horizontally on the Window
    for i in range(rows):
        pygame.draw.line(win, color.DARK_GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, color.DARK_GREY, (j*gap, 0), (j*gap, width))

#Draw Everything that is needed for the Screen
def draw(win, grid, rows, width):
    #Fill the Entire Window White so that recent changes can be implemented
    win.fill(color.WHITE)

    #Draw each node in the Grid
    for row in grid:
        for node in row:
            node.draw(win)

    #Create the Grid
    draw_gridlines(win, rows, width)

    #Update the Window of the Program
    pygame.display.update()

#Get the Node Position that is clicked on
def get_ClickedPos(pos, rows, width):
    #Calculate the gap in the grid
    gap = width // rows

    #Get the X and Y components of Position
    y, x = pos
    
    #Calculate row and col that are on the grid
    row = y // gap
    col = x // gap

    #Return the row and col that have been selected
    return row, col


#Will be the Driving Function for the Program
def main(win, width):
    #The Number of Rows that will Exist in Simulation
    ROWS = 50

    #The Grid that everything events will take place on 
    grid = create_Grid(ROWS, width)

    #The start and end points that pathfind will be attempting to make a path between
    start = None
    end = None

    #Will handle if a given simulation has started or not
    started = False

    #Lets Program run
    run = True

    #The Loop that will help run the Simulation
    while run:
        for event in pygame.event.get():

            draw(WIN, grid, ROWS, width) 

            #If Giant "X" Button in Top-Right Corner has already been pressed
            if event.type == pygame.QUIT:
                run = False

            #Don't allow any Inputs if a Simulation has already Started
            if started:
                continue

            #If the Left Mouse button has been pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_ClickedPos(pos, ROWS, width)
                node = grid[row][col]

                #If Start has not been defined yet
                if not start:
                    start = node 
                    start.setStart()

                #If End has not been defined yet
                elif not end:
                    end = node
                    end.setEnd()

                #If Start and End have already been defined
                elif node != end and node != start:
                    node.setBarrier()

            #If the Right Mouse button has been pressed
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_ClickedPos(pos, ROWS, width)
                node = grid[row][col]

                if node == start:
                    start = None
                elif node == end:
                    end = None

    pygame.quit()


main(WIN, WIDTH)