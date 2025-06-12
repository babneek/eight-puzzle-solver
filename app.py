import sys
import os
import streamlit as st

# ✅ Add root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from puzzle_solver.solver import a_star
from utils.helpers import print_puzzle, tuple_from_grid

st.set_page_config(page_title="8 Puzzle Solver", layout="centered")

st.title("🧠 8-Puzzle AI Solver")
st.write("Enter the initial and goal state of the 8-puzzle (use 0 for the blank tile).")

# Input forms for 3x3 puzzle grid
def input_grid(label):
    st.subheader(label)
    grid = []
    for i in range(3):
        cols = st.columns(3)
        row = []
        for j in range(3):
            cell = cols[j].number_input(f"{label} [{i},{j}]", min_value=0, max_value=8, step=1, key=f"{label}_{i}_{j}")
            row.append(cell)
        grid.append(row)
    return grid

initial_grid = input_grid("Initial State")
goal_grid = input_grid("Goal State")

if st.button("Solve Puzzle"):
    start = tuple_from_grid(initial_grid)
    goal = tuple_from_grid(goal_grid)

    if sorted(start) != list(range(9)) or sorted(goal) != list(range(9)):
        st.error("Each grid must contain all numbers from 0 to 8 exactly once.")
    else:
        with st.spinner("Solving..."):
            result = a_star(start, goal)
            if result:
                st.success(f"Solution found in {len(result) - 1} moves!")
                for i, (state, move) in enumerate(result):
                    st.text(f"Step {i}: Move {move}")
                    st.text(f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}")
            else:
                st.error("No solution found.")
