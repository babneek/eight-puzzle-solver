def manhattan_distance(state, goal):
    """
    Calculates the Manhattan distance between the current state and the goal state.
    """
    distance = 0
    for i, value in enumerate(state):
        if value == 0:
            continue  # Skip the blank tile
        goal_index = goal.index(value)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
