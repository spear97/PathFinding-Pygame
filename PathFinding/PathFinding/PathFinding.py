import pygame, math
import Color as color
from Node import Node
from queue import PriorityQueue

#Set up Window for Simulation
WIDTH = 800
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding")

#Create a Grid for the Simulation
def create_Grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return

#Draw the grid lines so the simulation can be seen better
def draw_gridlines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, color.DARK_GREY, (0, i*gap), (widht, i*gap))
        for j in range(rows):
            pygame.draw.line(win, color.DARK_GREY, (j*gap, 0), (j*gap, width))

#Draw Everything that is needed for the Screen
def draw(win, grid, rows, width):
    win.fill(color.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    create_Grid(win, rows, width)
    pygame.display.update()

#Get the Node that is clicked on
def get_ClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = i // gap
    col = x // gap
    return row, col
