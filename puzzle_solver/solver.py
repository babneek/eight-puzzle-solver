import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import heapq
from puzzle_solver.heuristics import manhattan_distance
from utils.helpers import get_neighbors

def a_star(start, goal):
    """
    A* search algorithm for solving the 8-puzzle problem.
    
    :param start: Tuple representing the initial state
    :param goal: Tuple representing the goal state
    :return: List of (state, move) tuples representing the path from start to goal
    """
    open_set = []
    heapq.heappush(open_set, (0 + manhattan_distance(start, goal), 0, start, []))
    
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [(current, "Goal")]

        for neighbor, move in get_neighbors(current):
            if neighbor not in visited:
                new_path = path + [(current, move)]
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (g + 1 + h, g + 1, neighbor, new_path))

    return None  # No solution found
