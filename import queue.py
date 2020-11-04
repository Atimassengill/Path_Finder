import queue


def MakeMaze1():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "X", "#", "#", "","#"])

    return maze

def MakeMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "X", "#", "#", "#", "#", "#"])

    return maze

def Show_Maze(maze, path=''):
    for x, pos in enumerate(maze[0]):
        if pos == o:
            start = x
        S = start
    R = 0
    pos = set()
    for move in path:
        if move == "L":
            S -= 1

        elif move == "R":
            S += 1

        elif move == "U":
            R -= 1

        elif move == "D":
            R += 1
        pos.add((R, S))
    
    for R, row in enumerate(maze):
        for S, col in enumerate(row):
            if (R, S) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    S = start
    R = 0
    for move in moves:
        if move == "L":
            S -= 1

        elif move == "R":
            S += 1

        elif move == "U":
            R -= 1

        elif move == "D":
            R += 1

        if not(0 <= S < len(maze[0]) and 0 <= R < len(maze)):
            return False
        elif (maze[R][S] == "#"):
            return False

    return True


def Find_the_End(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    S = start
    R = 0
    for move in moves:
        if move == "L":
            S -= 1

        elif move == "R":
            S += 1

        elif move == "U":
            R -= 1

        elif move == "D":
            R += 1

    if maze[R][S] == "X":
        print("Found: " + moves)
        print(maze, moves)
        return True

    return False

import queue
nums = queue.Queue()
nums.put('')
add = ''
maze = MakeMaze2()
while not Find_the_End(maze, add): 
    add = nums.get()
    
    for R in ["L", "R", "U", "D"]:
        put = add + R
        if valid(maze, put):
            nums.put(put)
