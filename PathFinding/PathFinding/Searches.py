from Node import Node

#User Manhattan Method to find out how far Point a is from Point b
def h_AStar(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)