import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        #self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_width = total_width

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        pass

    def is_open(self):
        pass

    def is_barrier(self):
        pass

    def is_start(self):
        pass

    def is_end(self):
        pass

    def reset(self):
        pass

    def make_start(self):
        pass

    def make_closed(self):
        pass

    def make_open(self):
        pass

    def make_barrier(self):
        pass

    def make_end(self):
        pass

    def make_path(self):
        pass

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows-1 and not grid[self.row+1][self.col].is_barrier(): #DOWN
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row-1][self.col])

        if self.row < self.total_rows-1 and not grid[self.row][self.col+1].is_barrier(): #RIGHT
            self.neighbors.append(grid[self.row][self.col+1])

        if self.row > 0 and not grid[self.row][self.self.col-1].is_barrier(): #LEFT
            self.neightbors.append(grid[self.row][self.col-1])

    def __lt__(self, other):
        return False