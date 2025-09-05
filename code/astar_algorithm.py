import pygame
import time
from queue import PriorityQueue
from constants import ALGORITHM_DELAY

def manhattan_distance(p1, p2):
    """Calculate Manhattan distance for two points"""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    """Visualize the final path from start to end"""
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def astar_algorithm(draw, grid, start, end):
    """
    A* pathfinding algorithm implementation
    
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # Initialize g_score and f_score for all nodes
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = manhattan_distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        # Handle pygame events to prevent window freezing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        # Path found
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        # Explore neighbors
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + manhattan_distance(neighbour.get_pos(), end.get_pos())

                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()
        time.sleep(ALGORITHM_DELAY)

        if current != start:
            current.make_closed()

    return False