"""
main.py
Joel Bratt
Main program that runs the tic tac toe loop, handels exceptions,
and imports custom modules.
7/9/2026
"""
from classes import Board, Player, CPU
import scoreboard

def main():
    """Main execution function to run the game."""
    print("Welcome to Modular Tic-Tac-Toe!")

    scores = scoreboard.load_scores()
    scoreboard.display_scoreboard(scores)

    user_letter = input("Would you like to be O's or X's ").upper()
    while user_letter not in ["X", "O"]:
        user_letter = input("Invalid. Type X or O ").upper()
    print('Great, Lets continue')