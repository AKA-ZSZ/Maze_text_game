from abc import ABC, abstractmethod


class AbstractView(ABC):
    """ Template for views

    Defines `_display_message' and  'display_instructions' as abstractmethods.

    """

    def display_message(self):
        """Method to display message"""
        # print(self._display_message())
        self._display_message()

    def display_instructions(self, *args, **kargs):
        # print(self._display_instructions())
        self._display_instructions(*args, **kargs)

    @abstractmethod
    def _display_instructions(self):
        pass

    @abstractmethod
    def _display_message(self):
        pass
