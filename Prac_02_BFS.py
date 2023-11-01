from collections import deque

# Representing the 8-puzzle problem
class PuzzleState:
    def __init__(self, puzzle, moves=0):
        self.puzzle = puzzle
        self.blank_tile = puzzle.index(0) # index of blank tile
        self.moves = moves

    def get_possible_moves(self):
        possible_moves = []
        for offset in [-3, -1, 1, 3]:
            new_pos = self.blank_tile + offset
            if 0 <= new_pos < 9:
                if offset == -3 and self.blank_tile not in [0, 1, 2]:
                    possible_moves.append(new_pos)
                elif offset == -1 and self.blank_tile not in [0, 3, 6]:
                    possible_moves.append(new_pos)
                elif offset == 1 and self.blank_tile not in [2, 5, 8]:
                    possible_moves.append(new_pos)
                elif offset == 3 and self.blank_tile not in [6, 7, 8]:
                    possible_moves.append(new_pos)
        return possible_moves

    def generate_new_state(self, move):
        new_puzzle = self.puzzle[:]
        new_puzzle[self.blank_tile], new_puzzle[move] = new_puzzle[move], new_puzzle[self.blank_tile]
        return PuzzleState(new_puzzle, self.moves + 1)

# Breadth-First Search algorithm
def bfs(initial_state, goal_state):
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_state = queue.popleft()
        if current_state.puzzle == goal_state:
            return current_state.moves
        visited.add(tuple(current_state.puzzle))

        possible_moves = current_state.get_possible_moves()
        for move in possible_moves:
            new_state = current_state.generate_new_state(move)
            if tuple(new_state.puzzle) not in visited:
                queue.append(new_state)

# Example usage
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8] # initial state of the puzzle
goal_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]    # goal state of the puzzle

initial_state_obj = PuzzleState(initial_state)
moves = bfs(initial_state_obj, goal_state)
print("Number of moves required to reach the goal state:", moves)