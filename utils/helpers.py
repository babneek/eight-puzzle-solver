def get_neighbors(state):
    """
    Returns all valid neighbor states by moving the blank tile (0) in the 8-puzzle.
    """
    neighbors = []
    index = state.index(0)
    row, col = divmod(index, 3)

    directions = {
        'Up': (-1, 0),
        'Down': (1, 0),
        'Left': (0, -1),
        'Right': (0, 1)
    }

    for move, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append((tuple(new_state), move))
    
    return neighbors


def print_puzzle(state):
    """
    Prints the 3x3 puzzle state in grid format.
    """
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()


def tuple_from_grid(grid):
    """
    Converts a 2D list (grid) into a flattened tuple.
    Example: [[1,2,3],[4,5,6],[7,8,0]] -> (1,2,3,4,5,6,7,8,0)
    """
    return tuple(cell for row in grid for cell in row)
