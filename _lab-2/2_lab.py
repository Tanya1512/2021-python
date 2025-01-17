maze = ('######## #',
        '#  #   # #',
        '## # ### #',
        '##   #   #',
        '#  ##  ###',
        '##     # #',
        '# ## ### #',
        '# ## # # #',
        '####     #',
        '####### ##', 
        '####### ##')

max_x, max_y = len(maze[0]), len(maze)

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')

def is_coord_in_maze(maze, coord):
    if coord[0]<0 or coord[0]>len(maze)-1:
        return False
    if coord[1]<0 or coord[1]>len(maze[0])-1:
        return False
    return True

def is_coord_exit(coord):
    if coord[0]>9:
        return True
    return False

def is_path_clean(maze, coord):
    if maze[coord[0]][coord[1]] == '#':
        return False
    return True

def step(coord, direction):
    if direction == 'N':
         return step_N(coord)
    elif direction == 'S':
         return step_S(coord)
    elif direction == 'E':
         return step_E(coord)
    elif direction == 'W':
         return step_W(coord)

def step_N(coord):
    return [coord[0]-1, coord[1]]

def step_E(coord):
    return [coord[0], coord[1]+1]

def step_S(coord):
    return [coord[0]+1, coord[1]]

def step_W(coord):
    return [coord[0], coord[1]-1]

def cut_way_back(maze, coord):
    new_maze = list(maze)
    # how to do thing like this:
    # to cancel the way back
    # 'cause strings in python are unmutable
    new_maze[coord[0]][coord[1]] = '#'
    return new_maze

def find_a_way(maze, coord):
    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if not is_coord_in_maze(maze, coord):
        print('not in bounds!')
        return

    if is_coord_exit(coord):
        print('new way is found')
        path_to_exit = current_path.copy()
        return

    if len(current_path) > len(path_to_exit):
        print('too large path')
        return

    for direction in POSSIBLE_WAYS:
        if is_path_clean(maze, step(coord, direction)):
               print(direction)
               current_path.append(direction)
               find_a_way(cut_way_back(maze, coord), step(coord, direction))
               current_path.pop()

    return 

path_to_exit = [' '*len(maze)*len(maze[0])]
current_path = []

start_point = [0, 8]
find_a_way(maze, start_point)
print(path_to_exit)
