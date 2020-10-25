# import pytest
# from unittest.mock import mock_open, patch
# from maze import Maze

# @patch('builtins.open', mock_open(read_data='  XXX\n' + '   XX  \n' + ' X X   \n'
#                                                 'X     X\n' + 'XXX   X'))
# def test_init_load_all():
#     # maze = Maze()
#     assert len(Maze) == 5
#     # assert students[0].name == 'Tim'
#     # assert students[0].gpa == 70