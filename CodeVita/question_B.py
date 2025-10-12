num_commands = int(input().strip())
    
commands = []
    
for _ in range(num_commands):
    existing_cube,new_cube,direction = input().split()
    
    commands.append((int(existing_cube),int(new_cube),direction))
    
target_cube = int(input())
    
for i in range(len(commands)):
    for j in range(i+1,len(commands)):
        if commands[i][0] > commands[j][0] or (commands[i][0] == commands[j][0] and commands[i][1] > commands[j][1]):
            commands[i], commands[j] = commands[j], commands[i]
                            
direction_mapping = {
    'top': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

position_cube = {}

for existing_cube,new_cube,direction in commands:
    if existing_cube not in position_cube:
        position_cube[existing_cube] = (0,0)
        
    existing_cube_row,existing_cube_col = position_cube[existing_cube]
    
    move_row,move_col = direction_mapping[direction]
    
    new_cube_row = existing_cube_row + move_row
    new_cube_col = existing_cube_col + move_col
    
    position_cube[new_cube] = (new_cube_row,new_cube_col)
    
target_row , target_col = position_cube[target_cube]
adjacent_cubes = []

order_check = ['top', 'down', 'left', 'right']

for key in order_check:
    move_row,move_col = direction_mapping[key]
    adjacent_row = target_row + move_row
    adjacent_col = target_col + move_col
    
    default = -1
    
    for cube_num, (row,col) in position_cube.items():
        if row == adjacent_row and col == adjacent_col:
            default = cube_num
            break
        
    adjacent_cubes.append(default)
    


for num in adjacent_cubes:
    print(num , end=" ")
print()


