import pygame

#Colors for Node Class
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (68, 85, 90)
LIGHT_GREEN = (144, 238, 144)

#Node Class for Nodes on the Graph
class Node:
    #Constructor
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    #Get the Position of the Node
    def get_pos(self):
        return (self.row, self.col)

    #Check if Node is Open
    def is_opened(self):
        return self.color == LIGHT_BLUE

    #Check if Node is Closed 
    def is_closed(self):
        return self.color == BLUE

    #Check if Node is Start
    def is_start(self):
        return self.color == GREEN

    #Check if Node is End
    def is_end(self):
        return self.color == RED

    #Check if Node is Blocked
    def is_blocked(self):
        return self.color == GREY

    #Set Node back to Default
    def reset(self):
        self.color = WHITE

    #Set Node to be Open
    def make_open(self):
        self.color = LIGHT_BLUE

    #Set Node to be Closed
    def make_closed(self):
        self.color = BLUE

    #Set Node to be Start
    def make_start(self):
        self.color = GREEN

    #Set Node to be End
    def make_end(self):
        self.color = RED

    #Set Node to be Blocked
    def make_blocked(self):
        self.color = GREY

    #Set Node to be Path
    def make_path(self):
        self.color = LIGHT_GREEN

    #Draw Node on Window
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    #Collect the Neighbors that are near the current Node
    def update_neighbors(self, grid):
        self.neighbors = []
        #DOWN
        if self.row < self.total_rows-1 and not grid[self.row+1][self.col].is_blocked():
            self.neighbors.append(grid[self.row+1][self.col])
        #UP
        if self.row > 0 and not grid[self.row-1][self.col].is_blocked():
            self.neighbors.append(grid[self.row-1][self.col])
        #RIGHT
        if self.col < self.total_rows-1 and not grid[self.row][self.col+1].is_blocked():
            self.neighbors.append(grid[self.row][self.col+1])
        #LEFT
        if self.col > 0 and not grid[self.row][self.col-1].is_blocked():
            self.neighbors.append(grid[self.row][self.col-1])