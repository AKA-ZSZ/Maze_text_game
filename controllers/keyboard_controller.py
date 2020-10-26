class KeyboardController:
    def __init__(self):
        pass


    def get_action(self):
        # a list of command that the game would recognize
        input_list = ("w", "a", "s", "d", "q")
        user_input=""
        
        while user_input not in input_list:
            try:
                user_input=input()

                # if the input is not recognized by the game, user need to enter another command
                if user_input in input_list:
                    return user_input
            except IndexError():
                continue
