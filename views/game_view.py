
class GameView:

    def __init__(self,maze):
        # if not isinstance(maze, List):
        #     raise TypeError("Maze must be list")

        self._maze = maze

    def display_move_options(self):
        print(self._display_move_options())

    def _display_move_options(self):
        return "type w,a,s,d to move the player: "

    def display_maze(self):
        print(self._display_maze())

    def refresh(self):
        print(self._refresh())

    # _init_display
    def _display_maze(self):

        #randomly select 5 spots, player and exit
        max_spots_len=len(self._maze.items)
        i=0
        while i< max_spots_len:
            random_spot=self._maze.find_random_spot()
            if self._maze.check_position(random_spot[0],random_spot[1]):
                if not self._maze.is_item(random_spot[0], random_spot[1]):
                    # record initial location
                    self._maze.locations[self._maze.items[i]]=random_spot

                    # write items into maze map
                    self._maze.structure[random_spot[0]][random_spot[1]]=self._maze.items[i]

                    i+=1

        text = ""
        for line in self._maze.structure:
            text += ("").join(line)
            text += "\n"
        return text


    #refresh the map every time game controller calls the view
    def _refresh(self):
        pass
