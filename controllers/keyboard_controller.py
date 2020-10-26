class KeyboardController:
    def __init__(self):
        # self._user_input = user_input
        # input_list = ["w", "a", "s", "d", "q"]
        # if user_input in input_list:
        #     self._user_input = user_input
        # else:
        #     raise ValueError(f"'{user_input}' is not a valid command.")
        # self._user_input = ""
        pass

    # @property
    # def user_input(self):
    #     return self._user_input

    def get_action(self):
        input_list = ("w", "a", "s", "d", "q")
        user_input=""
        
        while user_input not in input_list:
            # print('Please enter w/a/s/d:')
            user_input=input()

        return user_input
        # if self._user_input in input_list:
        #     return self._user_input
        # else:
        #     raise ValueError(f"'{self._user_input}' is not a valid command.")