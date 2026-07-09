"""
classes.py
Joel Bratt
contains the classes that will be used in the game of tic tac toe.
7/8/26
"""
import random

class Board:
    """This will be the tic tac toe board and its logic."""

    def __init__(self):
        """Initializes board with the spots of 1-9 and defines win conditions. """
        self.spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.wincons = [
    #Horizontal
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    #Columns
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    #diag
    (0, 4, 8), (2, 4, 6)
    ]
    
    def display(self):
        """Displays the game state to the console using print."""
        print(
        f' {self.spots[0]} | {self.spots[1]} | {self.spots[2]} \n'
        f'----------\n'
        f' {self.spots[3]} | {self.spots[4]} | {self.spots[5]} \n'
        f'----------\n'
        f' {self.spots[6]} | {self.spots[7]} | {self.spots[8]} \n')
    
    def get_open_spots(self):
        """Returns the positions on the board that are yet to be taken"""
        return [spot for spot in self.spots if isinstance(spot, int)]
