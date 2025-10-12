N, M = map(int, input().split())

treasure_grid = []
for _ in range(N):
    treasure_grid.append(input().split())
    
start_x, start_y = map(int, input().split())

pearl, platinum, gold, diamond = map(int, input().split())
treasure_value = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

K = int(input())
# print(N,M)
# print(treasure_grid)

def gravity_logic(row,col):
    total = 0
    #jabh tak # nhi aata ya last row na aajaye tabh tak girana h
    while row+1<N and treasure_grid[row+1][col]!='#':
        total += treasure_value.get(treasure_grid[row][col],0)
        row += 1
    #last cell ki bhi value khali nhi jani chaiye 
    total += treasure_value.get(treasure_grid[row][col],0)
    return row, col, total

def is_it_stable(row,col):
    if row == N - 1:
        return True
    if treasure_grid[row+1][col] == '#':
        return True
    return False 

max_treasure = 0

def total_collection(row, col, remaining_steps, collected_treasure):
    global max_treasure
    if remaining_steps < 0:
        return
    
    if is_it_stable(row,col) and row != N-1:
        max_treasure = max(max_treasure, collected_treasure)
        
    for delta_row, delta_col in [(0,-1),(0,1)]:
        next_row, next_col = row + delta_row, col + delta_col
        if 0 <= next_row < N and 0 <= next_col < M and treasure_grid[next_row][next_col] != '#':
            #har move ke baad gravity ko bhi dekhna padega 
            final_row, final_col, collected_value = gravity_logic(next_row, next_col)
            total_collection(final_row, final_col, remaining_steps - 1, collected_treasure + collected_value)
    

    above_row, above_col = row - 1, col
    if 0 <= above_row < N:
        if treasure_grid[above_row][above_col] != '#':
            total_collection(above_row, above_col, remaining_steps - 1, collected_treasure + treasure_value.get(treasure_grid[above_row][above_col],0))
        else:
            #kitna hi upar jaa skte h agr upar khali h toh
            climb_row = above_row - 1
            while climb_row >= 0 and treasure_grid[climb_row][above_col] == '#':
                climb_row -= 1
            if climb_row >= 0 and treasure_grid[climb_row][above_col] != '#':
                total_collection(climb_row, above_col, remaining_steps, collected_treasure + treasure_value.get(treasure_grid[climb_row][above_col],0))


final_start_row, final_start_col, start_val = gravity_logic(start_x, start_y)
total_collection(final_start_row, final_start_col, K, start_val)
print(max_treasure)
