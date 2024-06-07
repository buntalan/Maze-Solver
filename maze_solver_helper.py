# maze_solver.py
import maze_solver

def maze_printer(maze):
    # Prints maze
    for row in maze:
        for character in row:
            print(character, end='')
        print('\n', end='')

def maze_save(inputMaze):
    # Saves maze
    starting_location = []
    exit_location = []
    maze = []
    row = []
    wall_count = 0
    move_count = 0
    
    for index, character in enumerate(inputMaze):
        # Check if next character is a newline or end of string. If so, then
        # just continue. If character is a wall, then add one to wall_count
        if character != "\n" and index != len(inputMaze) - 1:
            row.append(character)
            if character == "o":
                starting_location = [len(maze), len(row) - 1]
            elif character == "x":
                exit_location = [len(maze), len(row) - 1]
            elif character == "*":
                wall_count += 1
        elif index == len(inputMaze) - 1:
            row.append(character)
            if character == "o":
                starting_location = [len(maze), len(row) - 1]
            elif character == "x":
                exit_location = [len(maze), len(row) - 1]
            elif character == "*":
                wall_count += 1
            maze.append(row)
        else:
            if len(row) == 0:
                continue
            maze.append(row)
            row = []
    return maze, starting_location, exit_location, move_count, wall_count