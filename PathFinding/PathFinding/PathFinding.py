import pygame
import Node
import Search as s
import Color as c

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption ("PathFinding Algorithm")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(widn, rows, width):
    gap = width //rows 
    for i in range(rows):
        pygame.draw.line(win, c.GREY, (0, i*gap), (width, i*gap))

def draw(win, grid, rows, width):
    win.fill(c.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.diplay.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x, = pos

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: #LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clikced_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygameK_SPACE and start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbor(grid)

                        s.A_Star(lambda: draw(win, grid, Rows, width), grid, start, end)

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)