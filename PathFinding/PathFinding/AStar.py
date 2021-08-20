import pygame
from queue import PriorityQueue

#Calculate the Heuristic that is needed for the ASTAR Algorithm
def h_ASTAR(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

#Reconstruct the Needed Path
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

#ASTAR Algorithm
def AStar(draw, grid, start, end):

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
	f_score[start] = h_ASTAR(start.get_pos(), end.get_pos())

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

		#Find the Closest Neighbor Node to the End Node
		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			#If temp_g_score is cheaper than current g_score, then
			#update the g_score and f_score
			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h_ASTAR(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		#Update display to Window
		draw()

		#If current is not Start, make the Node a Closed Node
		if current != start:
			current.make_closed()

	return False
