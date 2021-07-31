import Color as color
import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        #The Row the Node Belongs to 
        self.row = row

        #The Column that the Node Belongs to 
        self.col = col

        #The X Location that the Node is placed at
        self.x = row * width

        #The Y Location that the Node is placed at
        self.y = col * width

        #The color that the Node is white on default
        self.color = color.WHITE

        #All Surrounding Nodes that surround itself
        self.neighbors = []

        #The Overall Size that the Node will be
        self.width = width

        #The total Number of Rows
        self.total_rows = total_rows

        #The Color the Node will be on the grid by default
        self.default_color = color.WHITE

        #The color the node will be when it is set as closed
        self.closed_color = color.BLUE

        #The color the node will be when the node is open
        self.open_color = color.TURQUOISE

        #The color the node will be when it is Stating Node
        self.start_color = color.GREEN

        #The color the node will be when it is the Ending Node
        self.end_color = color.RED

        #The color the node will be when it is an Obstacle to not be explored
        self.block_color = color.BLACK

        #The color the node will be when it part of the path
        self.path_color = color.ORANGE

    #The Position that the Node is currently at
    def getPosition(self):
        return self.row, self.col

    #Check if the Node is closed or not 
    def closed(self):
        return self.color == self.closed_color

    #Check if the Node is open or not
    def open(self):
        return self.color == self.open_color

    #Check if the Node is blocked or not
    def blocked(self):
        return self.color == self.block_color

    #Check if the Node is the start Node or not
    def start(self):
        return self.color == self.start_color

    #Check if the Node is the End Node or not
    def end(self):
        return self.color == self.end_color

    #Set the Node back to the Default Color
    def reset(self):
        self.color = self.default_color

    #Set the Node as a Closed Node
    def setClosed(self):
        self.color = self.closed_color

    #Set the Node as an Opened Node
    def setOpen(self):
        self.color = self.open_color

    #Set the Node as an Obstacel Node
    def setBarrier(self):
        self.color = self.block_color

    #Set the Node as a Start Node
    def setStart(self):
        self.color = self.start_color

    #Set the Node as an End Node
    def setEnd(self):
        self.color = self.end_color

    #Set the Node as a Path Node
    def setPath(self):
        self.color = self.path_color

    #Draw the Node
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    #Update all Neighbor nodes surrounding it
    def update_neighbors(self, grid):
        return

    def __lt__(self, other):
        return False
