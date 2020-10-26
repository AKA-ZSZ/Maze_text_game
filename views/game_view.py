
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

    def get_items(self):
        self._maze.get_item()

    # _init_display
    def _display_maze(self):

        text = ""
        for line in self._maze.structure:
            text += ("").join(line)
            text += "\n"
        return text


    #refresh the map every time game controller calls the view
    # def _refresh(self):
    #     pass


