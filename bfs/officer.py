import queue

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == 'O':
            start = x
    i = start
    j = 0
    for move in moves:
        if move == 'L':
            i -= 1
        elif move == 'R':
            i += 1
        elif move == 'D':
            j += 1
        elif move == 'U':
            j -= 1
        if not(0 <= i < len(maze[0]) and 0<= j < len(maze)):
            return False
        elif maze[j][i] == 'X':
            return False
    return True
            


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == 'O':
            start = x
    i = start
    j = 0
    for move in moves:
        if move == 'L':
            i -= 1
        elif move == 'R':
            i += 1
        elif move == 'D':
            j += 1
        elif move == 'U':
            j -= 1
    if maze[j][i] == 'T':
        print('Found: ' + moves)
        print(len(moves))
        return True
    
    return False

def leastSpaces(maze):
    paths = queue.Queue()
    paths.put('')
    add = ''
    while not findEnd(maze,add):
        add = paths.get()
        for move in ['L', 'R', 'U', 'D']:
            poten = add + move
            if valid(maze, poten):
                paths.put(poten)

    return len(add)
maze  = [['_', 'O','_'],
        ['_', 'X', 'X'],
        ['_','_','T']
]
leastSpaces(maze)




