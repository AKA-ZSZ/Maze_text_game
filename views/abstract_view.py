from abc import ABC, abstractmethod


class AbstractView(ABC):
    """ Template for views

    Defines `_display_message as abstractmethods.

    """

    def display_message(self):
        print(self._display_message())

    @abstractmethod
    def _display_message(self):
        pass

