import heapq

class Node:
    def __init__(self, position):
        self.position = position
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal node)
        self.f = 0  # Total cost (g + h)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    # Calculate Manhattan distance as heuristic
    return abs(node.position[0] - goal.position[0]) + abs(node.position[1] - goal.position[1])

def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node)

        for neighbor_position in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x = current_node.position[0] + neighbor_position[0]
            neighbor_y = current_node.position[1] + neighbor_position[1]
            neighbor = Node((neighbor_x, neighbor_y))

            if neighbor.position[0] < 0 or neighbor.position[0] >= len(grid) or \
               neighbor.position[1] < 0 or neighbor.position[1] >= len(grid[0]) or \
               grid[neighbor.position[0]][neighbor.position[1]] == 1:
                continue

            if neighbor in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal_node)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node

            if neighbor not in open_list:
                heapq.heappush(open_list, neighbor)

    return None  # No path found

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")