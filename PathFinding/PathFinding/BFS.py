import pygame
from ConstructPath import *
from queue import PriorityQueue

def BFS(draw, grid, start, end):

	#Queue of Nodes that have not been visited 
	queue = PriorityQueue()

	#Queue of Nodes that have been visitied
	visited = PriorityQueue()

	#Insert the start Node in queue
	queue.put(start)

	#Run Algorithm while queue is not Empty
	while not queue.empty():

		#Check to ensure user hasn't closed the Application
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		#pop queue and store Node in current
		current = queue.get()

		#If Current happens to be end Node, reconstruct the path
		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		#Insert Current to visited
		visited.put(current)

		#Get all neighbors to current
		neighbors = current.update_neighbors(grid)

		#TODO: Insert neighbors into queue 

		#If current is not start, set is as closed
		if current != start:
			current.make_closed()

	return False