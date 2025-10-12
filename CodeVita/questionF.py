# Input reading
N, M = map(int, input().split())

treasure_grid = []
for _ in range(N):
    treasure_grid.append(input().split())
    
start_x, start_y = map(int, input().split())

pearl, platinum, gold, diamond = map(int, input().split())
treasure_value = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

K = int(input())

max_treasure = 0

# Apply gravity and return all collected cells
def gravity_collect(row, col, visited):
    collected = 0
    cells = []
    while row + 1 < N and treasure_grid[row + 1][col] != '#':
        if not visited[row][col]:
            collected += treasure_value.get(treasure_grid[row][col], 0)
            cells.append((row, col))
        row += 1
    if not visited[row][col]:
        collected += treasure_value.get(treasure_grid[row][col], 0)
        cells.append((row, col))
    return row, col, collected, cells

# Check if cell is stable
def is_stable(row, col):
    return row == N - 1 or treasure_grid[row + 1][col] == '#'

# DFS with visited tracking
def dfs(row, col, steps_left, collected_treasure, visited):
    global max_treasure
    if steps_left < 0:
        return

    # Apply gravity
    row, col, val, cells = gravity_collect(row, col, visited)
    collected_treasure += val

    # Mark collected cells as visited
    for r, c in cells:
        visited[r][c] = True

    # Update max treasure if stable
    if is_stable(row, col):
        max_treasure = max(max_treasure, collected_treasure)

    # Move left and right
    for dr, dc in [(0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < N and 0 <= nc < M and treasure_grid[nr][nc] != '#':
            dfs(nr, nc, steps_left - 1, collected_treasure, visited)

    # Move up
    nr, nc = row - 1, col
    while nr >= 0 and treasure_grid[nr][nc] == '#':
        nr -= 1
    if nr >= 0:
        dfs(nr, nc, steps_left - 1, collected_treasure, visited)

    # Backtrack visited cells
    for r, c in cells:
        visited[r][c] = False

# Initialize visited matrix
visited = [[False] * M for _ in range(N)]
dfs(start_x, start_y, K, 0, visited)

print(max_treasure)
