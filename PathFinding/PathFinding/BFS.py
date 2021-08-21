import pygame
from queue import PriorityQueue
import math

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def BFS(draw, grid, start, end):
	#The Node that the Algorithm is currently on
	count = 0

	#Initialize the Set of Currently Open Nodes on the Graph
	open_set = PriorityQueue()

	#Push the Start Node to be the the first Open Node for the Algorithm
	open_set.put((0, count, start))

	#Initialize the set of nodes immediately preceeding the current node
	came_from = {}

	#Push the value of start into a map so it can latter be put into open_set
	open_set_hash = {start}

	findEnd = False

	current = None

	#Run Algorithm while open_set is not Empy
	while not findEnd:

		#Check to ensure user hasn't closed the Application
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		#Try to get the greatest value in the queue
		current = open_set.get()[2]
		open_set_hash.remove(current)

		#If Current happens to be end Node, reconstruct the path
		if current == end:
			end.make_end()
			findEnd = True

		#Find the Closest Neighbor Node to the End Node
		for neighbor in current.neighbors:

			if neighbor not in open_set_hash:
				count += 1
				open_set.put((0, count, neighbor))
				open_set_hash.add(neighbor)
				neighbor.make_open()

			if neighbor in open_set_hash:
				if current != start and current != end:
					current.make_closed()
				if current == start and current != end:
					current.make_start()
				if current != start and current == end:
					current.make_end()
				
		#Update display to Window
		draw()

	if findEnd:
		end.make_end()
		while current != start:
			for x in current.neighbors:
				if h(current.get_pos(), start.get_pos()) > h(x.get_pos(), start.get_pos()):
					current = x
			if current == start:
				break
			current.make_path()
