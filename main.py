from modules.maze import Maze

import os


def main():

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, "maze.txt")
    maze1 = Maze("maze.txt")
    maze1.display()

    while not maze1.is_exit(maze1.locations['P']):
        # ask for input
        print("\nPlease Press W or A or S or D:")
        user_input = input()
        player_location = maze1.locations['P']

        # case W
        if user_input.lower() == "w":

            # step_value: 0(false) if player is at the boundary
            # or the moving place is a wall. otherwise 1(true)
            step_value = (player_location[0] != 0) and (
                maze1.can_move_to(player_location[0]-1, player_location[1]))

            maze1.locations["P"] = (
                player_location[0]-step_value, player_location[1])  # move up

        # case A
        elif user_input.lower() == "a":
            step_value = (player_location[1] != 0) and (
                maze1.can_move_to(player_location[0], player_location[1]-1))

            maze1.locations["P"] = (
                player_location[0], player_location[1]-step_value)  # left

        # case S
        elif user_input.lower() == "s":
            step_value = (player_location[0] != maze1.maze_height-1) and (
                maze1.can_move_to(player_location[0]+1, player_location[1]))

            maze1.locations["P"] = (
                player_location[0]+step_value, player_location[1])  # down

        # case D
        elif user_input.lower() == "d":
            step_value = (player_location[1] != maze1.maze_width-1) and (
                maze1.can_move_to(player_location[0], player_location[1]+1))

            maze1.locations["P"] = (
                player_location[0], player_location[1]+step_value)  # right

        else:
            print("\ninvalid command. Please Enter a valid command.")

        # move the player according to the command
        if player_location != maze1.locations['P']:  # the move happened
            # make the original location a whitespace

            maze1.maze_lines[player_location[0]
                             ] = maze1.maze_lines[player_location[0]].replace("P", " ")

            # replace the new location with P
            new_line = ''
            count = 0
            for char in maze1.maze_lines[maze1.locations['P'][0]]:
                if count == maze1.locations['P'][1]:
                    char = "P"
                new_line += char
                count += 1

            maze1.maze_lines[maze1.locations['P'][0]] = new_line

            # When getting a Treasure
            if maze1.locations["P"] == maze1.locations["T"]:
                maze1.get_item()

        print()
        maze1.display()

    print("\nYou Win!\n")


if __name__ == "__main__":
    main()
