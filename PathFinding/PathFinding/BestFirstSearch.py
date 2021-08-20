import pygame
from ConstructPath import *
import math
from queue import PriorityQueue

#Calculate the Heuristic that is needed for the BestFirstSearch Algorithm
def h_BestFirst(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def BestFirstSearch(draw, grid, start, end):

    #The Node that the Algorithm is currently on
	count = 0

	#Initialize the Set of Currently Open Nodes on the Graph
	open_set = PriorityQueue()

	#Push the Start Node to be the the first Open Node for the Algorithm
	open_set.put((0, count, start))

	#Initialize the set of nodes immediately preceeding the current node
	came_from = {}

	#Calculate the Cost from the Start Node to the Current Node
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0

	#Calculate the Cost from the Current Node to the End Node
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h_BestFirst(start.get_pos(), end.get_pos())

	#Push the value of start into a map so it can latter be put into open_set
	open_set_hash = {start}

	#Run Algorithm while open_set is not Empy
	while not open_set.empty():

		#Check to ensure user hasn't closed the Application
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		break
