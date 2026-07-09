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

    cpu_letter = "O" if user_letter == "X" else "X"
    human = Player("Player", user_letter)
    cpu = CPU("CPU", cpu_letter)

    game_board = Board()

    while len(game_board.get_open_spots()) > 0:
        
        game_board.display()
        print("Your move!")

        try:
            """exception handeling"""
            """sees if a letter instead of number was typed"""
            current_pick = int(input("Pick an open spot (1-9): "))

            """bounds validation"""
            if current_pick < 1 or current_pick > 9:
                print("Error: Pick a number between 1 and 9")
                continue

            """spot check"""
            if game_board.spots[current_pick - 1] in ["X", "O"]:
                print("That spot is already taken!")
                continue
        
        except ValueError:
            "catches runtime error if int() fails"
            print("Invalid input! You must type an integer number")
            continue

        """Validate player move"""
        game_board.update_spot(current_pick - 1, human.letter)

        """checks win"""
        if game_board.check_win(human.letter):
            game_board.display()
            print('You Win!!!')
            scores["Player"] += 1
            break

        """CPU Turn"""
        open_spots = game_board.get_open_spots()
        if len(open_spots) > 0:
            print("\n The Computer is Picking a spot...")
            cpu_choice = cpu.pick_spot(open_spots)
            game_board.update_spot(cpu_choice -1, cpu.letter)

            """win check for cpu"""
            if game_board.check_win(cpu.letter):
                game_board.display()
                print("Computer Wins...")
                scores["CPU"] += 1
                break

    
    