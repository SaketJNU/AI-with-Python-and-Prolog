from collections import deque

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start, [start])])  # (position, path)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path  # Found the goal

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found


# 0 = path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 4)
print("Path from start to goal in maze:")
print(bfs_maze(maze, start, goal))
