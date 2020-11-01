from .abstract_view import AbstractView
import pygame

class WelcomeView(AbstractView):
    """ Display the Game Welcome view. Inherits from "AbstractView"
    """
    def __init__(self,window):
        self._window=window
        # Paint the screen white
        self._window.fill((255, 255, 255))

        pygame.font.init()
        self._arial = pygame.font.SysFont('arial', 18)
        

    
    def _display_message(self):
        """Template method: display the initial welcome message

        Returns:
            str: welcome message
        """
        # return "Welcome to our maze game!!"
        
        msg="Welcome to our maze game!!"
        msg_surface=self._arial.render(msg,True,(0,0,0))
        msg_text=msg_surface.convert_alpha()

        self._window.blit(msg_text,(155,180))
        




    def _display_instructions(self):
        """Template method: display the game start instructions

        Returns:
            str: instruction message
        """
        # return "Press w/a/s/d to start the game"
        instruction="Press w/a/s/d to start the game"

        ins_surface=self._arial.render(instruction,True,(0,0,0))
        ins_text=ins_surface.convert_alpha()

        self._window.blit(ins_text,(155,200))
