class KeyboardController:
    def __init__(self):
        # self._user_input = user_input
        # input_list = ["w", "a", "s", "d", "q"]
        # if user_input in input_list:
        #     self._user_input = user_input
        # else:
        #     raise ValueError(f"'{user_input}' is not a valid command.")
        self._user_input = ""

    @property
    def user_input(self):
        return self._user_input

    def get_action(self):
        input_list = ["w", "a", "s", "d", "q"]
        if self._user_input in input_list:
            return self._user_input
        else:
            raise ValueError(f"'{self._user_input}' is not a valid command.")