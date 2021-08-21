import pygame
from ConstructPath import *
from queue import PriorityQueue
import math

def h_BestFirst(p1, p2):
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

	#Run Algorithm while open_set is not Empy
	while not open_set.empty():

		#Check to ensure user hasn't closed the Application
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		#Try to get the greatest value in the queue
		current = open_set.get()[2]
		open_set_hash.remove(current)

		#If Current happens to be end Node, reconstruct the path
		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		#TODO: Get furtheset Left Node in Neighbors
		for neighbor in current.neighbors:
			came_from[neighbor] = current
			if neighbor not in open_set_hash:
				open_set.put((0, count, neighbor))
				open_set_hash.add(neighbor)
				neighbor.make_open()
				

		#Update display to Window
		draw()

		#If current is not Start, make the Node a Closed Node
		if current != start:
			current.make_closed()

	return False