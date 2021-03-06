import pygame
from queue import PriorityQueue
import math

#Heuristic used to locate start from end
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def BFS(draw, grid, start, end):

	#Set Caption to Display which Algorithm is being used
	pygame.display.set_caption("Breadth First Search Path Finding Algorithm (Press 1 for A* and 2 for Best First Search)")

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

	#Determines if a path has been found
	findEnd = False

	#The current node that is being analyzed
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

			#If neighbor is not in open_set_hash make it open
			if neighbor not in open_set_hash:
				count += 1
				open_set.put((0, count, neighbor))
				open_set_hash.add(neighbor)
				neighbor.make_open()

			#If neighbor is in open_set_hash
			if neighbor in open_set_hash:
				#If neighbor is neither start nor end, make it closed
				if current != start and current != end:
					current.make_closed()
				#If neighbor is start, but not end, then make it start
				if current == start and current != end:
					current.make_start()
				#If neighbor is not start, but end, then make it end
				if current != start and current == end:
					current.make_end()
				
		#Update display to Window
		draw()

	#If end is found
	if findEnd:
		#make end end
		end.make_end()
		#While current is not back to start yet, backtrace path
		while current != start:
			#Calculate which Neighbor is closest to start
			for neighbor in current.neighbors:
				#Update Current to neightbor if it has shorter heuristic
				if h(current.get_pos(), start.get_pos()) > h(neighbor.get_pos(), start.get_pos()):
					current = neighbor
			#Make current a path node
			if current != start:
				current.make_path()
			#If current is start, break loop
			if current == start:
				break
