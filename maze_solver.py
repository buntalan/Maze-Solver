"""
This module solves mazes by following wall to the right through the whole
maze. 
"""

import time
import string
from maze_solver_helper import *

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
STARTING_DIRECTION = SOUTH

def main():
    """
    This class runs our maze_solver program. 
    """
    input_maze = "*****\n*o*x*\n*   *\n*****"
    input_maze_long = ("*****\n" +
                       "*o*x*\n" +
                       "*   *\n" +
                       "*****")

    # Save maze to memory
    maze, starting_location, exit_location, \
    move_count, wall_count = maze_save(input_maze_long)

    print(maze)
    print(starting_location)
    print(exit_location)

    player_position = starting_location[:]
    player_direction = STARTING_DIRECTION
    exit_found = False
    character_holder = store_token(maze, player_position)
    place_token(maze, player_position, "C")

    while not exit_found and move_count <= wall_count:
        maze_printer(maze)
        print("\n")
        print(player_position)
        print(player_direction)
        time.sleep(0.5)
        if check((player_direction + 1) % 4,
                 player_position,
                 maze):
            place_token(maze, player_position, character_holder)
            player_direction = (player_direction + 1) % 4
            move(player_direction, player_position)
            character_holder = store_token(maze, player_position)
            place_token(maze, player_position, "C")
        elif check(player_direction,
                 player_position,
                 maze):
            place_token(maze, player_position, character_holder)
            move(player_direction, player_position)
            character_holder = store_token(maze, player_position)
            place_token(maze, player_position, "C")
        elif check((player_direction - 1) % 4,
                   player_position,
                   maze):
            place_token(maze, player_position, character_holder)
            player_direction = (player_direction - 1) % 4
            move(player_direction, player_position)
            character_holder = store_token(maze, player_position)
            place_token(maze, player_position, "C")
        else:
            place_token(maze, player_position, character_holder)
            player_direction = (player_direction - 2) % 4
            move(player_direction, player_position)
            character_holder = store_token(maze, player_position)
            place_token(maze, player_position, "C")
        move_count += 1
        if player_position == exit_location:
            exit_found = True

    maze_printer(maze)

    if exit_found:
        print("Exit found!")
    if move_count > wall_count:
        print("No exit was found.")


def move(direction, position):
    # Moves in direction passed
    match direction:
        # NORTH
        case 0:
            position[0] = position[0] - 1
        # EAST
        case 1:
            position[1] = position[1] + 1
        # SOUTH
        case 2:
            position[0] = position[0] + 1
        # WEST
        case 3:
            position[1] = position[1] - 1

def check(direction, position, maze) -> bool:
    # Check if move is possible
    match direction:
        case 0:
            if maze[position[0] - 1][position[1]] != "*":
                return True
            else:
                return False
        # EAST
        case 1:
            if maze[position[0]][position[1] + 1] != "*":
                return True
            else:
                return False
        # SOUTH
        case 2:
            if maze[position[0] + 1][position[1]] != "*":
                return True
            else:
                return False
        # WEST
        case 3:
            if maze[position[0]][position[1] - 1] != "*":
                return True
            else:
                return False

def store_token(maze, place):
    temp = maze[place[0]][place[1]]
    return temp

def place_token(maze, place, token):
    maze[place[0]][place[1]] = token

if __name__ == '__main__':
    main()
