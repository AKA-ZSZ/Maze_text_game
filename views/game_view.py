
class GameView:

    def __init__(self,maze):
        if not isinstance(maze, object):
            raise TypeError("Maze must be object")

        self._maze = maze

    def display_move_options(self):
        print(self._display_move_options())

    def display_maze(self):
        print(self._display_maze())

    def get_items(self,items):
        print(self._get_items(items))

    def _get_items(self, items):
        return f"""Get an item!\nYou have: {items}.\n"""

    def _display_move_options(self):
        return "type w,a,s,d to move the player: "

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


